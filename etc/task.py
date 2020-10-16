import time


class Task(object):
    def __init__(self, client):
        self.client = client
        print("task created")

    def work(self):
        pass


class LongTask(Task):

    def work(self):
        self.client.send(str.encode('ON PROGRESS TASK 1'))
        time.sleep(10)
        self.client.send(str.encode('HELLO WORLD DARI TASK 1'))
        self.client.close()


class MediumTask(Task):

    def work(self):
        self.client.send(str.encode('ON PROGRESS TASK 2'))
        time.sleep(3)
        self.client.send(str.encode('HELLO WORLD DARI TASK 2'))
        self.client.close()


class ShortTask(Task):

    def work(self):
        self.client.send(str.encode('ON PROGRESS TASK 3'))
        time.sleep(1)
        self.client.send(str.encode('HELLO WORLD DARI TASK 3'))
        self.client.close()
