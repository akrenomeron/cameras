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

class ScrollCam(QMainWindow):
    def __init__(self):
        print("first")
        super().__init__()
        self.setWindowTitle("main cam")
        self.setMinimumSize(1990, 1800)

        self.url_1 = 0
        #self.url_1 = 'http://192.168.1.99:8080/stream'
        #self.url_2 = "http://192.168.1.99:8082/stream"
        self.url_2 = 1
        self.url_3 = "http://192.168.1.99:8084/stream"
        self.url_4 = "http://192.168.1.99:8086/stream" #photogrammetry cam
        self.url_5 =  "http://192.168.1.99:8088/stream"
        self.url_6 = "http://192.168.1.99:8090/stream"

        global cams_stream
        cams_stream = [self.url_1, self.url_2, self.url_3, self.url_4, self.url_5, self.url_6]
        global index
        index = 0

        self.capture = cv2.VideoCapture(cams_stream[index])

        self.camera_position = QLabel(self)
        self.camera_position.setAlignment(Qt.AlignCenter)

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.camera_position, 0, 0)

        self.widget = QWidget(self)
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(30)

    def updateCam(self):
        self.capture.release()
        self.capture = cv2.VideoCapture(cams_stream[index])
        
    def updateFrame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            height, width, channels = frame.shape
            bytes_per_line = width * channels  
            q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
            self.camera_position.setPixmap(QPixmap.fromImage(q_image))

    def keyPressed(self):
        index = (index + 1) % len(cams_stream)

    def closeEvent(self, event):    
        self.capture.release()
        super().closeEvent(event)    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScrollCam()
    window.show()
    #ScrollCam().show()
    sys.exit(app.exec_())