# https://www.youtube.com/watch?v=wzrGwor2veQ
# Python TCP sockets

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # Create a socket, SOCK_STREAM = TCP connection
print(s)

server = 'pythonprogramming.net'        # server based on domain name
port = 80

server_ip = socket.gethostbyname(server)        # get the ip address (or ping to get address)
print(server_ip)

request = "GET / HTTP/1.1\nHost: " + server + "\n\n"

# s.connect(("pythonprogramming.net", 80))
s.connect((server, port))
s.send(request.encode())        # Python2 vs Python3 makes distinction
result = s.recv(4096)       # buffer, how much data we are downloading at any given moment

print(result)

while len(result) > 0:
    print(result)
    # result = s.recv(4096)
    result = s.recv(1024)
