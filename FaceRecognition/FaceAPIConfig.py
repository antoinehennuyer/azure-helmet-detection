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

    #face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID)
    face_client.person_group.get(person_group_id=PERSON_GROUP_ID)

    woman = face_client.person_group_person.create(PERSON_GROUP_ID, "Woman")
    man = face_client.person_group_person.create(PERSON_GROUP_ID, "Man")
    child = face_client.person_group_person.create(PERSON_GROUP_ID, "Child")

    data_set = initDataSet()

    for person in data_set:
        for image in data_set[person]:
            img = open(image, 'r+b')
            id = woman.person_id
            if person == 'Man':
                id = man.person_id
            elif person == 'Child':
                id = child.person_id
            face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, id, img)

def initDataSet():
    data_set = {}
    data_set['woman'] = [file for file in glob.glob('*.jpg') if file.startswith("woman")]
    data_set['man'] = [file for file in glob.glob('*.jpg') if file.startswith("man")]
    data_set['child'] = [file for file in glob.glob('*.jpg') if file.startswith("child")]
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
    for face in faces:
        face_ids.append(face.face_id)

    results = face_client.face.identify(face_ids, PERSON_GROUP_ID) # Identify faces
    print("results: " + str(results[0]))
    for person in results:
        dict_face_recognition[person.face_id] = getCoordinatesAndConfidence(person, faces)
    return  dict_face_recognition
    """
    print(dict_face_recognition)
    print('Identifying faces in {}'.format(os.path.basename(image.name)))
    if not results:
        print('No person identified in the person group for faces from {}.'.format(os.path.basename(image.name)))
    for person in results:
        print('Person for face ID {} is identified in {} with a confidence of {}.'.format(person.face_id, os.path.basename(image.name), person.candidates[0].confidence))
    base = Image.open(path).convert('RGBA')

    draw = ImageDraw.Draw(base)
    for face in faces:
        draw.rectangle(getRectangle(face), outline='red')

    base.show()
    """

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

if __name__ == '__main__':
    PERSON_GROUP_ID = 'my-unique-person-group'
    face_client = initFaceClient()
    initGroup(face_client, PERSON_GROUP_ID)
    trainFaceClient(face_client, PERSON_GROUP_ID)

    path = 'test-image-person-group.jpg'
    img = openMyImg(path)
    print(predictFaceClient(face_client, img, PRESON_GROUP_ID))
    print("OK")
