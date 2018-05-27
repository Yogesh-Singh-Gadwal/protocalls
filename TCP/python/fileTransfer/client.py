import sys
import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#define server address:
srvr_add=('localhost',22002)

print>>sys.stderr,'connecting to %s port %s' % srvr_add

sock.connect(srvr_add)
#toSend.txt is the name of file which is going to sent
f=open("tosend.txt","r")

try:
    #tosend ='this is the echo message'
    tosend=f.read(50)
    print>>sys.stderr,'sending "%s"' %tosend
    sock.sendall(tosend)

    bits_recv=0
    bits_expected = len(tosend)

    while bits_recv < bits_expected:
        data=sock.recv(20)
        bits_recv+=len(data)
        print>>sys.stderr,'received: "%s"' %data

finally:
    print>>sys.stderr,'closing socket'
    sock.close()
