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
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QColor
from mqlist import MListItem
from savetool import SaveDataTool
import json

class QItemData():
    def __init__(self,name,info):
        self.name = name
        self.info = info
class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.cap = cv2.VideoCapture(0)
        self.frame_timer =  QTimer(self)
        self.frame_timer.timeout.connect(self.getFrame)
        self.save_tool = SaveDataTool('./save.txt')
        self.initPrame()
        self.load_ui()
        self.parame_change()
        self.listInit()

    def parame_change(self):
        self.ui.info_left_x.setValue(self.infoLeftX)
        self.ui.info_left_y.setValue(self.infoLeftY)
        self.ui.info_right_x.setValue(self.infoRightX)
        self.ui.info_right_y.setValue(self.infoRightY)

        self.ui.info_max_rad.setValue(self.infoMaxRad)
        self.ui.info_min_rad.setValue(self.infoMinRad)


        self.ui.canny_add_blue.setChecked(self.cannyAddBlue)

        self.ui.mindel_x.setValue(self.blueValue)
        self.ui.mindel_y.setValue(self.blueYValue)
        self.ui.canny_min.setValue(self.cannyMin)
        self.ui.canny_max.setValue(self.cannyMax)
        
    # 初始化产品配置参数
    def listInit(self):
        rows = 30
        cols = 2
        self.m_model = QStandardItemModel(rows,cols)
        self.m_model.setHorizontalHeaderLabels(["名称","信息"])
        self.m_model.itemChanged.connect(self.itemChanged)
        self.ui.tableView.clicked.connect(self.tabletViewClicked)
        self.ui.tableView.setModel(self.m_model)
        delegate = MListItem()    
        self.ui.tableView.setItemDelegateForColumn(2, delegate)
        self.ui.tableView.setColumnWidth(0, 100)
        self.ui.tableView.setColumnWidth(1, 300)
        #加载配置文件 
        listDatga = self.save_tool.load_data()
        for row in range(rows):
            itemd = listDatga[row]
            print("创建数据",row)
            index = self.m_model.index(row,0)
            self.m_model.setData(index,itemd['name'])
            print("创建数据",index.row(),index.column(),index.data())
            index = self.m_model.index(row,1)
            self.m_model.setData(index,itemd['info'])
            print("创建数据",index.row(),index.column(),index.data())
    # 默认参数
    def initPrame(self):
        self.canny_open = False
        self.gray_open = False
        self.contout_open = False
        self.isRadius = True
        self.isLinght = True

        self.handler_row = 0

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
        self.ui = loader.load(ui_file,self)
        self.ui.open_camera.clicked.connect(lambda:self.contol_camera("open"))
        self.ui.open_canny.clicked.connect(lambda:self.contol_camera("open_canny"))
        self.ui.open_gray.clicked.connect(lambda:self.contol_camera("open_gray"))
        self.ui.open_coutour.clicked.connect(lambda:self.contol_camera("open_coutour"))
        
        # 将配置参数写入文件
        self.ui.save.clicked.connect(lambda:self.contol_camera("save"))
        # 更新参数
        self.ui.save_params.clicked.connect(lambda:self.contol_camera("save_params"))

        self.ui.info_left_x.valueChanged.connect(self.infoLeftXChanged)
        self.ui.info_left_y.valueChanged.connect(self.infoLeftYChanged)
        self.ui.info_right_x.valueChanged.connect(self.infoRightXChanged)
        self.ui.info_right_y.valueChanged.connect(self.infoRightYChanged)

        self.ui.info_min_rad.valueChanged.connect(self.infoMinRadChanged)
        self.ui.info_max_rad.valueChanged.connect(self.infoMaxRadChanged)

        self.ui.info_min_vx.valueChanged.connect(self.infoMinVXChanged)
        self.ui.info_max_vx.valueChanged.connect(self.infoMaXVXChanged)
        self.ui.info_lingths.valueChanged.connect(self.linghtsValueChanged)

        # 均值x
        self.ui.mindel_x.valueChanged.connect(self.blueXValueChanged)
        # 均值y
        self.ui.mindel_y.valueChanged.connect(self.blueYValueChanged)
        # 轮廓参数最小
        self.ui.canny_min.valueChanged.connect(self.cannyMinChanged)
        # 轮廓参数最大
        self.ui.canny_max.valueChanged.connect(self.cannyMaxChanged)
        # 轮廓提取是否添加均值滤波
        self.ui.canny_add_blue.stateChanged.connect(self.cannyAddBlueState)

        # 鼠标框选轮廓
        self.ui.groupBox.mouse = MQlabelMouse(self.ui)
        self.ui.groupBox.mouse.mouseFinshSignal.connect(self.mouseHander)


        self.ui.groupBox.mouse.setGeometry(200,70,640,480)


        ui_file.close()


    '''
    鼠标框选区域，返回
    ''' 
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
    # 左上角X
    def infoLeftXChanged(self,newvalue):
        self.infoLeftX = newvalue        
    # 左上角Y
    def infoLeftYChanged(self,newvalue):
        self.infoLeftY = newvalue
    # 右下角
    def infoRightXChanged(self,newvalue):
        self.infoRightX = newvalue
    # 右下角
    def infoRightYChanged(self,newvalue):
        self.infoRightY = newvalue

    # 圆半径最小值
    def infoMinRadChanged(self,newvalue):
        self.infoMinRad = newvalue
    # 圆半径最大
    def infoMaxRadChanged(self,newvalue):
        self.infoMaxRad = newvalue
    # 轮廓最小点数
    def linghtsValueChanged(self,newvalue):
        self.infolinghts = newvalue

    # 线最小角度
    def infoMinVXChanged(self,newvalue):
        self.infoMinVX = newvalue
        print("infoMinVX",newvalue)
    # 线最大角度
    def infoMaXVXChanged(self,newvalue):
        self.infoMaxVX = newvalue
        print("infoMaxVX",newvalue)

    def blueXValueChanged(self,newvalue):
        self.blueValue = newvalue

    def blueYValueChanged(self,newvalue):
        self.blueYValue = newvalue
    
    # cannY 最小值
    def cannyMinChanged(self,newvalue):
        self.cannyMin = newvalue
    # canny 最大值
    def cannyMaxChanged(self,newvalue):
        self.cannyMax = newvalue         
    # 是否添加
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
        if str == "save":
            with open("save.txt","w",encoding='utf-8') as f:
                listData = []
                for i in range(self.m_model.rowCount()):
                    print(self.m_model.itemData(self.m_model.index(i,0))[0])
                    print(self.m_model.itemData(self.m_model.index(i,1))[0])  
                    itemD = {"name":self.m_model.itemData(self.m_model.index(i,0))[0],"info":self.m_model.itemData(self.m_model.index(i,1))[0]}  
                    listData.append(itemD)
                self.save_tool.save_data(listData) 
        if str == "save_params":
            # 将当前配置参数保存到配置表
            params_info = {
                "blue_x":self.blueValue,
                "blue_y":self.blueYValue,
                "canny_min":self.cannyMin,
                "canny_max":self.cannyMax,
                "canny_add_blue":self.cannyAddBlue,
                "info_left_x":self.infoLeftX,
                "info_left_y":self.infoLeftY,
                "info_right_x":self.infoRightX,
                "info_right_y":self.infoRightY,
                "info_min_rad":self.infoMinRad,
                "info_max_rad":self.infoMaxRad,
                "info_min_vx":self.infoMinVX,
                "info_max_vx":self.infoMaxVX,
                "info_linghts":self.infolinghts
            }
            str_d =json.dumps(params_info)
            print(str_d)
            index =  self.m_model.index(self.handler_row,1) 
            self.m_model.setData(index,str_d)
    # 列表内容更改
    def itemChanged(self,index):
        print(index.row(),index.column(),index.data())
    # 选中列表某一项
    def tabletViewClicked(self,index):
        print("tabletViewClicked:",index.row(),index.column(),index.data())
        self.handler_row = index.row()
        index = self.m_model.index(self.handler_row,1)
        params_info = json.loads(index.data())
        self.blueValue = params_info["blue_x"]
        self.blueYValue = params_info["blue_y"]
        self.cannyMin = params_info["canny_min"]
        self.cannyMax = params_info["canny_max"]
        self.cannyAddBlue = params_info["canny_add_blue"]
        self.infoLeftX = params_info["info_left_x"]
        self.infoLeftY = params_info["info_left_y"]
        self.infoRightX = params_info["info_right_x"]
        self.infoRightY = params_info["info_right_y"]
        self.infoMinRad = params_info["info_min_rad"]
        self.infoMaxRad = params_info["info_max_rad"]
        self.infoMinVX = params_info["info_min_vx"]
        self.infoMaxVX = params_info["info_max_vx"]
        self.infolinghts = params_info["info_linghts"]

        self.parame_change()
    # 获取摄像头数据
    def getFrame(self):
        ret, self.frame = self.cap.read()    
        if ret:
           info_frame = self.frame.copy() 
           cv2.rectangle(info_frame,(self.infoLeftX,self.infoLeftY),(self.infoRightX,self.infoRightY),(0,200,0),1)
           self.ui.groupBox.mouse.setPixmap(QPixmap.fromImage(QImage(info_frame.data, info_frame.shape[1],info_frame.shape[0], QImage.Format_RGB888)))
           if self.gray_open :
            # 均值滤波
              self.gray = cv2.blur(self.frame.copy(),(self.blueValue,self.blueYValue))
              self.ui.img_2.setPixmap(QPixmap.fromImage(QImage(self.gray.data, self.gray.shape[1],self.gray.shape[0], QImage.Format_RGB888))) 
           if self.canny_open and (self.frame is not None):
              canny = None
            #   canny 边缘检测：是否经过均值滤波
              if self.cannyAddBlue and (self.gray is not None):
                 canny = self.gray.copy()
              else:
                canny = self.frame.copy()
              self.canny = cv2.Canny(canny, self.cannyMin, self.cannyMax)
              canny =  cv2.cvtColor(self.canny,cv2.COLOR_GRAY2RGB)
              self.ui.img_3.setPixmap(QPixmap.fromImage(QImage(canny.data, canny.shape[1],canny.shape[0], QImage.Format_RGB888)))   
           if self.contout_open and (self.canny is not None):
                contout =  self.canny.copy()
                self.contours, hierachy =  cv2.findContours(contout,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                contout =  cv2.cvtColor(contout,cv2.COLOR_GRAY2RGB)
                for cnt in self.contours :
                    # 圆孔拟合（半径，中心）
                    if self.isRadius:
                        (x,y),radius = cv2.minEnclosingCircle(cnt)    
                        center = (int(x),int(y))
                        radius = int(radius)
                        if x < self.infoRightX and y < self.infoRightY  and x > self.infoLeftX and  y > self.infoLeftY and radius > self.infoMinRad and radius < self.infoMaxRad :
                            cv2.circle(contout,center,radius,(0,255,255),2)
                            self.radiusok = True
                    # 线拟合（角度，特征点数） 
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
                # 圆孔，直线检测通过则输出OK,圆桶定位完成
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
