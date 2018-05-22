#This sample program, based on the one in the standard library documentation, receives incoming messages and echos them back to the sender. It starts #by creating a TCP/IP socket.
import socket
import sys

# Create a TCP/IP socket
socfd=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Then bind() is used to associate the socket with the server address. In this case, the address is localhost, referring to the current server, and the #port number is 10000.

# Bind the socket to the port
server_address = ('localhost',10001)
print("server created")
socfd.bind(server_address)

#Calling listen() puts the socket into server mode, and accept() waits for an incoming connection.
# Listen for incoming connections
socfd.listen(1)
connection, client_address = socfd.accept()

# recev recieve the the data from client in this particular it will accept only 25 byte accept this it will ignore all the data sent by client
data = connection.recv(25)
if data:
	print >>sys.stderr, 'sending data back to the client'
#send all sends the data to everyone who wil have the address to recieve can recieve it by port and ip
	connection.sendall(data)
else:
	print >>sys.stderr, 'no more data from', client_address    

#closing the socket otherwise port will be open and no one can utilise that port
socfd.close()
