#include <iostream>
#include <cstring>
#include <string>
#include <stdexcept>

#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
using namespace std;

mutex m;


int create_server_socket(string protocol, int port)
{
	int server_socket;
	if (protocol == "tcp")
		server_socket = socket(AF_INET, SOCK_STREAM, 0);
	else if (protocol == "udp")
		server_socket = socket(AF_INET, SOCK_DGRAM, 0);
	else
    	throw invalid_argument("Unsupported protocol: " + protocol);
    
    if (server_socket < 0)
        throw runtime_error("Socket creation failed");
	sockaddr_in serverAddress;
	serverAddress.sin_family = AF_INET;
	serverAddress.sin_port = htons(port);
	serverAddress.sin_addr.s_addr = INADDR_ANY;
	bind(server_socket, (struct sockaddr*)&serverAddress, sizeof(serverAddress));
	if (bind(server_socket, (struct sockaddr*)&serverAddress, sizeof(serverAddress)) < 0) {
        close(server_socket);
        throw runtime_error("Bind failed");
    }
	return server_socket;
}
