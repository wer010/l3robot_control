# 作为机器人控制器的上位机程序的主界面，
# 使用pyqt5作为界面设计
# 主要功能：1、读取excel中的坐标点位置；2、把位置按照格式传送至下位机；3、中途发生错误记录当前位置信息
import sys
import MyWindow
from PyQt5.QtWidgets import QApplication
import socket
import time

def inisock():
    server_ip = '192.168.0.1'
    server_port = 2000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.0.10', 0))
    try:
        s.connect((server_ip, server_port))
    except socket.error:
        print('fail to setup socket connection')
    return s

def sendcmd(s,cmd):
    try:
        s.send(cmd.encode())
        a = s.recv(1024)
        print(a)
        time.sleep(0.2)
    except socket.error:
        print('fail to setup socket connection')

def main():
    app = QApplication(sys.argv)
    window = MyWindow.mywindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()




