from matplotlib import pyplot as plt, patches
from matplotlib import image
from tkinter import filedialog
from tkinter import *
import json


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
        ax.add_patch(rect)
        ax.imshow(img)
        plt.show()
root.destroy()
# PRINT IF SAS OPEN OR NOT

# WRITE ON CSV THE RESULT
