#!/usr/bin/env python3
"""
Joe O'Regan
21/02/2019
Looping TCP Echo Server
"""

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8888  # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Echo Server: Listening for connections on', HOST, ':', PORT)

conn, address = s.accept()
print("Connection from: " + str(address))

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print('Received from '+str(address)+': '+str(data))

    conn.sendall(data.encode())

conn.close()
