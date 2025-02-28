from socket import *
server_port = 12000

# Create UDP socket
server_socket = socket(AF_INET, SOCK_DGRAM)

# Bind socket to local port number 12000
server_socket.bind(('', server_port))
print("The server is ready to recieve")

# Loop forever
while True:
    # Read from UDP socket into message, getting clients address (client IP and port)
    message, client_address = server_socket.recvfrom(2048)
    modified_message = message.decode().upper()

    # Send upper case string back to this client
    server_socket.sendto(modified_message.encode(), client_address)