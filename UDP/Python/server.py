import socket
import sys
#create sockets
socfd=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#address declaration
server_address = ('localhost',10001)
print("server created")

#bind the server address to the socket family
socfd.bind(server_address)

#data recieve the data and addrs recieve the address of the cliend data being recieved
data,addrs = socfd.recvfrom(1024)
print(data)

#send the data back tp the address
#address must be sting form only
socfd.sendto(data,addrs)
socfd.close()
