from PyQt5.QtCore import right
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300,1000,500)
        self.setWindowTitle("example program")
        self.setWindowIcon(QIcon("web.jpg"))
        self.designLayout()
        self.show()
        
    def designLayout(self):
        #layout
        main_vboxlayout = QVBoxLayout()
        mid_hboxlayout = QHBoxLayout()
        right_layout = QVBoxLayout()
        speed_label = QLabel("denemeeeee")
        widget2 = QFrame()
        widget3 = QFrame()
        #style
        speed_label.setStyleSheet("background-color: rgb(0, 0, 255);color: rgb(255,0,0);")
        widget2.setStyleSheet("background-color: rgb(255, 0, 0)")
        widget3.setStyleSheet("background-color: rgb(255, 255, 0)")
        #add
        right_layout.addWidget(speed_label)
        right_layout.addWidget(QPushButton("deneme"))
        mid_hboxlayout.addWidget(widget2,7)
        mid_hboxlayout.addLayout(right_layout,3)
        main_vboxlayout.addLayout(mid_hboxlayout,15)
        main_vboxlayout.addWidget(widget3,5)
        self.setLayout(main_vboxlayout)

app = QApplication(sys.argv)
window = Window()

sys.exit(app.exec_())
