# import the require packages.
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QLabel, QGridLayout, QScrollArea, QSizePolicy, QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QImage, QPalette
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QEvent, QObject
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys
from PyQt5 import *
from PyQt5 import QtWidgets
import cv2
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
from tkinter import *
import tkinter as tk
import pyautogui as pg
import time
from PIL import Image

def CaptureCam(url):
    ImageUpdate = pyqtSignal(QImage)

    #init variables
    threadActive = True
    capture = cv2.VideoCapture(url)

    if capture.isOpened():
        while threadActive:
            ret, frame = capture.read() #gets videocapture cams stream

            if ret:
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) == ord('q'):
                    break

            else:
                break 
    capture.release()
    
url_1 = 0
url_2 = 1

camera_1 = QLabel()
camera_1.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
camera_1.setScaledContents(True)
camera_1.installEventFilter(self)