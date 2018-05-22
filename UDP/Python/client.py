import socket
import sys

#create sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#declare the addres  in this particular it is local host but it could be anything like domain or ip address
server_address = ('localhost', 10001)

#message to be send
message = 'This is the message.  It will be repeated.'

#send message to specified address
sock.sendto(message,server_address)

#recieve data from specified address 
#1025 represents the maximum bite could recieved
data=sock.recvfrom(1025)
print(data)
sock.close()



