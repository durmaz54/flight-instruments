import io
from os import close
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import folium
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(250,150,1200,800)
        self.setWindowTitle("Flight Instruments")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.setStyleSheet(open("style.qss","r").read())
        self.designLayout()
        self.show()
        
    def designLayout(self):
        #layout
        main_vboxlayout = QVBoxLayout()
        mid_hboxlayout = QHBoxLayout()
        mid_hboxlayout.setObjectName("mid_hboxlayout")
        right_layout = QGridLayout()
        
        #widget
        speed_label = QLabel("bar")
        speed_label.setObjectName("speed_label")
        a_label = QLabel("a instrument")
        b_label = QLabel("b instrument")
        c_label = QLabel("c instrument")
        d_label = QLabel("d instrument")
        e_label = QLabel("bar")
        #---------slopebar-------------
        self.slope_bar_value = 35
        self.slopeleft_bar = QProgressBar()
        self.slopeleft_bar.setOrientation(Qt.Vertical)
        self.slopeleft_bar.setValue(self.slope_bar_value)
        self.slopeleft_bar.setObjectName("slope_bar")
        self.slopeleft_bar.setFormat("Slope")
        self.sloperight_bar = QProgressBar()
        self.sloperight_bar.setOrientation(Qt.Vertical)
        self.sloperight_bar.setValue(abs((self.slope_bar_value)-100))
        self.sloperight_bar.setObjectName("slope_bar")
        self.sloperight_bar.setFormat("Slope")
        #-----------slopebar--------------
        widget2 = QFrame()
        widget2.setObjectName("widget2")
        bottom_frame = QFrame()
        bottom_frame.setObjectName("bottom_frame")

        #---------------------------ADD-------------------------
        #right layout
        right_layout.addWidget(self.slopeleft_bar,0,0,10,1) # (y,x)
        right_layout.addWidget(a_label,0,1,5,4)
        right_layout.addWidget(b_label,0,5,5,4)
        right_layout.addWidget(c_label,5,1,5,4)
        right_layout.addWidget(d_label,5,5,5,4)
        right_layout.addWidget(self.sloperight_bar,0,10,10,1)
        #-----------
        mid_hboxlayout.addWidget(self.googleMapWidget(),7)
        mid_hboxlayout.addLayout(right_layout,3)
        main_vboxlayout.addLayout(mid_hboxlayout,15)
        main_vboxlayout.addWidget(bottom_frame,5)
        self.setLayout(main_vboxlayout)
    
    
    def googleMapWidget(self):
        m = folium.Map(location=[41.092628, 30.572079],zoom_start=15)
        self.map_data = io.BytesIO()
        m.save(self.map_data, close_file=False)
        map_webengine = QWebEngineView()
        map_webengine.setHtml(self.map_data.getvalue().decode())

        return map_webengine

        

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            if self.slope_bar_value >= 100:
                self.slope_bar_value = 0
            self.slope_bar_value += 5
            self.slopeleft_bar.setValue(self.slope_bar_value)
            self.sloperight_bar.setValue(abs((self.slope_bar_value)-100))
            print(self.slope_bar_value)

app = QApplication(sys.argv)
window = Window()

sys.exit(app.exec_())
