import os
import socket
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 60001 # Reserve a port for your service.

s.connect((host, port))

f = open('tests/welcome.wav','rb')
print("Sending...")
l = f.read(4096)
while (l):
    print("Sending...")
    s.send(l)
    l = f.read(4096)
f.close()
print("Done Sending")
s.shutdown(socket.SHUT_WR)
print (s.recv(1024))
s.close()