from threading import Thread, Event
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
                if self.queue.empty():
                    print("Queue already empty")


class ClientThread(Thread):
    def __init__(self, conn, ip, port, queue, task_type):
        Thread.__init__(self)
        self.conn = conn
        self.ip = ip
        self.port = port
        self.queue = queue
        self.task_type = task_type
        self._stop_event = Event()
        print("[+] New server socket thread started for " + ip +
              ":" + str(port) + " - " + "Task type : " + str(self.task_type))

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):

        task_created = False
        if self.queue.qsize() == 0:
            self.conn.send(str.encode('no task is on queue'))
        else:
            self.conn.send(str.encode(
                'task is queued in position ' + str(self.queue.qsize())))

        while True:

            if not self.queue.full() and not task_created:
                task_created = True
                if self.task_type == 1:
                    self.queue.put(LongTask(self.conn, self))
                elif self.task_type == 2:
                    self.queue.put(MediumTask(self.conn, self))
                else:
                    self.queue.put(ShortTask(self.conn, self))

            if self.stopped():
                return
