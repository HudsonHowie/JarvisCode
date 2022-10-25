#!/usr/bin/python

import socket                   # Import socket module
import os

port = 60001                  # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()


# Get local machine name
s.bind((host, port))
f = open('fare.wav', 'wb')
# Bind to the port
s.listen(1)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    print ("Recieving...")
    l = conn.recv(4096)
    while (l):
       print("Recieving...")
       f.write(l)
       l = conn.recv(4096)
    f.close()
    print('Done receiving')
    conn.send(b'Thank you for connecting')
    conn.close()
    break