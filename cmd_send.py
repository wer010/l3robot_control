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