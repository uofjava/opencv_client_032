from ctypes import Union
import PySide6
from PySide6.QtGui import * 
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter

class MListItem(QStyledItemDelegate):
    # onClick = Signal(int)
    def __init__(self, parent=None):
        super().__init__(parent)
        # # 名称
        # self.lintText = QLineEdit()
        # # 提示信息
        # self.infoText = QLabel()
        # # 清除
        # self.cleanBtn = QPushButton()
    def setEditorData(self, editor, index):
        print("setEditorData",editor,index)

    # def setModelData(self, editor, model, index) -> None:
    #     print("setModelData",editor,model,index)
    #     return super().setModelData(editor, model, index)

    # def updateEditorGeometry(self, editor, option, index) -> None:
    #     print("updateEditorGeometry",editor,option,index)
    #     return super().updateEditorGeometry(editor, option, index) 

       
    def paint(self, painter: PySide6.QtGui.QPainter, option: PySide6.QtWidgets.QStyleOptionViewItem, index: QModelIndex) -> None:
        # print("option:",option)
        print("index:",index.row(),index.column(),index.data())
        # self.cleanBtn.setText("擦除")

