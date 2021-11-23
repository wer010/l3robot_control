# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lanhai/Projects/l3robot_control/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QRect,pyqtSignal,QCoreApplication
from PyQt5.QtWidgets import QComboBox,QMessageBox,QTableWidgetItem,QCheckBox,QMainWindow,QLineEdit,QSlider,QGroupBox,QPushButton, QFileDialog, QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QLabel
import excel_read
import cmd_send
import queue
import time


class Ui_Dialog(object):
    q = queue.Queue(0)
    i = 0

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

        ###################grid view start
        self.lineEdit_ipaddress.setSizePolicy(sizePolicy)
        self.lineEdit_ipaddress.setObjectName("lineEdit_ipaddress")
        self.lineEdit_ipaddress.setText("192.168.0.1")
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
        self.label_cb = QtWidgets.QLabel(self.groupBox)
        self.label_cb.setText('加载模式')
        self.gridLayout.addWidget(self.label_cb)
        self.combobox = QComboBox(self.groupBox)
        self.combobox.addItems(['坐标模式','托盘模式'])
        self.gridLayout.addWidget(self.combobox)

        self.checkbox_gotoc = QCheckBox('蘸胶工序',self.groupBox)
        self.gridLayout.addWidget(self.checkbox_gotoc)

        self.lineEdit_cpos = QLineEdit(self.groupBox)
        self.gridLayout.addWidget(self.lineEdit_cpos)


        self.label_offset = QtWidgets.QLabel(self.groupBox)
        self.label_offset.setText('偏移量')
        self.gridLayout.addWidget(self.label_offset)
        self.lineEdit_offset = QLineEdit(self.groupBox)
        self.gridLayout.addWidget(self.lineEdit_offset)

        self.label_index = QtWidgets.QLabel(self.groupBox)
        self.label_index.setText('当前序号')
        self.gridLayout.addWidget(self.label_index)
        self.lineEdit_index = QLineEdit(self.groupBox)
        self.lineEdit_index.setValidator(QtGui.QIntValidator())
        self.lineEdit_index.setText('1')
        self.gridLayout.addWidget(self.lineEdit_index)
        # ##################grid view end

        self.verticalLayout.addWidget(self.groupBox)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_status = QtWidgets.QLabel(Dialog)
        self.label_status.setObjectName("label_status")
        self.verticalLayout.addWidget(self.label_status)

        # draw the table
        self.tableView = QtWidgets.QTableWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.init_table(self.combobox.currentIndex())

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_exit.clicked.connect(QCoreApplication.quit)
        self.pushButton_loadA.clicked.connect(self.loadFileA)
        self.pushButton_loadB.clicked.connect(self.loadFileB)
        self.pushButton_connect.clicked.connect(self.connect2controller)
        self.pushButton_start.clicked.connect(self.begin)
        self.pushButton_pause.clicked.connect(self.pause)
        self.combobox.currentIndexChanged.connect(self.init_table)
        self.checkbox_gotoc.stateChanged.connect(self.changecb1)

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
        self.checkbox_gotoc.setChecked(True)

    def changecb1(self):
        self.lineEdit_cpos.setEnabled(self.checkbox_gotoc.isChecked())

    def loadFileA(self):
        file_name,_ = QFileDialog.getOpenFileName(self,'打开文件',"./","Excel files(*.xls)")
        self.label_status.setText(file_name)
        if file_name != '':
            positiona = excel_read.read_excel(file_name)
            self.counta = positiona.shape[0]
            self.tableView.setRowCount(self.counta)
            for i in range(self.counta):
                self.tableView.setItem(i, 0, QTableWidgetItem(str(positiona[i, 0])))
                self.tableView.setItem(i, 1, QTableWidgetItem(str(positiona[i, 1])))
                self.tableView.setItem(i, 2, QTableWidgetItem(str(positiona[i, 2])))
                self.tableView.setItem(i, 3, QTableWidgetItem(str(positiona[i, 3])))
            if self.combobox.currentIndex()==1:
                self.tableView.insertRow(self.counta)
                self.counta = int(positiona[-1,0])*int(positiona[-1,1])
                self.tableView.setItem(self.tableView.rowCount()-1,0,QTableWidgetItem('Total number {}'.format(self.counta)))
                self.tableView.setItem(self.tableView.rowCount()-1,1,QTableWidgetItem('Current done number {}'.format(int(self.i))))

    def loadFileB(self):
        file_name,_ = QFileDialog.getOpenFileName(self,'打开文件',"./","Excel files(*.xls)")
        self.label_status.setText(file_name)
        if file_name != '':
            positionb = excel_read.read_excel(file_name)
            self.countb = positionb.shape[0]
            if self.tableView.rowCount()<self.countb:
                self.tableView.setRowCount(self.countb)
            for i in range(self.countb):
                self.tableView.setItem(i, 4, QTableWidgetItem(str(positionb[i, 0])))
                self.tableView.setItem(i, 5, QTableWidgetItem(str(positionb[i, 1])))
                self.tableView.setItem(i, 6, QTableWidgetItem(str(positionb[i, 2])))
                self.tableView.setItem(i, 7, QTableWidgetItem(str(positionb[i, 3])))
            if self.combobox.currentIndex()==1:
                self.countb = int(positionb[-1,0])*int(positionb[-1,1])
                self.tableView.setItem(self.tableView.rowCount()-1,2,QTableWidgetItem('Total number {}'.format(self.countb)))
                self.tableView.setItem(self.tableView.rowCount()-1,3,QTableWidgetItem('Current done number {}'.format(int(self.i))))

    def connect2controller(self):
        ip = self.lineEdit_ipaddress.text()
        port = self.lineEdit.text()
        self.client = cmd_send.client_thread(self.q, ip, port)
        if self.client.inisock()==0:
            self.showdialog("连接成功")

    def pause(self):
        if self.isPause == True:
            self.isPause = False
            self.pushButton_pause.setText('暂停')
            if hasattr(self, 'i'):
                self.i = int(self.lineEdit_index.text()) - 1
                self.msgrecv('Put OK\r\n')
        else:
            self.isPause = True
            self.pushButton_pause.setText('恢复')


    # 子线程消息接收处理
    def msgrecv(self,s):
        self.label_status.setText(s)
        if 'Put OK' in s:
            # 放好一个，接着放下一个
            if self.combobox.currentIndex() == 0:
                self.tableView.setItem(self.i, 8, QTableWidgetItem('OK'))
            else:
                self.tableView.setItem(self.tableView.rowCount() - 1, 1,
                                       QTableWidgetItem('Current done number {}'.format(int(self.i))))
            if (not self.isPause):
                if ((self.i+1) < min(self.counta, self.countb)):
                    self.i +=1
                    self.lineEdit_index.setText(str(self.i+1))
                    if self.combobox.currentIndex()==0:
                        self.send_pos()
                    else:
                        self.send_plt()
                else:
                    self.msgsend('HOME')
                    self.label_status.setText('All Done')
                    self.msgsend('QUIT')

    def msgsend(self,s):
        if self.q.empty():
            self.q.put(s)
        time.sleep(0.2)


    def init_robot(self, us_cposition, mode):
        # us_cposition:bool, 是否使用蘸胶工序
        # mode: int, 0为位置模式，1为托盘模式
        if us_cposition and self.lineEdit_cpos.text() != None:
            a = 'CPOS ' + self.lineEdit_cpos.text()
            self.msgsend(a)
        if mode == 1:
            a = 'Pallet1 {} {} {} {} {} {} {} {} {} {}'.format(self.tableView.item(0, 0).text(),
                                                               self.tableView.item(0, 1).text(),
                                                               self.tableView.item(1, 0).text(),
                                                               self.tableView.item(1, 1).text(),
                                                               self.tableView.item(2, 0).text(),
                                                               self.tableView.item(2, 1).text(),
                                                               self.tableView.item(3, 0).text(),
                                                               self.tableView.item(3, 1).text(),
                                                               self.tableView.item(4, 0).text(),
                                                               self.tableView.item(4, 1).text())
            self.msgsend(a)
            a = 'Pallet2 {} {} {} {} {} {} {} {} {} {}'.format(self.tableView.item(0, 2).text(),
                                                               self.tableView.item(0, 3).text(),
                                                               self.tableView.item(1, 2).text(),
                                                               self.tableView.item(1, 3).text(),
                                                               self.tableView.item(2, 2).text(),
                                                               self.tableView.item(2, 3).text(),
                                                               self.tableView.item(3, 2).text(),
                                                               self.tableView.item(3, 3).text(),
                                                               self.tableView.item(4, 2).text(),
                                                               self.tableView.item(4, 3).text())
            self.msgsend(a)
        return



    def send_pos(self):
        a = self.posmsg_init(self.i)
        self.msgsend(a)
        return

    def send_plt(self):
        a = self.pltmsg_init(self.i+1)
        self.msgsend(a)

    def begin(self):        #开始往队列里加消息，子线程收到消息就传到下位机
        if hasattr(self,'client'):
            self.client.start()
            self.client.recv_msg.connect(self.msgrecv)
            self.init_robot(self.checkbox_gotoc.isChecked(), mode = self.combobox.currentIndex())


            self.i = int(self.lineEdit_index.text())-1
            if self.combobox.currentIndex()==0:
                self.send_pos()
            else:
                self.send_plt()
        else:
            self.showdialog("Connect to device first")

    def posmsg_init(self,i):
        ax, ay, bx, by = [0, 0, 0, 0]
        res = self.lineEdit_offset.text().split()
        if len(res)==4:
            ax, ay, bx, by = res

        a = 'POS {} {} {} {} {} {} {} {}'.format(float(self.tableView.item(i, 0).text()) + float(ax),
                                                 float(self.tableView.item(i, 1).text())+ float(ay),
                                                 self.tableView.item(i, 2).text(),
                                                 self.tableView.item(i, 3).text(),
                                                 float(self.tableView.item(i, 4).text())+ float(bx),
                                                 float(self.tableView.item(i, 5).text())+ float(by),
                                                 self.tableView.item(i, 6).text(),
                                                 self.tableView.item(i, 7).text())
        return a

    def pltmsg_init(self,i):
        a = 'PLT {} {} {}'.format(i, self.lineEdit_Aheight.text(), self.lineEdit_Bheight.text())
        return a

    def init_table(self,flag):
        self.tableView.clear()
        self.tableView.setRowCount(0)
        if flag==0:
            self.tableView.setColumnCount(9)
            # self.tableView.setColumnWidth(0,120)
            # self.tableView.setColumnWidth(1,120)
            # self.tableView.setColumnWidth(2,120)
            # self.tableView.setColumnWidth(3,120)
            self.tableView.setHorizontalHeaderLabels(['A坐标X','A坐标Y','A坐标Z','A角度A','B坐标X','B坐标Y','B坐标Z','B角度A','状态'])
        else:
            self.tableView.setColumnCount(8)
            # self.tableView.setColumnWidth(0, 150)
            # self.tableView.setColumnWidth(1, 150)
            # self.tableView.setColumnWidth(2, 150)
            # self.tableView.setColumnWidth(3, 150)
            self.tableView.setHorizontalHeaderLabels(['A坐标X','A坐标Y','A坐标Z','A角度A','B坐标X','B坐标Y','B坐标Z','B角度A'])

    def showdialog(self, t):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText(t)
        msg.setWindowTitle("MessageBox")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()