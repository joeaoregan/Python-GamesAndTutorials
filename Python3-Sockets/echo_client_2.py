#!/usr/bin/env python3
"""
Joe O'Regan
21/02/2019
TCP Echo Client with encode/decode
"""

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8888         # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('TCP Echo Client Connecting To',HOST,':',PORT)

data = input(' -> ')
s.sendall(data.encode())

data = s.recv(1024).decode()

print('Received', repr(data))

s.close()
