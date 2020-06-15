from matplotlib import pyplot as plt, patches
from matplotlib import image
from tkinter import filedialog
from tkinter import *
import json
import csv
import os.path
import http.client, urllib.request, urllib.parse, urllib.error, base64
import re
from FaceRecognition.FaceAPIConfig import initFaceClient, predictFaceClient, initGroup
from datetime import datetime
from azure.storage.blob import BlockBlobService


path = "test_img.jpg"
plt.rcParams.update({'font.size': 8})
PRED_KEY = "15e2e8487c2b470c8770d173ff939b8a"
ZONE_AZURE = "westeurope.api.cognitive.microsoft.com"
PROJECT_ID = "e1d47eeb-1e08-480c-9e0c-485b59dc6bd6"
PROJECT_NAME = "test%20prediction%20model"

ACCOUNT_NAME = 'imagestoragehelmet'
ACCOUNT_KEY = 'OVP3UZeeo8YjT/wAyZ35mJeMhKmPbt3T8AP0xAhbEHOMC5t0ImT3t7PtTOrYN3B9Jqaq1HmKpljIO7jTwHLFYQ=='
CONTAINER_NAME_IMAGE = 'imagecontainer'
CONTAINER_NAME_CSV = "csvcontainer"

def get_img():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file"
            ,filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    img = plt.imread(root.filename)
    name = root.filename
    root.destroy()
    root.quit()
    return img, name


def add_data(file,tab):
    if not os.path.exists(file):
        with open(file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["id","user","probaUser", "tag", "probaTag","date","emotion" ])
                writer.writerows(tab)
    else:
        with open(file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(tab)
                
    
def read_answer_api_helmet(json_test, img):
    json_test = json.loads(json_test)
    prediction_list = json_test["predictions"]
    figure, ax = plt.subplots(1)
    tab = []
    rect_list = []
    for predic in prediction_list:
        if predic["probability"] > 0.5:
            #print("prediction detected ! It is:" + predic["tagName"])
            left_corner = predic["boundingBox"]["left"] * img.shape[1]
            top_corner = predic["boundingBox"]["top"] * img.shape[0]
            width = predic["boundingBox"]["width"] * img.shape[1]
            height = predic["boundingBox"]["height"] * img.shape[0]
            rect_list.append([left_corner, top_corner, width, height, predic["probability"] * 100, predic["tagName"]])
            tab.append([json_test["id"],"toto",predic["tagName"],predic["probability"],json_test["created"], left_corner, top_corner, left_corner + width, top_corner + height])
    for r in rect_list:
        rect = patches.Rectangle((r[0], r[1]), r[2], r[3], edgecolor='r', facecolor="none")
        rect2 = patches.Rectangle((r[0], r[1] - 20), r[2],20, color='r')
        ax.add_patch(rect)
        ax.add_patch(rect2)
        plt.text(r[0] + 5, r[1] - 5,  r[5] + ": "+ str(round(r[4],1)) + "%", color="white")
    ax.imshow(img)
    plt.savefig("result.png",bblob_inches='tight')
    plt.show()
    return tab


def send_api_helmet(filename):
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Prediction-key': PRED_KEY,
    }
    try:
        conn = http.client.HTTPSConnection(ZONE_AZURE)
        img_data = open(filename, "rb").read()
        conn.request("POST", "/customvision/v3.0/Prediction/{0}/detect/iterations/{1}/image".format(PROJECT_ID, PROJECT_NAME) , img_data, headers)
        response = conn.getresponse()
        json_test = response.read()
        #print(data)
        conn.close()
        return json_test
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def send_face_recognition(filename):
    PERSON_GROUP_ID = "my-unique-person-groupe"
    face_client = initFaceClient()
    pic = open(filename, 'r+b')
    #iinitGroup(face_client, PERSON_GROUP_ID)
    res = predictFaceClient(face_client, pic, PERSON_GROUP_ID)
    pic.close()
    return res
    
def print_face_img(faces, img):
    figure, ax = plt.subplots(1)
    for name, r in faces.items():
        print(r)
        rect = patches.Rectangle((int(r[2]), int(r[0])), int(r[3]- r[2]), int(r[1]- r[0]), edgecolor='r', facecolor="none")
        rect2 = patches.Rectangle((int(r[2]), int(r[0]) - 20), r[3] - r[2],20, color='r')
        ax.add_patch(rect)
        ax.add_patch(rect2)
        plt.text(int(r[2]) + 5, int(r[0]) - 5,  name[5:] + ": "+ str(round(r[4]*100,1)) + "%", color="white")
    ax.imshow(img)
    #plt.savefig("result.png",bblob_inches='tight')
    plt.show()

def compute_score(face, t):
    topDif = face[0] - t[6]
    leftDif = face[2] - t[5]
    rightDif = face[3] - t[7]
    bottomDif = face[1] - t[8]
    return abs(topDif) + abs(leftDif) + abs(rightDif) + abs(bottomDif)

def create_row_csv(face_detected, tabs):
    rows = []
    for name, face in face_detected.items():
        min = 999999
        min_val = None
        i = 0
        for t in tabs:
            res = compute_score(face,t)
            if res < min:
                min = res
                min_val = t
        del tabs[tabs.index(min_val)]
        rows.append([min_val[0],name[5:],face[4] ,min_val[2],min_val[3], min_val[4], face[5] ])
    return rows

def main():
    img, filename = get_img()
    ############## FOR TESTING ########
    #filename = "img.jpg"
    #img = plt.imread("img.jpg")
    ##################################

    json_res = send_api_helmet(filename)
    face_detected = send_face_recognition(filename)
    print_face_img(face_detected, img)
    tab = read_answer_api_helmet(json_res, img)
    date = datetime.today().strftime(("%Y-%m-%d"))
    csv_name = str(date) + ".csv" 
    rows = create_row_csv(face_detected, tab)
    if len(rows) == 0:
        print("SAS closed. Unknow face detected")
    else:
        res = 0
        for row in rows:
            print(row[1] + " was detected on the photo with " + row[3])
            if row[3] == "no helmet":
                res = 1
        if res == 0:
            print("SAS open.")
        else:
            print("SAS closed.")
    print(rows)
    add_data( csv_name,rows)
    block_blob_service = BlockBlobService(
        account_name=ACCOUNT_NAME,
        account_key=ACCOUNT_KEY
    )
    block_blob_service.create_blob_from_path(CONTAINER_NAME_IMAGE, re.split("/", filename)[-1], filename)
    block_blob_service.create_blob_from_path(CONTAINER_NAME_CSV, csv_name, csv_name)   

main()
