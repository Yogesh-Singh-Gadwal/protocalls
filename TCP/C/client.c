#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <arpa/inet.h>


int main(int argc, char *argv[])
{
	if (argc < 3)
	{	// using command line argument
		printf("Usage: %s <serv_ip> <serv_port>\n", argv[0]);
		exit(1);
	}

	int cfd, serv_port;
	serv_port = strtoul(argv[2], NULL, 10);//string to unsigned long
	
	int s= socket(PF_INET,SOCK_STREAM,0);
	if(s<0){
		perror("socket");
		exit(2);	
	}
	/*
	Create your Socket do error checking
	Remember socket returns a socket descriptor
	SOCK_STREAM --->TCP
	or
	SOCK_DGRAM  --->UDP
	AF_INET ------->protocol/address family
	*/
	
	struct sockaddr_in saddr = {0};
	saddr.sin_family = AF_INET; // set to AF_INET
	saddr.sin_port = htons(serv_port); // Port number
	saddr.sin_addr.s_addr = inet_addr(argv[1]); // IP address eg "192.168.1.1"
	
	
	/*
	1. Connect to the server using proper API for connect
	2. Send data to connected server
	3. Receive data from connected server and print data received
	4. Close the connection
	*/
	if(connect(s,(struct sockaddr_in *)&saddr,sizeof(saddr))<0){
	perror("connect");
	close(s);
	exit(3);	
	}
	
	if(send(s,"nak warsi",strlen("nak warsi"),0)<0){
		perror("send");
		exit(4);	
	}
	char buf[20]={0};
	if(recv(s,buf,sizeof(buf),0)<0){
		perror("recv");
		close(5);
	}
	
	printf("data recieved: %s\n",buf);
	close(s);	
	
	return 0;
}
