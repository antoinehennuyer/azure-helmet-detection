from matplotlib import pyplot as plt, patches
from matplotlib import image
from tkinter import filedialog
from tkinter import *
import json
import csv
import os.path
import http.client, urllib.request, urllib.parse, urllib.error, base64

plt.rcParams.update({'font.size': 8})
path = "test_img.jpg"
PRED_KEY = "15e2e8487c2b470c8770d173ff939b8a"
ZONE_AZURE = "westeurope.api.cognitive.microsoft.com"
PROJECT_ID = "e1d47eeb-1e08-480c-9e0c-485b59dc6bd6"
#json_test = json.load(open("test.json"))

def get_img():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file"
            ,filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    img = plt.imread(root.filename)
    root.destroy()
    root.quit()
    return img

def add_data(file,tab):
    if not os.path.exists(file):
        with open(file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["id","user", "tag", "proba","date"])
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
    for predic in prediction_list:
        if predic["probability"] > 0.5:
            print("prediction detected ! It is:" + predic["tagName"])
            left_corner = predic["boundingBox"]["left"] * img.shape[1]
            top_corner = predic["boundingBox"]["top"] * img.shape[0]
            width = predic["boundingBox"]["width"] * img.shape[1]
            height = predic["boundingBox"]["height"] * img.shape[0]
            rect = patches.Rectangle((left_corner, top_corner), width, height, edgecolor='r', facecolor="none")
            rect2 = patches.Rectangle((left_corner, top_corner - 20), 130,20, color = "r")
            ax.add_patch(rect2)
            ax.add_patch(rect)
            proba = predic["probability"] * 100
            plt.text(left_corner + 5, top_corner - 5, predic["tagName"] + ": "+ str(round(proba,1)) + "%", color="white")
            ax.imshow(img)
            plt.savefig("result.png",bblob_inches='tight')
            tab.append([json_test["id"],"toto",predic["tagName"],predic["probability"],json_test["created"]])
            plt.show()
    return tab





def send_api_helmet():
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Prediction-key': PRED_KEY,
    }



    try:
        conn = http.client.HTTPSConnection(ZONE_AZURE)
        img_data = open("test_img.jpg", "rb").read()
        conn.request("POST", "https://westeurope.api.cognitive.microsoft.com/customvision/v3.0/Prediction/e1d47eeb-1e08-480c-9e0c-485b59dc6bd6/detect/iterations/test%20prediction%20model/image" , img_data, headers)
        response = conn.getresponse()
        json_test = response.read()
        #print(data)
        conn.close()
        return json_test
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


#img = get_img()
img = plt.imread("test_img.jpg")

# SEND TO API HELMET DETECTION
json_res = send_api_helmet()

# SEND TO API FACE RECOGNITION

# PRINT IMAGE DETECTION WITH PROBABILITIES

tab = read_answer_api_helmet(json_res, img)


# PRINT IF SAS OPEN OR NOT


# WRITE ON CSV THE RESULT

add_data("toto.csv",tab)

# PUSH IMAGE ON DATALAKE
