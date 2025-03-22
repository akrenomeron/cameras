from tkinter import *
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import pyscreenshot
import pygetwindow as gw
import pyscreeze
import keyboard
import threading
import time

width, height = 1570, 1440

url1 = 0
url2 = 1

url_streams = [url1, url2]
current_url = url_streams[0]

cam = cv2.VideoCapture(current_url)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

window = Tk()
window.title('one cam')
window.bind('<Escape>', lambda e: window.quit())

camDisplay = Label(window)
camDisplay.pack()

check = True

global index 
index = 0

def press(index):
    index += 1
    print(index)

def switch_cam():
    '''
    print("index now: " + str(index))
    keyboard.add_hotkey("right arrow", lambda: press(index))
    print("index after: " + str(index))
    '''
    index = 0
    while True:
       if keyboard.is_pressed("right arrow"):
            print("u pressed")
            index += 1
            #time.sleep(1)
            print(index)
            pass


#runs first cam stream
def open_camera():
    #read VideoCapture
    #print("getting frame 1")
    ret, frame1 = cam.read()

    #updates image settings
    opencv_image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
    captured_image1 = Image.fromarray(opencv_image1)
    photo_image1 = ImageTk.PhotoImage(image = captured_image1)
    camDisplay.photo_image1 = photo_image1
    camDisplay.configure(image=photo_image1)

    #updates frame
    camDisplay.after(10, open_camera)

switchThread = threading.Thread(target=switch_cam, daemon=True)
switchThread.start()

cameraThread = threading.Thread(target=open_camera, daemon=True)
cameraThread.start()

window.mainloop()