from face_recognition import FaceRecognition

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_curve, precision_recall_curve, roc_auc_score, accuracy_score

import matplotlib.pyplot as plt
import os
import glob
import pandas as pd
import random
import numpy as np
import cv2
import base64
from tqdm import tqdm
import requests
from pprint import pprint
import shutil


ROOT_Train ="train"
MODEL_PATH = "model.pkl"
BACKUP_MODEL_PATH = "backupmodels/"



import sqlite3
import time
import datetime
import mysql.connector
#cursor = conn.cursor()
# dbname = "database.db"

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="admin",
  password="p1234",
  database="bioauth"
)


def trainme():
    train = []
    print(str(datetime.datetime.now())+" <---------- Training -----------> ")
    for path in glob.iglob(os.path.join(ROOT_Train, "**", "*.jpg")):
        print(path)
        person = path.split("/")[-2]
        train.append({"person":person, "path": path})
    train = pd.DataFrame(train)
    fr = FaceRecognition()
    fr.fit_from_dataframe(train)
    # Backup previous model file
    original = MODEL_PATH
    target = BACKUP_MODEL_PATH+str(datetime.datetime.now())+"_model.pkl"
    shutil.copyfile(original, target)
    fr.save(MODEL_PATH)
    print(str(datetime.datetime.now())+" <---------- Finish -----------> ")
    pass
        



def updatedata(id):
    # conn = sqlite3.connect(dbname)
    print(str(datetime.datetime.now())+" <---------- Updating: "+str(id)+" -----------> ")
    # conn.execute("UPDATE watcher SET isNewUserRegistered=0 WHERE id = "+str(id))
    # conn.commit()
    # conn.close()
    
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE users SET isnew=0 WHERE id = "+str(id))
    mydb.commit()
    pass

while True:
    # conn = sqlite3.connect(dbname)
    # cursor = conn.execute("SELECT * from watcher WHERE isNewUserRegistered = 1")
    # alluser = cursor.fetchall()

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users WHERE isnew = 1")
    alluser = mycursor.fetchall()
    mydb.commit()
    print(alluser)

    if len(alluser) != 0:
        id = alluser[0][0]
        trainme()
        updatedata(id)
        pass

    # conn.commit()
    # conn.close()


    time.sleep(5)
    print(str(datetime.datetime.now())+" <---------- Watching -----------> ")
    pass


