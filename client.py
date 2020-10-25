# Import socket module
import socket
import sys
# Create a socket object


def main_c(x, c):
    s = socket.socket()

    address = ['127.0.0.1']
    port = [8000]
    arr = []

    for i in range(len(address)):
        add = address[i]
        po = port[i]

        s = socket.socket()
        s.connect((add, po))
        s.send(str.encode("5"))
        queue = s.recv(4096).decode().split(" ")[-1]
        if(queue == "queue"):
            queue = "0"
        arr.append(int(queue))

    s.close()

    index_min = arr.index(min(arr))

    # Define the port on which you want to connect
    address = address[index_min]
    port = port[index_min]
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
    return 1


def main_c2(x):
    s = socket.socket()

    # Define the port on which you want to connect
    port = 8000

    # connect to the server on local computer
    s.connect(('127.0.0.1', port))

    s.send(str.encode(x))
    message = []
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
    s.close()
    return 1


# def main_c3(x):
#     address = ['127.0.0.1']
#     port = [8000]

#     for i in range(len(address)):
#         add = address[i]
#         po = port[i]
#         s = socket.socket()

#         # Define the port on which you want to connect
#         port = 8000

#         # connect to the server on local computer
#         s.connect(('127.0.0.1', port))

#         s.send(str.encode(x))
#         message = []
#         queue = s.recv(4096).decode().split(" ")[-1]
#         if(queue == "queue"):
#             queue = "0"
#         print("Worker {}:{} Queue: {:>30}".format(add, po, queue))
#         # receive data from the server
#         # close the connection
#         s.close()
#     return 1


# def main_c4(x):
#     address = ['127.0.0.1']
#     port = [8000]

#     for i in range(len(address)):
#         add = address[i]
#         po = port[i]
#         s = socket.socket()

#         # Define the port on which you want to connect
#         port = 8000

#         # connect to the server on local computer
#         s.connect(('127.0.0.1', port))

#         s.send(str.encode(x))
#         message = []
#         queue = s.recv(4096).decode().split(" ")[-1]
#         if(queue == "queue"):
#             queue = 0
#         if(int(queue) > 0):
#             print("Worker {}:{} is Busy".format(add, po))
#         else:
#             print("Worker {}:{} is Available".format(add, po))
#         # receive data from the server
#         # close the connection
#         s.close()
#     return 1
