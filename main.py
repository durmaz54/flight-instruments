import io
from os import close
from typing import Any
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import folium
import sys
import MidLayout

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
        text = QLabel("takım adı")
        text.setObjectName("text")
        text.setFont(QFont("Arial",25))
        up_layout.addWidget(text)
        return up_layout
    def midLayout(self):
        mid_layout = QHBoxLayout()
        mid_layout.addLayout(MidLayout.leftLayout(self),7)
        mid_layout.addLayout(MidLayout.rightLayout(self),3)
        return mid_layout
    
    def bottomLayout(self):
        bottom_layout = QGridLayout()
        text2 = QLabel("bottom_layout")
        text2.setObjectName("text2")
        bottom_layout.addWidget(text2)
        return bottom_layout
app = QApplication(sys.argv)
window = Window()

sys.exit(app.exec_())
