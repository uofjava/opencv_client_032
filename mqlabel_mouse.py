import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QEvent, QPoint, Signal, SignalInstance
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import * 


class MQlabelMouse(QLabel):
    mouseFinshSignal = Signal(int,int,int,int)
    def __init__(self, parent=None):
        super(MQlabelMouse, self).__init__(parent)
        self.leftPoint = (0,0)
        self.rightPoint = (0,0)
        self.setFixedSize(640,480)

    def mousePressEvent(self, event):
        #鼠标左键按下
        if event.button() == Qt.LeftButton:
            print("鼠标左键按下x:",event.x(),"，y:",event.y())
            self.leftPoint = (event.x(),event.y())
    def mouseReleaseEvent(self, event):
        #鼠标左键释放
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            print("鼠标左键释放x:", event.x(), "，y:", event.y())
            self.rightPoint = (event.x(),event.y())
            self.mouseFinshSignal.emit(self.leftPoint[0],self.leftPoint[1],self.rightPoint[0],self.rightPoint[1])
    def mouseMoveEvent(self, event):
        #鼠标左键按下的同时移动鼠标
        if event.buttons() and Qt.LeftButton:
           self.endPoint = event.pos()
           print("鼠标左键按下的同时移动鼠标x:", event.x(), "，y:", event.y())