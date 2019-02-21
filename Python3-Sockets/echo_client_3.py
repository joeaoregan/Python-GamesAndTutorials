#!/usr/bin/env python3
"""
Joe O'Regan
21/02/2019
Looping TCP Echo Client
"""

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8888         # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('TCP Echo Client Connecting To',HOST,':',PORT)

data = input(' -> ')

while data.lower().strip() != 'exit':
    s.sendall(data.encode())

    data = s.recv(1024).decode()

    print('Server:', repr(data))

    data = input(' -> ')

s.close()
