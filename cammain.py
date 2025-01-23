import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QLabel, QGridLayout, QScrollArea, QSizePolicy, QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QImage, QPalette
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QEvent, QObject, QTimer
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import threading

import camsWindow
import onecam

window = threading.Thread(target=camsWindow.main)
key = threading.Thread(target=onecam.main)

window.start()
key.start()

window.join()
key.join()