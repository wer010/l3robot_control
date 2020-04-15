# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lanhai/Projects/l3robot_control/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QRect,pyqtSignal,QCoreApplication
from PyQt5.QtWidgets import QMessageBox,QTableWidgetItem,QMainWindow,QLineEdit,QSlider,QGroupBox,QPushButton, QFileDialog, QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QLabel
import excel_read
import cmd_send
import queue

class Ui_Dialog(object):
    q = queue.Queue(0)

    def setupUi(self, Dialog):
        self.isPause = False
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        mainwindow = QtWidgets.QWidget()
        Dialog.setCentralWidget(mainwindow)
        self.horizontalLayout = QtWidgets.QHBoxLayout(mainwindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Groupbox = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Groupbox.sizePolicy().hasHeightForWidth())
        self.Groupbox.setSizePolicy(sizePolicy)
        self.Groupbox.setObjectName("Groupbox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Groupbox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_loadA = QtWidgets.QPushButton(self.Groupbox)
        self.pushButton_loadA.setObjectName("pushButton_loadA")
        self.verticalLayout_4.addWidget(self.pushButton_loadA)
        self.pushButton_loadB = QtWidgets.QPushButton(self.Groupbox)
        self.pushButton_loadB.setObjectName("pushButton_loadB")
        self.verticalLayout_4.addWidget(self.pushButton_loadB)
        self.pushButton_connect = QtWidgets.QPushButton(self.Groupbox)
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.verticalLayout_4.addWidget(self.pushButton_connect)
        self.pushButton_start = QtWidgets.QPushButton(self.Groupbox)
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout_4.addWidget(self.pushButton_start)
        self.pushButton_pause = QtWidgets.QPushButton(self.Groupbox)
        self.pushButton_pause.setObjectName("pushButton_pause")
        self.verticalLayout_4.addWidget(self.pushButton_pause)
        self.pushButton_exit = QtWidgets.QPushButton(self.Groupbox)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.verticalLayout_4.addWidget(self.pushButton_exit)
        self.verticalLayout_3.addWidget(self.Groupbox)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_ipaddress = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ipaddress.sizePolicy().hasHeightForWidth())
        self.lineEdit_ipaddress.setSizePolicy(sizePolicy)
        self.lineEdit_ipaddress.setObjectName("lineEdit_ipaddress")
        self.lineEdit_ipaddress.setText("127.0.0.1")
        self.gridLayout.addWidget(self.lineEdit_ipaddress, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_Aheight = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Aheight.setObjectName("lineEdit_Aheight")
        self.lineEdit_Aheight.setText('0')
        self.gridLayout.addWidget(self.lineEdit_Aheight, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText('2000')
        self.gridLayout.addWidget(self.lineEdit, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.lineEdit_Bheight = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Bheight.setObjectName("lineEdit_Bheight")
        self.lineEdit_Bheight.setText('0')
        self.gridLayout.addWidget(self.lineEdit_Bheight, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_status = QtWidgets.QLabel(Dialog)
        self.label_status.setObjectName("label_status")
        self.verticalLayout.addWidget(self.label_status)
        self.tableView = QtWidgets.QTableWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.init_table()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_exit.clicked.connect(QCoreApplication.quit)
        self.pushButton_loadA.clicked.connect(self.loadFileA)
        self.pushButton_loadB.clicked.connect(self.loadFileB)
        self.pushButton_connect.clicked.connect(self.connect2controller)
        self.pushButton_start.clicked.connect(self.begin)
        self.pushButton_pause.clicked.connect(self.pause)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Groupbox.setTitle(_translate("Dialog", "Control panel"))
        self.pushButton_loadA.setText(_translate("Dialog", "载入元件位置"))
        self.pushButton_loadB.setText(_translate("Dialog", "载入贴装位置"))
        self.pushButton_connect.setText(_translate("Dialog", "连接"))
        self.pushButton_start.setText(_translate("Dialog", "开始"))
        self.pushButton_pause.setText(_translate("Dialog", "暂停"))
        self.pushButton_exit.setText(_translate("Dialog", "退出"))
        self.groupBox.setTitle(_translate("Dialog", "GroupBox"))
        self.label_4.setText(_translate("Dialog", "元件高度"))
        self.label.setText(_translate("Dialog", "IP地址"))
        self.label_3.setText(_translate("Dialog", "端口"))
        self.label_5.setText(_translate("Dialog", "贴装高度"))
        self.label_2.setText(_translate("Dialog", "当前位置信息"))
        self.label_status.setText(_translate("Dialog", "TextLabel"))

    def loadFileA(self):
        file_name,_ = QFileDialog.getOpenFileName(self,'打开文件',"./","Excel files(*.xls)")
        self.label_status.setText(file_name)
        positiona = excel_read.read_excel(file_name)
        self.counta = positiona.shape[0]
        self.tableView.setRowCount(self.counta)
        for i in range(self.counta):
            self.tableView.setItem(i, 0, QTableWidgetItem(str(positiona[i, 0])))
            self.tableView.setItem(i, 1, QTableWidgetItem(str(positiona[i, 1])))




    def loadFileB(self):
        file_name,_ = QFileDialog.getOpenFileName(self,'打开文件',"./","Excel files(*.xls)")
        self.label_status.setText(file_name)
        positionb = excel_read.read_excel(file_name)
        self.countb = positionb.shape[0]
        if self.tableView.rowCount()<self.countb:
            self.tableView.setRowCount(self.countb)
        for i in range(self.countb):
            self.tableView.setItem(i, 2, QTableWidgetItem(str(positionb[i, 0])))
            self.tableView.setItem(i, 3, QTableWidgetItem(str(positionb[i, 1])))

    def connect2controller(self):
        ip = self.lineEdit_ipaddress.text()
        port = self.lineEdit.text()
        self.client = cmd_send.client_thread(self.q, ip, port)

    def pause(self):
        if self.isPause == True:
            self.isPause = False
            self.pushButton_pause.setText('暂停')
            if hasattr(self, 'i'):
                self.msgrecv('Get OK')
        else:
            self.isPause = True
            self.pushButton_pause.setText('恢复')


#TODO :要让暂停功能更稳定一些，这里应该多设置几条信息类型
    def msgrecv(self,s):
        self.label_status.setText(s)
        if s=='Get OK':
            self.tableView.setItem(self.i, 4, QTableWidgetItem('OK'))
            if self.isPause != True:
                self.i  = self.i + 1
                if self.i < min(self.counta, self.countb):
                    a = self.msg_init(self.i)
                    self.q.put(a)
                else:
                    self.label_status.setText('All Done')





    def begin(self):        #开始往队列里加消息，子线程收到消息就传到下位机
        if hasattr(self,'client'):
            self.client.start()
            self.client.recv_msg.connect(self.msgrecv)
            self.i = 0
            a = self.msg_init(self.i)
            self.q.put(a)
        else:
            self.showdialog("Connect to device first")


    def msg_init(self,i):
        a = 'POS {} {} {} {} {} {} {} {}'.format(self.tableView.item(i, 0).text(),
                                                 self.tableView.item(i, 1).text(),
                                                 self.lineEdit_Aheight.text(), '0',
                                                 self.tableView.item(i, 2).text(),
                                                 self.tableView.item(i, 3).text(),
                                                 self.lineEdit_Aheight.text(), '0')
        return a

    def init_table(self):
        self.tableView.setColumnCount(5)
        self.tableView.setColumnWidth(0,120)
        self.tableView.setColumnWidth(1,120)
        self.tableView.setColumnWidth(2,120)
        self.tableView.setColumnWidth(3,120)

        self.tableView.setHorizontalHeaderLabels(['AX坐标','AY坐标','BX坐标','BY坐标','状态'])


    def showdialog(self, t):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText(t)
        msg.setWindowTitle("MessageBox")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()