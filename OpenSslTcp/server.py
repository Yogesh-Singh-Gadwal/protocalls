import socket
import sys 
import ssl

KEY="key"
CERT="cert"

#Creating socket:
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

srvr_addr=('localhost',10005)

sock.bind(srvr_addr)			#server address
#listening on port:
sock.listen(1)


s_ssl = ssl.wrap_socket(sock,keyfile=KEY,certfile=CERT,server_side=True)

#accepting client connection
connection, clnt_addr=s_ssl.accept()

#recieve from client
data = connection.recv(50)

#sending same data back
connection.sendall(data)

connection.close()
