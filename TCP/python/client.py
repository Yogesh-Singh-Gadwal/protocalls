#The client program sets up its socket differently from the way a server does. Instead of binding to a port and listening, it uses connect() to attach #the socket directly to the remote address.
import socket
import sys

## Connect the socket to the port where the server is listening
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#After the connection is established, data can be sent through the socket with sendall() and received with recv(), just as in the server.
server_address = ('localhost', 10001)
sock.connect(server_address)

message = 'This is the message.  It will be repeated.'

# Send data
sock.sendall(message)
#recieve data
data = sock.recv(25)
print(data)

#close the socket
sock.close()



