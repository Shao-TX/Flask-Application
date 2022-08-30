from inference import toArduino, text_emotion
from generate import g_img_1
import os

from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.values['username'])
        return 'Hello' + request.values['username']

    return render_template('login.html')

# 測試用
@app.route("/test")
def test(): 
    return render_template('test.html')

# 負責處理 Arduino 開關
@app.route("/control_arduino", methods=['POST', 'GET'])
def arduino():
    if request.method == 'POST':
        data = (request.get_data()).decode('utf-8')
        toArduino(data)

        return "Turn " + data

# 負責處理文字生成圖像
@app.route("/generate_image", methods=['POST', 'GET'])
def generate_image():
    if request.method == 'POST':
        data = (request.get_data()).decode('utf-8')
    
    g_img_1(data)

    return data

# 負責處理文字情緒辨識
@app.route("/text_emotion", methods=['POST', 'GET'])
def text_emoiton():
    if request.method == 'POST':
        data = (request.get_data()).decode('utf-8')
    
    print("情緒辨識中...")
    emotion = text_emotion(data)

    return emotion

if __name__ == "__main__":
    app.debug=True
    app.run()