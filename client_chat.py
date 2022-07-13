import socket
import os

s = socket.socket()		
r, w = os.pipe()

port = 12345				

s.connect(('127.0.0.1', port))
data = s.recv(1024).decode()
s.close()

def isPalindrome(str):
            if str == str[::-1]:
                print("It's a Pallindrome")
            else :
                print("It's not a Pallindrome")

def parent_child():
    p2 = os.fork()
    if p2 == 0:
        intel[1] = intel[1].upper()
        print("Second part to upper: ",intel[1])
    elif p2 > 0:
        p1 = os.fork()
        if p1 == 0:
            isPalindrome(str)
        elif p1 > 0:
            p1 = os.fork()
        print("Child process and id is : ", os.getpid())
        
print("Recieved data: ",data)
intel = []
intel = data.split()
str = intel[0]
parent_child()
