import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srvadr = ('10.22.8.155', 12345)
msg ='I want to join wagon queue'
waiting = []
while True:
    sock.sendto(msg.encode(), srvadr)
    data, addr = sock.recvfrom(1024)
    print(data)
    while True:
        data2,addr2 = sock.recvfrom(1024)
        i = data2.decode()
        x = i.split(',')
        y = x[0]
        if y == 'these shits':
            print(y)
    
