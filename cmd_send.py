import socket
import time
from PyQt5.QtCore import QThread, pyqtSignal
#TODO: 设计消息队列用于主线程与子线程之间的通信
class client_thread(QThread):
    recv_msg = pyqtSignal(str)
    def __init__(self, q, server_ip = '127.0.0.1', server_port=2000):
        super().__init__()
        self.q = q
        self.server_ip = server_ip
        self.server_port = server_port

    def run(self):
        while True:
            try:
                if not self.q.empty():
                    cmd = self.q.get()+'\r\n'
                    if cmd == 'QUIT\r\n':
                        break
                    self.s.send(cmd.encode())
                    a = self.s.recv(1024).decode()
                    self.recv_msg.emit(a)
                else:
                    time.sleep(0.5)
                    # print('looping')
            except socket.error:
                print('fail to setup socket connection')
                self.recv_msg.emit('error')
                break
        pass

    def inisock(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.server_ip, int(self.server_port)))
            self.s = s
            ret = 0
        except socket.error:
            print('fail to setup socket connection')
            ret = -1
        return ret

# def sendcmd(s,cmd):
#     try:
#         s.send(cmd.encode())
#         a = s.recv(1024)
#         return(a.decode())
#         time.sleep(0.2)
#     except socket.error:
#         print('fail to setup socket connection')
#         return 0