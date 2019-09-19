import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srvadr = ('10.22.8.155', 12345)
msg ='I want to join passenger queue'
waiting = []
while True:
    sock.sendto(msg.encode(), srvadr)
    data, addr = sock.recvfrom(1024)

#1. send message to stand in queue
    #2. get message from server that we are in queue
    #3. wait until server tells us about a wagon to ride
    #4. talk to wagon to setup a ride, if fail stand in line again
    #5. wait until wagon ride ends, get message from wagon and stand in line
    print(data)
    while True:
        data2, addr2 = sock.recvfrom(1024)
        i = data2.decode()
        x = i.split(',')
        y = x[0]
        if y == 'this wagon':
            print(y)
            msg1 = 'message received'
            sock.sendto(msg1.encode(), srvadr)
            


