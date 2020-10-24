# Import socket module
import socket
import sys
# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 8000

# connect to the server on local computer
s.connect(('127.0.0.1', port))
sys.setrecursionlimit(999999999)
var =sys.argv
if len(var)== 3: 
     s.send(str.encode(sys.argv[1] + " " + sys.argv[2]))
elif len(var)== 5: 
     s.send(str.encode(sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4]))
else:
     s.send(str.encode(sys.argv[1]))
print(s.recv(4096).decode())
# receive data from the server
print(s.recv(4096).decode())
print(s.recv(4096).decode())
print(s.recv(4096).decode())
print(s.recv(4096).decode())
# close the connection
s.close()
