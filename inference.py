from transformers import pipeline

import serial
import os

try:
    ser = serial.Serial('/dev/ttyACM0', 9600)
except:
    ser = serial.Serial('/dev/ttyACM1', 9600)

def toArduino(state):
    ser.write(b'0\n') if state == "On" else ser.write(b'1\n')
    print("Serial : " + state)

def text_emotion(text):

    emotion_num = 5
    emotion_list = ["Sad", "Happy", "Love", "Angry", "Fear"]
    predict_list = []

    classifier = pipeline("text-classification",model='bhadresh-savani/bert-base-uncased-emotion', return_all_scores=True)
    prediction = classifier(text)

    print(prediction[0][0]["label"], prediction[0][0]['score'])
    print(prediction[0][1]["label"], prediction[0][1]['score'])
    print(prediction[0][2]["label"], prediction[0][2]['score'])
    print(prediction[0][3]["label"], prediction[0][3]['score'])
    print(prediction[0][4]["label"], prediction[0][4]['score'])

    for i in range(emotion_num):
        predict_list.append(prediction[0][i]['score'])

    print(max(predict_list))
    max_predict = predict_list.index(max(predict_list))

    return emotion_list[max_predict]

def text_summarization(input_text):

    classifier = pipeline("summarization")
    prediction = classifier(input_text)

    print(prediction)

    return prediction[0]['summary_text']