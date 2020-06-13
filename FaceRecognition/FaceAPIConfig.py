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
        face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID)

    fayssal = face_client.person_group_person.create(PERSON_GROUP_ID, "Fayssal")
    other = face_client.person_group_person.create(PERSON_GROUP_ID, "Other")

    data_set = initDataSet()

    for person in data_set:
        for image in data_set[person]:
            img = open(image, 'r+b')
            id = fayssal.person_id
            if person == 'Other':
                id = other.person_id
            face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, id, img)

def initDataSet():
    data_set = {}
    data_set['fayssal'] = [file for file in glob.glob('*.jpg') if file.startswith("fayssal")]
    data_set['other'] = [file for file in glob.glob('*.jpg') if file.startswith("other")]
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
    print("results: " + str(results[0]))
    for person in results:
        if len(person.candidates) > 0:
            dict_face_recognition[person.face_id] = getCoordinatesAndConfidence(person, faces)
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

if __name__ == '__main__':
    PERSON_GROUP_ID = 'my-unique-person-group'
    face_client = initFaceClient()
    cleanModel(face_client, PERSON_GROUP_ID)
    initGroup(face_client, PERSON_GROUP_ID)
    trainFaceClient(face_client, PERSON_GROUP_ID)

    path = 'test-image-person-group.jpg'
    img = openMyImg(path)
    print(predictFaceClient(face_client, img, PERSON_GROUP_ID))
