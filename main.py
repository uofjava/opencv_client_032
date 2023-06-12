# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import cv2
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QTimer, Slot
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import *

from mqlabel_mouse import MQlabelMouse



class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.cap = cv2.VideoCapture(0)
        self.frame_timer =  QTimer(self)
        self.frame_timer.timeout.connect(self.getFrame)
        self.initPrame()
        self.load_ui()
    def initPrame(self):
        self.canny_open = False
        self.gray_open = False
        self.contout_open = False
        self.isRadius = True
        self.isLinght = True
        self.infoLeftX = 0
        self.infoLeftY = 0
        self.infoRightX = 0
        self.infoRightY = 0
        self.infoMaxRad = 10
        self.infoMinRad = 5

        self.infoMinVX =730
        self.infoMaxVX = 750

        self.linghtok =False
        self.radiusok = False

        self.blueValue = 1
        self.blueYValue = 1
        self.cannyMin = 100
        self.cannyMax = 100
        self.cannyAddBlue = False
        self.frame = None
        self.gray = None
        self.canny = None
        self.infolinghts = 10

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        # print(path)
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        self.ui.open_camera.clicked.connect(lambda:self.contol_camera("open"))
        self.ui.open_canny.clicked.connect(lambda:self.contol_camera("open_canny"))
        self.ui.open_gray.clicked.connect(lambda:self.contol_camera("open_gray"))
        self.ui.open_coutour.clicked.connect(lambda:self.contol_camera("open_coutour"))
        
        self.ui.info_left_x.valueChanged.connect(self.infoLeftXChanged)
        self.ui.info_left_y.valueChanged.connect(self.infoLeftYChanged)
        self.ui.info_right_x.valueChanged.connect(self.infoRightXChanged)
        self.ui.info_right_y.valueChanged.connect(self.infoRightYChanged)

        self.ui.info_min_rad.valueChanged.connect(self.infoMinRadChanged)
        self.ui.info_max_rad.valueChanged.connect(self.infoMaxRadChanged)

        self.ui.info_min_vx.valueChanged.connect(self.infoMinVXChanged)
        self.ui.info_max_vx.valueChanged.connect(self.infoMaXVXChanged)



        self.ui.mindel_x.valueChanged.connect(self.blueXValueChanged)
        self.ui.mindel_y.valueChanged.connect(self.blueYValueChanged)
        self.ui.info_lingths.valueChanged.connect(self.linghtsValueChanged)
        self.ui.canny_min.valueChanged.connect(self.cannyMinChanged)
        self.ui.canny_max.valueChanged.connect(self.cannyMaxChanged)
        self.ui.canny_add_blue.stateChanged.connect(self.cannyAddBlueState)

        self.ui.groupBox.mouse = MQlabelMouse(self.ui)
        self.ui.groupBox.mouse.mouseFinshSignal.connect(self.mouseHander)


        self.ui.groupBox.mouse.setGeometry(200,50,640,480)


        ui_file.close()
    @Slot(str) 
    def mouseHander(self,left_x,left_y,right_x,right_y):
        print("left_x:",left_x, ",left_y:", left_y, "right_x:", right_x, "right_y:", right_y)
        self.infoLeftX = left_x
        self.infoLeftY = left_y
        self.infoRightX = right_x
        self.infoRightY = right_y
        self.ui.info_left_x.setValue(left_x)
        self.ui.info_left_y.setValue(left_y)
        self.ui.info_right_x.setValue(right_x)
        self.ui.info_right_y.setValue(right_y)

    def infoLeftXChanged(self,newvalue):
        self.infoLeftX = newvalue        
    def infoLeftYChanged(self,newvalue):
        self.infoLeftY = newvalue
    def infoRightXChanged(self,newvalue):
        self.infoRightX = newvalue
    def infoRightYChanged(self,newvalue):
        self.infoRightY = newvalue

    def infoMinRadChanged(self,newvalue):
        self.infoMinRad = newvalue
    def infoMaxRadChanged(self,newvalue):
        self.infoMaxRad = newvalue

    def linghtsValueChanged(self,newvalue):
        self.infolinghts = newvalue

    def infoMinVXChanged(self,newvalue):
        self.infoMinVX = newvalue
        print("infoMinVX",newvalue)
    def infoMaXVXChanged(self,newvalue):
        self.infoMaxVX = newvalue
        print("infoMaxVX",newvalue)

    def blueXValueChanged(self,newvalue):
        self.blueValue = newvalue

    def blueYValueChanged(self,newvalue):
        self.blueYValue = newvalue
    

    def cannyMinChanged(self,newvalue):
        self.cannyMin = newvalue
    def cannyMaxChanged(self,newvalue):
        self.cannyMax = newvalue         

    def cannyAddBlueState(self,value):
        print(value)
        if value == 2:
            self.cannyAddBlue = True
        else:
            self.cannyAddBlue = False

    def contol_camera(self,str):
        print("打开摄像头",str)
        if str == "open":
            self.frame_timer.start(35)
        if str == "close":
            self.canny_open = False
            self.gray_open = False
            self.contout_open = False
            self.frame_timer.stop()
        if str == "open_gray":
            self.gray_open = True
        if str == "open_canny":
            self.canny_open = True   
        if str == "open_coutour":
            self.contout_open = True            
    
    def getFrame(self):
        ret, self.frame = self.cap.read()    
        if ret:
           info_frame = self.frame.copy() 
           cv2.rectangle(info_frame,(self.infoLeftX,self.infoLeftY),(self.infoRightX,self.infoRightY),(0,200,0),1)
           
           self.ui.groupBox.mouse.setPixmap(QPixmap.fromImage(QImage(info_frame.data, info_frame.shape[1],info_frame.shape[0], QImage.Format_RGB888)))
           
        #    self.ui.img_1.setPixmap(QPixmap.fromImage(QImage(info_frame.data, info_frame.shape[1],info_frame.shape[0], QImage.Format_RGB888))) 
           if self.gray_open :
              self.gray = cv2.blur(self.frame.copy(),(self.blueValue,self.blueYValue))
              
              self.ui.img_2.setPixmap(QPixmap.fromImage(QImage(self.gray.data, self.gray.shape[1],self.gray.shape[0], QImage.Format_RGB888))) 
           if self.canny_open and (self.frame is not None):
              canny = None
              if self.cannyAddBlue and (self.gray is not None):
                 canny = self.gray.copy()
              else:
                canny = self.frame.copy()
              self.canny = cv2.Canny(canny, self.cannyMin, self.cannyMax)
              canny =  cv2.cvtColor(self.canny,cv2.COLOR_GRAY2RGB)
            #   if canny:  
              self.ui.img_3.setPixmap(QPixmap.fromImage(QImage(canny.data, canny.shape[1],canny.shape[0], QImage.Format_RGB888)))   
           if self.contout_open and (self.canny is not None):
                contout =  self.canny.copy()
                self.contours, hierachy =  cv2.findContours(contout,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                contout =  cv2.cvtColor(contout,cv2.COLOR_GRAY2RGB)
                # cv2.drawContours(contout,self.contours, -1, (0,255,1),2)
                
                for cnt in self.contours :
                    if self.isRadius:
                        (x,y),radius = cv2.minEnclosingCircle(cnt)    
                        center = (int(x),int(y))
                        radius = int(radius)
                        if x < self.infoRightX and y < self.infoRightY  and x > self.infoLeftX and  y > self.infoLeftY and radius > self.infoMinRad and radius < self.infoMaxRad :
                            cv2.circle(contout,center,radius,(0,255,255),2)
                            self.radiusok = True
                    if self.isLinght and cnt.size > self.infolinghts:
                        rows,cols = contout.shape[:2]
                        [vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
                        lefty = int((-x*vy/vx) + y)
                        righty = int(((cols-x)*vy/vx)+y)
                        # print(vx)
                        if vx < self.infoMaxVX /1000  and vx > self.infoMinVX / 1000 and vy < 0:
                            print(cnt.size)
                            cv2.line(contout,(cols-1,righty),(0,lefty),(0,255,0),2)
                            self.linghtok = True
                            for p in cnt:
                                # print(p)
                                cv2.circle(contout,(p[0][0],p[0][1]),1,(255,0,0),1)

                if self.linghtok and self.radiusok:
                    print("ok")
                    self.linghtok =False
                    self.radiusok = False
                self.ui.img_4.setPixmap(QPixmap.fromImage(QImage(contout.data, contout.shape[1],contout.shape[0], QImage.Format_RGB888)))   
        

if __name__ == "__main__":
    app = QApplication([])
    widget = main()
    widget.ui.show()
    sys.exit(app.exec_())
