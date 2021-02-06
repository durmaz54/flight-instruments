import io
from os import close
from typing import Any
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import folium
import sys
import right_layout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,1280,920)
        self.setWindowTitle("Flight Instruments")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.setStyleSheet(open("style.qss","r").read())
        self.designLayout()
        self.show()
    
    def designLayout(self):
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(self.upLayout(),1)
        mainLayout.addLayout(self.midLayout(),7)
        mainLayout.addLayout(self.bottomLayout(),2)
        self.setLayout(mainLayout)
    def upLayout(self):
        up_layout = QHBoxLayout()
        text = QLabel("up layout")
        text.setObjectName("text")
        up_layout.addWidget(text)
        return up_layout
    def midLayout(self):
        mid_layout = QHBoxLayout()
        mid_layout.addLayout(self.leftLayout(),7)
        mid_layout.addLayout(self.rightLayout(),3)
        return mid_layout
    def bottomLayout(self):
        bottom_layout = QGridLayout()
        text2 = QLabel("bottom_layout")
        text2.setObjectName("text2")
        bottom_layout.addWidget(text2)
        return bottom_layout
    def rightLayout(self):
        self.fontsize = 25
        #design
        right_layout = QGridLayout() #y,x
        vangle_text = QLabel("verticalAngle")
        vangle_text.setObjectName("vangle_text")
        vangle_text.setFont(QFont("Arial",self.fontsize))
        hangle_text = QLabel("horizontalAngle")
        hangle_text.setObjectName("hangle_text")
        hangle_text.setFont(QFont("Arial",self.fontsize))
        #add
        right_layout.addLayout(self.altitudeLayout(),0,0,alignment=Qt.AlignCenter)
        right_layout.addLayout(self.speedLayout(),0,1,alignment=Qt.AlignCenter)
        right_layout.addLayout(self.vAngleLayout(),1,0,alignment=Qt.AlignCenter)
        right_layout.addLayout(self.hAngleLayout(),1,1,alignment=Qt.AlignCenter)
        return right_layout
    def altitudeLayout(self):
        altitude_layout = QVBoxLayout()
        altitude_value = QLabel("deger")
        altitude_value.setObjectName("altitude_value")
        altitude_value.setFont(QFont("Arial", self.fontsize))
        altitude_text = QLabel("Altitude (m)")
        altitude_text.setFont(QFont("Arial",10))
        altitude_text.setObjectName("text")
        altitude_layout.addWidget(altitude_text, alignment=Qt.AlignCenter)
        altitude_layout.addWidget(altitude_value, alignment=Qt.AlignCenter)
        return altitude_layout
    def speedLayout(self):
        speed_layout = QVBoxLayout()
        speed_value = QLabel("deger")
        speed_value.setObjectName("speed_value")
        speed_value.setFont(QFont("Arial", self.fontsize))
        speed_text = QLabel("groundSpeed (m/s)")
        speed_text.setFont(QFont("Arial",10))
        speed_text.setObjectName("text")
        speed_layout.addWidget(speed_text, alignment=Qt.AlignCenter)
        speed_layout.addWidget(speed_value, alignment=Qt.AlignCenter)
        return speed_layout
    def vAngleLayout(self):
        vAngle_layout = QVBoxLayout()
        vAngle_value = QLabel("deger")
        vAngle_value.setObjectName("vAngle_value")
        vAngle_value.setFont(QFont("Arial", self.fontsize))
        vAngle_text = QLabel("Vertical Angle")
        vAngle_text.setFont(QFont("Arial",10))
        vAngle_text.setObjectName("text")
        vAngle_layout.addWidget(vAngle_text, alignment=Qt.AlignCenter)
        vAngle_layout.addWidget(vAngle_value, alignment=Qt.AlignCenter)
        return vAngle_layout
    def hAngleLayout(self):
        hAngle_layout = QVBoxLayout()
        hAngle_value = QLabel("deger")
        hAngle_value.setObjectName("hAngle_value")
        hAngle_value.setFont(QFont("Arial", self.fontsize))
        hAngle_text = QLabel("Horizontal Angle")
        hAngle_text.setFont(QFont("Arial",10))
        hAngle_text.setObjectName("text")
        hAngle_layout.addWidget(hAngle_text, alignment=Qt.AlignCenter)
        hAngle_layout.addWidget(hAngle_value, alignment=Qt.AlignCenter)
        return hAngle_layout
    def leftLayout(self):
        left_layout = QVBoxLayout()
        m = folium.Map(location=[41.092628, 30.572079],zoom_start=15)
        self.map_data = io.BytesIO()
        m.save(self.map_data, close_file=False)
        googleMap = QWebEngineView()
        googleMap.setHtml(self.map_data.getvalue().decode())
        left_layout.addWidget(googleMap)
        return left_layout

app = QApplication(sys.argv)
window = Window()

sys.exit(app.exec_())
