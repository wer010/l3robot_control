from PyQt5.QtCore import Qt,QRect,pyqtSignal,QCoreApplication
from PyQt5.QtWidgets import QMainWindow,QLineEdit,QSlider,QGroupBox,QPushButton, QFileDialog, QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QLabel
from PyQt5.QtGui import QDoubleValidator,QImage, QPixmap, QPainter, QPen
import ui

class MyLabel(QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False
    pressed = pyqtSignal(int,int)
    released = pyqtSignal(int,int)
    #鼠标点击事件
    def mousePressEvent(self, event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()
        self.pressed.emit(event.x(),event.y())

    #鼠标释放事件
    def mouseReleaseEvent(self, event):
        self.flag = False
        self.released.emit(event.x(),event.y())

    #鼠标移动事件
    def mouseMoveEvent(self, event):
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()
    #绘制事件
    def paintEvent(self, event):
        super().paintEvent(event)
        rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
        painter.drawRect(rect)




class mywindow(QMainWindow, ui.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #



    # def loadFile(self):
    #     file_name,_ = QFileDialog.getOpenFileName(self,'打开文件',"D:\\","Image files(*.jpg *.gif)")
    #     s = self.bb_area.size()
    #     self.image = QPixmap(file_name)
    #     os = self.image.size()
    #     ri = self.image.scaled(s, Qt.KeepAspectRatio, Qt.FastTransformation)
    #     rs = ri.size()
    #     self.r = max(rs.width()/os.width(), rs.height()/os.height())
    #     self.bb_area.setPixmap(ri)
    #
    # def mousedown(self,x,y):
    #     self.x0 = round(x/self.r)
    #     self.y0 = round(y/self.r)
    #
    # def mouseup(self,x,y):
    #     self.x1 = round(x/self.r)
    #     self.y1 = round(y/self.r)
    #     # self.b4.setText('x0:{},y0:{},x1:{},y1:{}'.format(self.x0, self.y0, self.x1, self.y1))
    #     self.roi = self.image.copy(self.x0,self.y0,self.x1-self.x0,self.y1-self.y0)
    #     self.b5.setPixmap(self.roi.scaled(self.b5.size(),Qt.KeepAspectRatio, Qt.FastTransformation))
