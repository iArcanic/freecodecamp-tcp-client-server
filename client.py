import socket

# Create the client socket object
client_socket = socket.socket(
    socket.AF_INET, # Using IPv4
    socket.SOCK_STREAM # Connection based protocol
)

# IP address of the host
host = socket.gethostname()

# Port to listen on
port = 444

# Connecting to the defined host and port
client_socket.connect((host, port))

# Recieve the incoming data with a max buffer size
message = client_socket.recv(1024)

# # Close the TCP connection
client_socket.close()

print(message.decode('ascii'))
