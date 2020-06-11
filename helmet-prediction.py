from matplotlib import pyplot as plt, patches
from matplotlib import image
from tkinter import filedialog
from tkinter import *
import json
import csv
import os.path

plt.rcParams.update({'font.size': 8})
path = "test_img.jpg"

# SEND TO API HELMET DETECTION

# SEND TO API FACE RECOGNITION

# PRINT IMAGE DETECTION WITH PROBABILITIES

json_test = json.load(open("test.json"))
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
img = plt.imread(root.filename)
figure, ax = plt.subplots(1)
prediction_list = json_test["predictions"]
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
        #TODO Save image
        plt.show()
        if not os.path.exists('test.csv'):
            with open('test.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["id","user", "helmet", "proba","date"])
        else:
            with open('test.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["1","toto", "yes", "0.95","12 juin"])


            
root.destroy()
root.quit()
# PRINT IF SAS OPEN OR NOT

# WRITE ON CSV THE RESULT

# PUSH IMAGE ON DATALAKE
