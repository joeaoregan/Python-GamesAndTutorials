# https://www.youtube.com/watch?v=szm3camsf8k
# Port Scanner
# Scans ports and tells if they are open or closed
# Not very efficient

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # Create a socket, SOCK_STREAM = TCP connection
server = 'pythonprogramming.net'        # server based on domain name


def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False


for x in range(1,26):       # test port numbers 1 to 25
    if pscan(x):
        print('Port ',x,' is open!!!!!!')
    else:
        print('Port ',x,' is closed')
