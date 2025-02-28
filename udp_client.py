# Python socket library
from socket import *
server_name = '127.0.0.1'
server_port = 12000

# Create UDP socket for server
client_socket = socket(AF_INET, SOCK_DGRAM)

# Get user keyboard input
message = input("Input lowercase sentence:")

# Attach server name, port to message, send into socket
client_socket.sendto(message.encode(), (server_name, server_port))

# Read reply characters from socket into string
modified_message, server_address = client_socket.recvfrom(2048)

# Print out received string and close socket
print(modified_message.decode())
client_socket.close