# https://www.youtube.com/watch?v=icE6PR19C0Y
# Threaded Port Scanner
# Scans ports and tells if they are open or closed

import socket
import threading
from queue import Queue

print_lock = threading.Lock()

target = 'pythonprogramming.net'


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port',port,'is open!')

        con.close()

    except:
        pass        # no need to print anything


def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()       # empty queue

q = Queue()         # define queue

# for x in range(30):
for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()       # has to be called after daemon

# for worker in range(1, 101):        # test first 100 ports, port 0 is an invalid port
for worker in range(1, 10000):        # test first 100 ports, port 0 is an invalid port
    q.put(worker)

q.join()
