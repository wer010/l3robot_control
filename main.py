# 作为机器人控制器的上位机程序的主界面，
# 使用pyqt5作为界面设计
# 主要功能：1、读取excel中的坐标点位置；2、把位置按照格式传送至下位机；3、中途发生错误记录当前位置信息
import sys
import MyWindow
from PyQt5.QtWidgets import QApplication




def main():
    app = QApplication(sys.argv)
    window = MyWindow.mywindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()




