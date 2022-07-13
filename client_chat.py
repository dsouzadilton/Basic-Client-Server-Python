import socket

s = socket.socket()
port = 12345

s.connect(('127.0.0.1', port))
status = 'True'
while status:
        text = s.recv(1024).decode()
        if text != 'over':
                print("Mr. Blue: ", text)
                val = input("You: ")
                s.send(val.encode())
        else :
                status = 'False'
                print("Terminating Connection...")
s.close()
print("Connection Terminated")
