import sys, io
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import random


temp = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>500</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>540</y>
     <width>141</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>pushButton</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        f = io.StringIO(temp)
        uic.loadUi(f, self)

        self.scene = QtWidgets.QGraphicsScene()
        self.view = QtWidgets.QGraphicsView(self)
        self.view.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.view.setScene(self.scene)
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        self.scene.clear()
        d = random.randint(10, 400)
        n1, n2, n3 = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.circle = QtWidgets.QGraphicsEllipseItem(-d / 2, -d / 2, d, d)
        self.circle.setBrush(QtGui.QColor(n1, n2, n3))
        self.scene.addItem(self.circle)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())