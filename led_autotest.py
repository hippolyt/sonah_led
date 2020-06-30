import socket
import time

def receive():
    time.sleep(1)
    response = s.recv(2048)
    return response

ipList = [
           # "192.168.1.1", 
           # "192.168.1.2", 
            "10.1.0.104"
            ]
portList = [1100, 8900]
command1 = b'\x00\x00\x00\x40\x01\x02\x57\x30\x30\x00\x00\x00\x32\xFD\x07\x06\x00\x00\x00\x91\x92\x33\xFE'
command2 = b'\x00\x00\x00\x40\x01\x02\x57\x30\x30\x00\x00\x00\x32\xFD\x07\x06\x00\x00\x00\x94\x94\x94\xFE'

for ip in ipList:
    for port in portList:
        print("\n")
        print(ip, ":", port)
        try:
            s = socket.socket()
            s.settimeout(10)
            s.connect((ip,port))
        except Exception as e:
            print("No connection", e)
            continue
        try:    
            s.send(command1)
        except Exception as e:
            print("Sending failed", e)
            continue
        try:
            response = receive()
        except Exception as e:
            print("Receiving failed", e)
        if response == b'\x06':
            print("Success")
            s.send(command2)
            time.sleep(3)
        else:
            print("Unknown Response", response)
