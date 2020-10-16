# Import socket module
import socket
import sys
# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 8000

# connect to the server on local computer
s.connect(('', port))
s.send(str.encode(sys.argv[1]))
print(s.recv(4096).decode())
# receive data from the server
print(s.recv(4096).decode())
print(s.recv(4096).decode())
# close the connection
s.close()
