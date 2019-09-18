import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srvadr = ('192.168.56.1', 12345)
msg ='I want to join passenger queue'
waiting = []
while True:
    sock.sendto(msg.encode(), srvadr)
    data, addr = sock.recvfrom(1024)
    print(data)
    break
