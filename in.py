import smtplib
import speech_recognition as sr
import pyttsx3
import requests
from email.message import EmailMessage

listener=sr.Recognizer()
engine=pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening..')
            voice=listener.listen(source)
            info=listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass

def sendmsg(msg):
    payload = {
    'content':"Welcome to Python project Expo"
    }
    header = {
    'authorization': 'MTA2NDkwMTg0NTY5MDEwMTgyMA.GAqHIh.Xiyk8_VXEZblk0S9xuLTvqDTTNqldJixmNppzk'
    }
    r = requests.post('https://discord.com/api/v9/channels/1064909552228778176/messages',data=payload,headers=header) #API key
    



def get_email_info():
    talk('Enter message you want to send to discord')
    msg=get_info()
    sendmsg(msg)
    talk('Your message is sent')
    talk('DO you want to send more message?')
    send_more=get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()