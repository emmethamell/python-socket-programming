from socket import *

server_name = '127.0.0.1'
server_port = 12000

# Create TCP socket for server, remote port 12000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

message = input("Input lowercase sentence: ")
client_socket.send(message.encode())

# No need to attach server name or port
modified_message = client_socket.recv(1024)
print("From server: ", modified_message.decode())
client_socket.close()