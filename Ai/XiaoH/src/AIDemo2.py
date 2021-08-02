# -*- coding: utf-8 -*-
#coding=utf-8
import tkinter
import pyttsx3
import pyaudio
import wave
from aip import AipSpeech
from aip import AipNlp
from tkinter import *
import threading
#from pil import ImageTk, Image
from PIL import Image,ImageTk

import time
root = tkinter.Tk


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        global root
        root = Tk()
        root.geometry('1024x1200')
        root.title('小辉')

        root.pilImage = Image.open("D:/temp/小太阳1.jpg")
        root.tkImage = ImageTk.PhotoImage(image=root.pilImage)
        root.Label = tkinter.Label(root, image=root.tkImage)
        root.Label.place(x=0, y=0)

        root.pilImage2 = Image.open("D:/temp/小太阳2.jpg")
        root.tkImage2 = ImageTk.PhotoImage(image=root.pilImage2)
        root.Label2 = tkinter.Label(root, image=root.tkImage2)

        lb = Label(root, text='你好，我是小辉。来和我聊天吧！但是你只有五秒钟的说话时间。', font=('宋体', 14), relief=GROOVE)
        lb.place(x=82, y=10, height=30, width=600)

        root.mainloop()


thread1 = myThread(1, "Thread-1", 1)
thread1.start()


class myThread2(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        root.pilImage = Image.open("D:/temp/小太阳1.jpg")
        root.tkImage = ImageTk.PhotoImage(image=root.pilImage)
        root.Label = tkinter.Label(root, image=root.tkImage)
        root.Label.place(x=0, y=0)

        root.pilImage2 = Image.open("D:/temp/小太阳2.jpg")
        root.tkImage2 = ImageTk.PhotoImage(image=root.pilImage2)
        root.Label2 = tkinter.Label(root, image=root.tkImage2)
        while True:
            root.Label2.place_forget()
            root.Label.place(x=0, y=0)
            time.sleep(0.4)
            root.Label.place_forget()
            root.Label2.place(x=0, y=0)
            time.sleep(0.4)


thread2 = myThread2(2, "Thread-2", 2)
thread2.start()


class myThread3(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        lb = Label(root, text=reply, font=('宋体', 14), relief=GROOVE)
        lb.place(x=500, y=175, height=30, width=600)

        root.pilImage3 = Image.open("D:/temp/you.jpg")
        root.tkImage3 = ImageTk.PhotoImage(image=root.pilImage3)
        root.Label3 = tkinter.Label(root, image=root.tkImage3)
        root.Label3.place(x=940, y=170)


thread3 = myThread3(3, "Thread-3", 3)


class myThread4(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        lb = Label(root, text=feedback, font=('宋体', 14), relief=GROOVE)
        lb.place(x=82, y=10, height=30, width=600)


thread4 = myThread4(4, "Thread-4", 4)


def use_pyttsx3(words):
    # 创建对象
    engine = pyttsx3.init()
    # 获取当前语音速率
    rate = engine.getProperty('rate')
    print(f'语音速率：{rate}')
    # 设置新的语音速率
    engine.setProperty('rate', 200)
    # 获取当前语音音量
    volume = engine.getProperty('volume')
    print(f'语音音量：{volume}')
    # 设置新的语音音量，音量最小为 0，最大为 1
    engine.setProperty('volume', 1.0)
    # 获取当前语音声音的详细信息
    voices = engine.getProperty('voices')
    print(f'语音声音详细信息：{voices}')
    # 设置当前语音声音为女性，当前声音不能读中文
    engine.setProperty('voice', voices[1].id)
    # 设置当前语音声音为男性，当前声音可以读中文
    engine.setProperty('voice', voices[0].id)
    # 获取当前语音声音
    voice = engine.getProperty('voice')
    print(f'语音声音：{voice}')
    # 将语音文本说出来
    engine.say(words)
    engine.runAndWait()
    engine.stop()


def use0_pyttsx3(words) -> object:
    # 语音文本
    path = 'd:/temp/greet.txt'
    with open(path, encoding='utf-8') as f_name:
        words = str(f_name.readlines()).replace(r'\n', '')
    use_pyttsx3(words)


if __name__ == '__main__':
    use0_pyttsx3('words')

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "d:/temp/output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

""" 你的 APPID AK SK """
APP_ID = '24481154'
API_KEY = 'VwLHBZQIZapOl0RE1CibwTVD'
SECRET_KEY = 'hbYNn0o413zGSuVO1RrMRo0I1Ej0ih1F'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


text = client.asr(get_file_content(WAVE_OUTPUT_FILENAME), 'WAV', 16000,
                  {
                      'dev_pid': 1537,
                  })
reply = text['result'][0]

print(reply)

thread3.start()

APP_ID = '24481154'
API_KEY = 'VwLHBZQIZapOl0RE1CibwTVD'
SECRET_KEY = 'hbYNn0o413zGSuVO1RrMRo0I1Ej0ih1F'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

""" 调用对话情绪识别接口 """
client.emotion(reply)

""" 如果有可选参数 """
options = {}
options["scene"] = "talk"

""" 带参数调用对话情绪识别接口 """
feedbacks = client.emotion(reply, options)['items'][0]['replies']

if feedbacks == []:
    print('...')
    feedback = '这可难倒我了，我居然不知道该怎么回答你，或许我太蠢了。'
else:
    print(feedbacks)
    feedback = feedbacks[0]
print('回复的文字：', feedback)
thread4.start()

use_pyttsx3(feedback)

while True:
    root.Label2.place_forget()
    root.Label.place(x=0, y=0)
    time.sleep(1)
    root.Label.place_forget()
    root.Label2.place(x=0, y=0)
    time.sleep(1)
