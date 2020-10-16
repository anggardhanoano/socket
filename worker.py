# COPY FROM GEEKSFORGEEKS
from etc.threads import *
import socket
import time
import threading
import queue

s = socket.socket()
taks_queue = queue.Queue()
threads = []
print("Socket successfully created")

port = 12345

s.bind(('', port))
print("socket binded to " + str(port))


def worker():
    c = TaskThread(name='commands', queue=taks_queue)
    c.start()
    threads.append(c)


def server():
    while True:
        s.listen(5)
        print("socket is listening")
        (conn, (ip, port)) = s.accept()
        print("Got connection from" + str(ip))
        task_type = int(conn.recv(1024))
        newthread = ClientThread(conn, ip, port, taks_queue, task_type)
        newthread.start()
        threads.append(newthread)


if __name__ == "__main__":
    worker()
    server()
    for t in threads:
        t.join()
