import io
from os import close
from typing import Any
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import folium
import sys

fontsize = 25
def leftLayout(self):
    left_layout = QVBoxLayout()
    m = folium.Map(location=[40.74227, 30.33177],zoom_start=15)
    map_data = io.BytesIO()
    m.save(map_data, close_file=False)
    googleMap = QWebEngineView()
    googleMap.setHtml(map_data.getvalue().decode())
    left_layout.addWidget(googleMap)
    return left_layout
def rightLayout(self):
    #design
    right_layout = QGridLayout() #y,x
    vangle_text = QLabel("verticalAngle")
    vangle_text.setObjectName("vangle_text")
    vangle_text.setFont(QFont("Arial",fontsize))
    hangle_text = QLabel("horizontalAngle")
    hangle_text.setObjectName("hangle_text")
    hangle_text.setFont(QFont("Arial",fontsize))
    #add
    right_layout.addLayout(altitudeLayout(),0,0,alignment=Qt.AlignCenter)
    right_layout.addLayout(speedLayout(),0,1,alignment=Qt.AlignCenter)
    right_layout.addLayout(vAngleLayout(),1,0,alignment=Qt.AlignCenter)
    right_layout.addLayout(hAngleLayout(),1,1,alignment=Qt.AlignCenter)
    return right_layout
def altitudeLayout():
    altitude_layout = QVBoxLayout()
    altitude_value = QLabel("deger")
    altitude_value.setObjectName("altitude_value")
    altitude_value.setFont(QFont("Arial", fontsize))
    altitude_text = QLabel("Altitude (m)")
    altitude_text.setFont(QFont("Arial",10))
    altitude_text.setObjectName("text")
    altitude_layout.addWidget(altitude_text, alignment=Qt.AlignCenter)
    altitude_layout.addWidget(altitude_value, alignment=Qt.AlignCenter)
    return altitude_layout
def speedLayout():
    speed_layout = QVBoxLayout()
    speed_value = QLabel("deger")
    speed_value.setObjectName("speed_value")
    speed_value.setFont(QFont("Arial", fontsize))
    speed_text = QLabel("groundSpeed (m/s)")
    speed_text.setFont(QFont("Arial",10))
    speed_text.setObjectName("text")
    speed_layout.addWidget(speed_text, alignment=Qt.AlignCenter)
    speed_layout.addWidget(speed_value, alignment=Qt.AlignCenter)
    return speed_layout
def vAngleLayout():
    vAngle_layout = QVBoxLayout()
    vAngle_value = QLabel("deger")
    vAngle_value.setObjectName("vAngle_value")
    vAngle_value.setFont(QFont("Arial", fontsize))
    vAngle_text = QLabel("Vertical Angle")
    vAngle_text.setFont(QFont("Arial",10))
    vAngle_text.setObjectName("text")
    vAngle_layout.addWidget(vAngle_text, alignment=Qt.AlignCenter)
    vAngle_layout.addWidget(vAngle_value, alignment=Qt.AlignCenter)
    return vAngle_layout
def hAngleLayout():
    hAngle_layout = QVBoxLayout()
    hAngle_value = QLabel("deger")
    hAngle_value.setObjectName("hAngle_value")
    hAngle_value.setFont(QFont("Arial", fontsize))
    hAngle_text = QLabel("Horizontal Angle")
    hAngle_text.setFont(QFont("Arial",10))
    hAngle_text.setObjectName("text")
    hAngle_layout.addWidget(hAngle_text, alignment=Qt.AlignCenter)
    hAngle_layout.addWidget(hAngle_value, alignment=Qt.AlignCenter)
    return hAngle_layout