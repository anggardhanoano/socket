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
    s.send(str.encode(x))
    message = []
    x = x + "-" + str(c)
    print("{:>30}{:>30}".format(x, s.recv(4096).decode()))
    # receive data from the server
    print("{:>30}{:>30}".format(x, s.recv(4096).decode()))
    print("{:>30}{:>30}".format(x, s.recv(4096).decode()))
    # close the connection
    s.close()
    return 1
