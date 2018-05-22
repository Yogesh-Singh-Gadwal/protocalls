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
	
	int s= socket(PF_INET,SOCK_DGRAM,0);
	if(s<0){
		perror("socket");
		exit(2);	
	}

	struct sockaddr_in saddr = {0};
	saddr.sin_family = AF_INET; // set to AF_INET
	saddr.sin_port = htons(serv_port); // Port number
	saddr.sin_addr.s_addr = inet_addr(argv[1]); // IP address eg "192.168.1.1"
	
	char buf[30]={0};

	if (sendto(s,"nakwarsi", strlen("nakwarsi"), 0, (struct sockaddr_in *)&saddr, sizeof(saddr)) < 0) { 
	perror("sendto failed"); 
	return 0; }
	
	recvfrom(s, buf, sizeof(buf), 0, (struct sockaddr *)&saddr,sizeof(saddr));
	
	close(s);

	return 0;
}
