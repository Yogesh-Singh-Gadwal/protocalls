import socket
import sys

#Creating socket:
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

srvr_addr=('127.0.0.1',22002)

print>>sys.stderr,'setting up %s on port %s' % srvr_addr

#Binding socket:
sock.bind(srvr_addr)

#listening on port:
sock.listen(1)
f=open("recieved.txt","a+")

while True:
    #waiting for connection
    print>>sys.stderr,'waiting for connection'
    #accepting client connection
    connection, clnt_addr=sock.accept()

    try:
        print>>sys.stderr,'connection from',clnt_addr
        while True:
            data = connection.recv(50)
            print>>sys.stderr,'received "%s" ' % data
            if data:
                f.write(data)
                print>>sys.stderr,'Sending data back to client'
                connection.sendall(data)
            else:
                print>>sys.stderr,'no more data from ',clnt_addr
                break
    finally:
        #closing connection:
        connection.close()
