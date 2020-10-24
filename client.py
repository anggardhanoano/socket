# Import socket module
import socket
import sys
# Create a socket object
def main_c(x, c):
    s = socket.socket()

    # Define the port on which you want to connect
    port = 8000

    # connect to the server on local computer
    s.connect(('127.0.0.1', port))
    # s.send(str.encode(sys.argv[1]))
    if x == "2": 
        temp = []
        print("Enter a website link: ")
        i = input()
        s.send(str.encode(x + " " + i))
    elif x == "1": 
        print("Enter Currency From, Currency To and Amount")
        print()
        i = input()
        i = i.split(" ")
        s.send(str.encode(x + " " + i[0] + " " + i[1] + " " + i[2]))
    else:
        s.send(str.encode(x))
    x = x + "-" + str(c)
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
    # s.send(str.encode(sys.argv[1]))
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
    
    