import socket

# Create the server socket object
server_socket = socket.socket(
    socket.AF_INET, # Using IPv4
    socket.SOCK_STREAM # Connection based protocol
)

# IP address of the host
host = socket.gethostname()

# Port to listen on
port = 444

# Bind the host and port to the socket object
server_socket.bind((host, port))

# Number of requests allowed at a given time
server_socket.listen(3)

while True:
    # Allow incoming TCP connections from the client
    client_socket, address = server_socket.accept()

    # Console logging
    print(f"Recieved connection from ${address}")

    # Welcome message upon connecting to the TCP server
    message = "Hello! Thank you for connecting to the server" + "\r\n"

    # Send the welcome message encoded to the client
    client_socket.send(message.encode('ascii'))

    # Close the TCP connection
    client_socket.close()
