from socket import *

serverPort = 12000

# Create TCP welcoming socket
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort)) 

# Listen for incoming requests
serverSocket.listen(1)
print("The server is ready to receive")

# Loop forever
while True:
    # Sever waits on accept for incoming requests, new socket created on return
    connectionSocket, addr = serverSocket.accept()

    # Read bytes from socket (but not address as in UDP)
    message = connectionSocket.recv(1024).decode()
    capitalizedSentence = message.upper()
    connectionSocket.send(capitalizedSentence.encode())

    # Close connection to this client (but not the welcoming socket)
    connectionSocket.close()
