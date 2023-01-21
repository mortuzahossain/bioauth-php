
import jsonpickle
import pandas as pd
from cv2 import *
from PIL import Image
import numpy as np
from face_recognition import FaceRecognition
from watcher import *
import json

import os
import os.path
from io import BytesIO
from base64 import b64decode

import random  
import string  
import mysql.connector


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="admin",
  password="p1234",
  database="bioauth"
)



def RandomString(length): 
    return ''.join((random.choice(string.ascii_lowercase) for x in range(length)))



faceDetactor = CascadeClassifier('haarcascade_frontalface_default.xml')
fr = FaceRecognition()
fr.load('model.pkl')

#app = Flask(__name__)
#api = Api(app)

@app.route('/', methods = ['GET'])
@cross_origin()
def test():
    response = {'RespMsg':'Welcome to Image Authentication API','RespCode':100}
    return Response(response=jsonpickle.encode(response), status=200, mimetype="application/json")

BASE_PATH_TRAIN = 'train/'
@app.route('/register', methods = ['POST'])
def registerUser():
    if request.is_json:
        try:
            content = request.get_json()
            images = content['images']
            userid = content['userid']
            name = content['name']
            email = content['email']
            password = content['password']

            file_path = BASE_PATH_TRAIN+userid
            if not os.path.exists(file_path):
                os.mkdir(BASE_PATH_TRAIN+userid)

            for i in range(0,len(images)):
                im = Image.open(BytesIO(b64decode(images[i])))
                im.save(file_path+"/"+str(i)+".jpg")
            
            response = {'RespMsg':'Registration success','RespCode':100}
            # Watcher.add_new(1)

            # Inserting into database
            mycursor = mydb.cursor()
            mycursor.execute("insert into watcher (userid,name,email,password,isNewUserRegistered,status) values ('%s','%s','%s','%s','%s','%s')" % (userid,name,email,password,1,1))
            mydb.commit()

            return  Response(response=jsonpickle.encode(response), status=200, mimetype="application/json")
        except Exception as e:
            response = {'RespMsg':'Exception '+str(e),'RespCode':104}
            return  Response(response=jsonpickle.encode(response), status=200, mimetype="application/json")
        
    else:
        response = {'RespMsg':'Please provide valid json formate','RespCode':103}
        return Response(response=jsonpickle.encode(response), status=200, mimetype="application/json")



BASE_PATH_TEST = 'userupload/'
@app.route('/', methods = ['POST'])
@cross_origin()
def imageRecognizer():
    if request.is_json:
       try:
            content = request.get_json()
            image = content['image']
            im = Image.open(BytesIO(b64decode(image)))
            imagepath = os.path.abspath(BASE_PATH_TEST+RandomString(20)+'.jpg')
            im.save(imagepath)
            img = imread(imagepath)
            gray = cvtColor(img,COLOR_BGR2GRAY)

            faces = faceDetactor.detectMultiScale(gray,1.3,5)
            if len(faces) == 0:
                response = {'RespMsg':'No face detected.','RespCode':102}
                return Response(response=jsonpickle.encode(response), status=200, mimetype="application/json")
            if len(faces)>1:
                response = {'RespMsg':'Multiple face detected.','RespCode':101}
                return Response(response=jsonpickle.encode(response), status=200, mimetype="application/json")
            fr.load('model.pkl')
            result = fr.predict(imagepath)
            confidence = result['predictions'][0]['confidence']
            person = result['predictions'][0]['person']
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM watcher WHERE userid = "+person)
            userinfo = mycursor.fetchall()
            row_headers=[x[0] for x in mycursor.description] 
            json_data=[]
            for result in userinfo:
                json_data.append(dict(zip(row_headers,result)))
            response = {'RespMsg':'Face Present In database','RespCode':100,'UserId':person,'userinfo':json_data[0],'Confidence':confidence.item()}
            return  Response(response=jsonpickle.encode(response), status=200, mimetype="application/json")

            response = {'RespMsg':'No face detected.','RespCode':102}
            return  Response(response=jsonpickle.encode(response), status=200, mimetype="application/json")
       except Exception as e:
           response = {'RespMsg':'Exception '+str(e),'RespCode':104}
           return  Response(response=jsonpickle.encode(response), status=200, mimetype="application/json")
        
    else:
        response = {'RespMsg':'Please provide valid json formate','RespCode':103}
        return Response(response=jsonpickle.encode(response), status=200, mimetype="application/json")


if __name__ == '__main__':
    app.run()
