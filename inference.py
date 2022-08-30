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

    for i in range(5):
        predict_list.append(prediction[0][i]['score'])

    print(max(predict_list))
    max_predict = predict_list.index(max(predict_list))

    return emotion_list[max_predict]

    """
    output:
    [[
    {'label': 'sadness', 'score': 0.0005138228880241513}, 
    {'label': 'joy', 'score': 0.9972520470619202}, 
    {'label': 'love', 'score': 0.0007443308713845909}, 
    {'label': 'anger', 'score': 0.0007404946954920888}, 
    {'label': 'fear', 'score': 0.00032938539516180754}, 
    {'label': 'surprise', 'score': 0.0004197491507511586}
    ]]  
    """ 