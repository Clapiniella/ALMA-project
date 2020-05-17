from keras.preprocessing.image import img_to_array
import imutils
import cv2
from keras.models import load_model
import src.constants as const
import numpy as np
import json
from querysql import addEmo
from keras.models import model_from_json

with open('../models/Model_0.6708552837371826_17-0-29.json','r') as f:
    model_json = json.load(f)
model = model_from_json(model_json)
model.load_weights('../models/Model_0.6708552837371826_17-0-29.h5')

face_cascade = cv2.CascadeClassifier('../files/haarcascade_frontalface_default.xml')


def webcam(counttoclose, idvideo):
    cap = cv2.VideoCapture(0)
    counter=125
    while cap.isOpened(): # True:
        counter+=1
        frame = cap.read()[1]
        frame = imutils.resize(frame, width=400)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.25, 6)
        canvas = np.zeros((300, 300, 3), dtype="uint8") 
        frameClone = frame.copy()
    
        if len(faces) > 0:
            (fX, fY, fW, fH) = faces[0]
            roi = gray[fY:fY + fH, fX:fX + fW]
            roi = cv2.resize(roi, (48, 48))
            roi = roi/ 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0).reshape(np.expand_dims(roi,axis=0).shape[0], 48, 48, 1)

            if counter >= 10:       
                preds = model.predict(roi)[0]   
                #emotion_probability = np.max(preds) 
                label = const.EMOTIONS[preds.argmax()]
                addEmo(idvideo, preds) #querysql function
                counter=0
        
            cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
                                        (250,128,114), 1) #square surrounded face

            for (i, (emotion, prob)) in enumerate(zip(const.EMOTIONS, preds)):
                        # construct the label text
                        text = "{}: {:.2f}%".format(emotion, prob * 100)
                        w = int(prob * 300)
                        cv2.rectangle(canvas, (7, (i * 35) + 5),
                        (w, (i * 35) + 35), (250,128,114), -1)
                        cv2.putText(canvas, text, (10, (i * 35) + 23),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45,
                        (255,255,255), 2)
                        cv2.putText(frameClone, label, (fX, fY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (250,128,114), 2) 
            
    
        numpy_horizontal_concat = np.concatenate((frameClone, canvas), axis=1)
        cv2.imshow('ALMA project', numpy_horizontal_concat)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        counttoclose+=1
        print(counttoclose)
        if counttoclose == 300:
            cap.release()
    cap.release()
    cv2.destroyAllWindows()
    return 'works!'

counttoclose = 0
