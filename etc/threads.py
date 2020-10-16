from threading import Thread
from .task import *
import logging
import time
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


class TaskThread(Thread):
    def __init__(self, group=None, target=None, name=None, queue=None,
                 args=(), kwargs=None, verbose=None):
        Thread.__init__(self)
        self.target = target
        self.name = name
        self.queue = queue

    def run(self):
        while True:
            if not self.queue.empty():
                job = self.queue.get()
                logging.debug("Queueing task")
                job.work()
                logging.debug("Finshed queue")


class ClientThread(Thread):
    def __init__(self, conn, ip, port, queue, task_type):
        Thread.__init__(self)
        self.conn = conn
        self.ip = ip
        self.port = port
        self.queue = queue
        self.task_type = task_type
        print("[+] New server socket thread started for " + ip +
              ":" + str(port) + " - " + "Task type : " + str(self.task_type))

    def run(self):
        if self.queue.qsize() == 0:
            self.conn.send(str.encode('no task is on queue'))
        else:
            self.conn.send(str.encode(
                'task is queued in position ' + str(self.queue.qsize())))

        if not self.queue.full():
            if self.task_type == 1:
                self.queue.put(LongTask(self.conn))
            elif self.task_type == 2:
                self.queue.put(MediumTask(self.conn))
            else:
                self.queue.put(ShortTask(self.conn))
