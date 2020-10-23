# COPY FROM GEEKSFORGEEKS
from etc.threads import *
import socket
import time
import threading
import queue

s = socket.socket()
taks_queue = queue.Queue()
threads = []
clients = []
print("Socket successfully created")

port = 8000

s.bind(('127.0.0.1', port))
print("socket binded to " + str(port))


def worker():
    for i in range(4):
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

        if task_type == 4:
            conn.send(str.encode('Task in queue ' + str(taks_queue.qsize())))
            conn.close()
        elif task_type == 5:
            conn.send(str.encode('Thread in worker ' +
                                 str(len([thread for thread in clients if not thread.stopped()]))))
            conn.close()
        else:
            newthread = ClientThread(conn, ip, port, taks_queue, task_type)
            newthread.start()
            clients.append(newthread)


if __name__ == "__main__":
    worker()
    server()
    for t in threads:
        t.join()

    for t in clients:
        t.join()
