# Import socket module
import socket
import sys
# Create a socket object

worker_address = ['18.207.226.80', '3.84.192.40', '52.207.212.113']
ports = [8000, 8000, 8000]


def main_c(x, c):
    s = socket.socket()

    min_task = 1000000
    index_add = 0

    for i in range(len(worker_address)):
        add = worker_address[i]
        po = ports[i]

        s = socket.socket()
        try:
            s.connect((add, po))
            s.send(str.encode("5"))

            queue = s.recv(4096).decode().split(" ")[-1]
            if(queue == "queue"):
                queue = "0"
            # arr.append(int(queue))
            if int(queue) < min_task:
                min_task = int(queue)
                index_add = i
        except:
            print("there is a problem connect to {}".format(add))

    s.close()

    # Define the port on which you want to connect
    try:
        address = worker_address[index_add]
        port = ports[index_add]
        s = socket.socket()
        # connect to the server on local computer
        s.connect((address, port))
        s.send(str.encode(x))
        x = x[0] + "-" + str(c)
        print("{:>30}{:>30}".format(x, s.recv(4096).decode()))
        # receive data from the server
        print("{:>30}{:>30}".format(x, s.recv(4096).decode()))
        print("{:>30}{:>30}".format(x, s.recv(4096).decode()))
        t = s.recv(4096).decode()
        if(t != ""):
            print("{:>30}{:>30}".format(x, t))
        t = s.recv(4096).decode()
        if(t != ""):
            print("{:>30}{:>30}".format(x, t))
        # close the connection
        # close the connection
        s.close()
    except Exception as e:
        print("all worker is unavailable :(")
    return 1


def main_c3(x):

    for i in range(len(worker_address)):
        add = worker_address[i]
        po = ports[i]
        s = socket.socket()

        # Define the port on which you want to connect

        # connect to the server on local computer
        try:
            s.connect((add, po))

            s.send(str.encode(x))
            message = []
            queue = s.recv(4096).decode().split(" ")[-1]
            if(queue == "queue"):
                queue = "0"
            print("Worker {}:{} Queue: {:>30}".format(add, po, queue))
        except Exception as e:
            print(add + " - " + str(e))
        # receive data from the server
        # close the connection
        s.close()
    return 1


def main_c4(x):

    for i in range(len(worker_address)):
        add = worker_address[i]
        po = ports[i]
        s = socket.socket()

        # Define the port on which you want to connect

        # connect to the server on local computer
        try:
            s.connect((add, po))

            s.send(str.encode(x))
            message = []
            queue = s.recv(4096).decode().split(" ")[-1]
            if(queue == "queue"):
                queue = 0
            if(int(queue) > 0):
                print("Worker {}:{} is Busy".format(add, po))
            else:
                print("Worker {}:{} is Available".format(add, po))
        except Exception as e:
            print(add + " - " + str(e))
        # receive data from the server
        # close the connection
        s.close()
    return 1
