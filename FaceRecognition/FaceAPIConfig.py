#!/usr/bin/env python3

import asyncio
import io
import glob
import os
import sys
import time
import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType


def initFaceClient():
    KEY = '5250cc4496a74ceca28563b13b083a01'
    ENDPOINT = 'https://westeurope.api.cognitive.microsoft.com/'
    return FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))


def initGroup(face_client, PERSON_GROUP_ID):
    print('Person group:', PERSON_GROUP_ID) #Person Group ID must be lower case, alphanumeric, and/or with '-', '_'
    if (findGroupID(face_client, PERSON_GROUP_ID)):
        face_client.person_group.get(person_group_id=PERSON_GROUP_ID)
    else:
        print('InitGroup: Create new person group {}'.format(PERSON_GROUP_ID))
        face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID)

    dirname = './dataset2/'
    list_sub_dir = os.listdir(dirname)
    list_person = {}
    for sub_dir in list_sub_dir:
        list_person[sub_dir] = face_client.person_group_person.create(PERSON_GROUP_ID, sub_dir)
    data_set = initDataSet()

    for person in data_set:
        for image in data_set[person]:
            img = open(image, 'r+b')
            id = list_person[person].person_id
            try:
                face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, id, img)
            except:
                print(image)

def initDataSet():
    data_set = {}
    dirname = './dataset2/'
    list_sub_dir = os.listdir(dirname)
    for sub_dir in list_sub_dir:
        data_set[sub_dir] = [dirname + sub_dir + '/' + file for file in os.listdir(dirname + sub_dir)]
    return data_set


def trainFaceClient(face_client, PERSON_GROUP_ID):
    print()
    print('Training the person group...')
    face_client.person_group.train(PERSON_GROUP_ID)

    while (True):
        training_status = face_client.person_group.get_training_status(PERSON_GROUP_ID)
        print("Training status: {}.".format(training_status.status))
        print()
        if (training_status.status is TrainingStatusType.succeeded):
            break
        elif (training_status.status is TrainingStatusType.failed):
            sys.exit('Training the person group has failed.')
        time.sleep(5)

def openMyImg(path):
    IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    image_array = glob.glob(os.path.join(IMAGES_FOLDER, path))
    return open(image_array[0], 'r+b')


def predictFaceClient(face_client, image, PERSON_GROUP_ID):
    dict_face_recognition = {}
    face_ids = []
    faces = face_client.face.detect_with_stream(image)
    if len(faces) == 0:
        return {}
    for face in faces:
        face_ids.append(face.face_id)
    results = face_client.face.identify(face_ids, PERSON_GROUP_ID) # Identify faces
    for person in results:
        if len(person.candidates) > 0:
            name = face_client.person_group_person.get(PERSON_GROUP_ID, person.candidates[0].person_id).name
            dict_face_recognition[name] = getCoordinatesAndConfidence(person, faces)
    return dict_face_recognition

def getCoordinatesAndConfidence(person, faces):
    face = None
    for f in faces:
        if f.face_id == person.face_id:
            face = f
            break

    rect = face.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height
    confidence = person.candidates[0].confidence
    return [top, bottom, left, right, confidence]

def getRectangle(faceDictionary):
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height
    return ((left, top), (right, bottom))

def cleanModel(face_client, PERSON_GROUP_ID):
    if findGroupID(face_client, PERSON_GROUP_ID):
        face_client.person_group.delete(person_group_id=PERSON_GROUP_ID)

def findGroupID(face_client, GROUP_ID):
    list_person_group = face_client.person_group.list()
    for person in list_person_group:
        if person.name == GROUP_ID:
            return 1
    print('No person group {} exist'.format(PERSON_GROUP_ID))
    return 0

def testModel(face_client, GROUP_ID):
    files = os.listdir('test')
    for file in files:
        img = openMyImg('test/' + file)
        print(file + ' => ')
        print(predictFaceClient(face_client, img, GROUP_ID))
        print()

if __name__ == '__main__':
    PERSON_GROUP_ID = 'my-unique-person-groupe'
    face_client = initFaceClient()
    #cleanModel(face_client, PERSON_GROUP_ID)
    #initGroup(face_client, PERSON_GROUP_ID)
    #trainFaceClient(face_client, PERSON_GROUP_ID)

    #img = openMyImg(sys.argv[1])
    #print(predictFaceClient(face_client, img, PERSON_GROUP_ID))
    testModel(face_client, PERSON_GROUP_ID)
