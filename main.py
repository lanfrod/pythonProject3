import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import random


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("UI.ui", self)

        self.scene = QtWidgets.QGraphicsScene()
        self.view = QtWidgets.QGraphicsView(self)
        self.view.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.view.setScene(self.scene)
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        self.scene.clear()
        diameter = random.randint(10, 400)
        self.circle = QtWidgets.QGraphicsEllipseItem(-diameter / 2, -diameter / 2, diameter, diameter)
        self.circle.setBrush(QtGui.QColor(255, 255, 0))
        self.scene.addItem(self.circle)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())