import socket as sk
import json

HOST = '10.22.8.155'
PORT = 12345
WAGON_SIZE = 2

s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
s.bind((HOST, PORT))

passengerQueue = []
wagonQueue = []


def addPassenger(address):  # add an IP + port to our passenger queue
    passengerQueue.append(address)
    s.sendto("You entered the passenger queue".encode(), address)
    print("Added the user to the passenger queue")


def addWagon(address):  # add an ip + port to our wagon queue
    wagonQueue.append(address)
    s.sendto("You entered the wagon queue".encode(), address)
    print("Added the user to the wagon queue")


def checkAvailableRide():  # check if we have a wagon and enough passengers for it, send away the wagon with the passengers
  	#do we have a wagon and enough people for it?
    if ((len(passengerQueue) >= WAGON_SIZE) and (len(wagonQueue) >= 1)):
        currentWagon = wagonQueue.pop(0)
        j, l = currentWagon #splits the first element in the wagon queue in order to get the clients ip address
        for i in range(WAGON_SIZE): #tell each passenger the wagon ip, and tell wagon each passenger ip
            currentPassenger = passengerQueue.pop(0)
            x, y = currentPassenger #splits the first element in the passenger queue in order to get the clients ip address
            s.sendto(('these shits,', str(x)).encode(), currentWagon)
            s.sendto(('this wagon,', str(j)).encode(), currentPassenger)
            data3, addr3 = sock.recvfrom(1024) #check if message was received by the client
            k = data3.decode()
            if k == 'message received':
                print('good')


def sendAnotherPassenger(address):
    newPassenger = passengerQueue.pop(0)  # pop first passenger in queue
    s.sendto(newPassenger[0].encode(), address)
    print("Sent a new passenger to wagon with disconnected passenger")


while 1:
    payload, client_address = s.recvfrom(65536)
    #data = json.loads(payload.decode())

    print("Received payload: " + payload.decode())

    payload = payload.decode()
    # if-else statement to handle the message received
    if (payload == "I want to join passenger queue"):
        addPassenger(client_address)
    elif (payload == "I want to join wagon queue"):
        addWagon(client_address)
    elif (payload == "I need one more passenger"):
        sendAnotherPassenger(client_address)


    checkAvailableRide() #check the queues if we can send wagon with passenger
