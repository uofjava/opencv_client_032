# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGroupBox,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpinBox, QStatusBar, QTableView, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(1954, 1080)
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.open_camera = QPushButton(self.centralwidget)
        self.open_camera.setObjectName(u"open_camera")
        self.open_camera.setGeometry(QRect(10, 10, 75, 23))
        self.open_gray = QPushButton(self.centralwidget)
        self.open_gray.setObjectName(u"open_gray")
        self.open_gray.setGeometry(QRect(180, 10, 81, 21))
        self.open_canny = QPushButton(self.centralwidget)
        self.open_canny.setObjectName(u"open_canny")
        self.open_canny.setGeometry(QRect(90, 10, 81, 21))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QRect(200, 50, 1280, 960))
        self.img_1 = QLabel(self.groupBox)
        self.img_1.setObjectName(u"img_1")
        self.img_1.setGeometry(QRect(0, 0, 640, 480))
        self.img_2 = QLabel(self.groupBox)
        self.img_2.setObjectName(u"img_2")
        self.img_2.setGeometry(QRect(640, 0, 640, 480))
        self.img_3 = QLabel(self.groupBox)
        self.img_3.setObjectName(u"img_3")
        self.img_3.setGeometry(QRect(0, 480, 640, 480))
        self.img_4 = QLabel(self.groupBox)
        self.img_4.setObjectName(u"img_4")
        self.img_4.setGeometry(QRect(640, 480, 640, 480))
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 50, 181, 191))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.mindel_x = QSpinBox(self.formLayoutWidget)
        self.mindel_x.setObjectName(u"mindel_x")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.mindel_x)

        self.label_9 = QLabel(self.formLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.mindel_y = QSpinBox(self.formLayoutWidget)
        self.mindel_y.setObjectName(u"mindel_y")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.mindel_y)

        self.label_10 = QLabel(self.formLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_10)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.canny_min = QSpinBox(self.formLayoutWidget)
        self.canny_min.setObjectName(u"canny_min")
        self.canny_min.setMaximum(255)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.canny_min)

        self.canny_max = QSpinBox(self.formLayoutWidget)
        self.canny_max.setObjectName(u"canny_max")
        self.canny_max.setMaximum(255)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.canny_max)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.label_18 = QLabel(self.formLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_18)

        self.canny_add_blue = QCheckBox(self.formLayoutWidget)
        self.canny_add_blue.setObjectName(u"canny_add_blue")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.canny_add_blue)

        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(1500, 60, 401, 248))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.info_left_x = QSlider(self.formLayoutWidget_2)
        self.info_left_x.setObjectName(u"info_left_x")
        self.info_left_x.setMaximum(640)
        self.info_left_x.setOrientation(Qt.Horizontal)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.info_left_x)

        self.label_5 = QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.info_left_y = QSlider(self.formLayoutWidget_2)
        self.info_left_y.setObjectName(u"info_left_y")
        self.info_left_y.setMaximum(480)
        self.info_left_y.setOrientation(Qt.Horizontal)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.info_left_y)

        self.label_6 = QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.info_right_x = QSlider(self.formLayoutWidget_2)
        self.info_right_x.setObjectName(u"info_right_x")
        self.info_right_x.setMaximum(640)
        self.info_right_x.setOrientation(Qt.Horizontal)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.info_right_x)

        self.label_7 = QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.info_right_y = QSlider(self.formLayoutWidget_2)
        self.info_right_y.setObjectName(u"info_right_y")
        self.info_right_y.setMaximum(480)
        self.info_right_y.setOrientation(Qt.Horizontal)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.info_right_y)

        self.label_19 = QLabel(self.formLayoutWidget_2)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_19)

        self.info_min_rad = QSlider(self.formLayoutWidget_2)
        self.info_min_rad.setObjectName(u"info_min_rad")
        self.info_min_rad.setMaximum(1000)
        self.info_min_rad.setPageStep(1)
        self.info_min_rad.setOrientation(Qt.Horizontal)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.info_min_rad)

        self.label_21 = QLabel(self.formLayoutWidget_2)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_21)

        self.label_22 = QLabel(self.formLayoutWidget_2)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label_22)

        self.label_20 = QLabel(self.formLayoutWidget_2)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.label_20)

        self.info_max_rad = QSlider(self.formLayoutWidget_2)
        self.info_max_rad.setObjectName(u"info_max_rad")
        self.info_max_rad.setMaximum(1000)
        self.info_max_rad.setPageStep(1)
        self.info_max_rad.setOrientation(Qt.Horizontal)

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.info_max_rad)

        self.info_max_vx = QSlider(self.formLayoutWidget_2)
        self.info_max_vx.setObjectName(u"info_max_vx")
        self.info_max_vx.setMaximum(1000)
        self.info_max_vx.setPageStep(1)
        self.info_max_vx.setOrientation(Qt.Horizontal)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.info_max_vx)

        self.info_min_vx = QSlider(self.formLayoutWidget_2)
        self.info_min_vx.setObjectName(u"info_min_vx")
        self.info_min_vx.setMaximum(1000)
        self.info_min_vx.setPageStep(1)
        self.info_min_vx.setOrientation(Qt.Horizontal)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.info_min_vx)

        self.label_23 = QLabel(self.formLayoutWidget_2)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.label_23)

        self.info_lingths = QSlider(self.formLayoutWidget_2)
        self.info_lingths.setObjectName(u"info_lingths")
        self.info_lingths.setMaximum(1000)
        self.info_lingths.setOrientation(Qt.Horizontal)

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.info_lingths)

        self.open_coutour = QPushButton(self.centralwidget)
        self.open_coutour.setObjectName(u"open_coutour")
        self.open_coutour.setGeometry(QRect(270, 10, 75, 23))
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(1500, 310, 401, 621))
        self.save = QPushButton(self.centralwidget)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(1500, 930, 75, 23))
        self.save_2 = QPushButton(self.centralwidget)
        self.save_2.setObjectName(u"save_2")
        self.save_2.setGeometry(QRect(1820, 930, 75, 23))
        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1954, 21))
        self.menu032 = QMenu(self.menubar)
        self.menu032.setObjectName(u"menu032")
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu032.menuAction())

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.open_camera.setText(QCoreApplication.translate("main", u"\u6253\u5f00\u6444\u50cf\u5934", None))
        self.open_gray.setText(QCoreApplication.translate("main", u"\u6253\u5f00\u7070\u5ea6\u56fe\u50cf", None))
        self.open_canny.setText(QCoreApplication.translate("main", u"\u6253\u5f00\u8fb9\u7f18\u68c0\u6d4b", None))
        self.groupBox.setTitle(QCoreApplication.translate("main", u"GroupBox", None))
        self.img_1.setText(QCoreApplication.translate("main", u"TextLabel", None))
        self.img_2.setText(QCoreApplication.translate("main", u"TextLabel", None))
        self.img_3.setText(QCoreApplication.translate("main", u"TextLabel", None))
        self.img_4.setText(QCoreApplication.translate("main", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("main", u"\u5747\u503cx", None))
        self.label_9.setText(QCoreApplication.translate("main", u"\u5747\u503cy", None))
        self.label_10.setText("")
        self.label_2.setText(QCoreApplication.translate("main", u"canny_min", None))
        self.label_3.setText(QCoreApplication.translate("main", u"canny_max", None))
        self.label_18.setText(QCoreApplication.translate("main", u"cannay", None))
        self.canny_add_blue.setText(QCoreApplication.translate("main", u"\u53bb\u566a", None))
        self.label_4.setText(QCoreApplication.translate("main", u"left_x", None))
        self.label_5.setText(QCoreApplication.translate("main", u"left_y", None))
        self.label_6.setText(QCoreApplication.translate("main", u"right_x", None))
        self.label_7.setText(QCoreApplication.translate("main", u"right_y", None))
        self.label_19.setText(QCoreApplication.translate("main", u"min_rad", None))
        self.label_21.setText(QCoreApplication.translate("main", u"min_VX", None))
        self.label_22.setText(QCoreApplication.translate("main", u"max_VX", None))
        self.label_20.setText(QCoreApplication.translate("main", u"max_rad", None))
        self.label_23.setText(QCoreApplication.translate("main", u"\u7ebf\u70b9\u6570", None))
        self.open_coutour.setText(QCoreApplication.translate("main", u"\u6253\u5f00\u8f6e\u5ed3\u68c0\u6d4b", None))
        self.save.setText(QCoreApplication.translate("main", u"\u5199\u5165\u6587\u4ef6", None))
        self.save_2.setText(QCoreApplication.translate("main", u"\u5199\u5165\u6587\u4ef6", None))
        self.menu032.setTitle(QCoreApplication.translate("main", u"032\u89c6\u89c9", None))
    # retranslateUi

