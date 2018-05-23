import sys
import socket
import ssl

#creating sockets
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#server address
#srvr_add=('localhost',10001)

#wrapping socket with ssl
ssl_sock=ssl.wrap_socket(sock,cert_reqs=1,ca_certs='cert')

#connecting to address
ssl_sock.connect(('127.0.0.1', 10005))
message='this is the echo message'

#send the message
ssl_sock.sendall(message)

#recieving data
data=ssl_sock.recv(50)
print(data)

#close the socket
sock.close()


