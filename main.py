import socket

# Define the target host and port range
target_host = "localhost"
port_range = range(1, 1025)  # scan ports 1 to 1024

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Scan each port in the range
for port in port_range:
    # Attempt to connect to the port
    try:
        client.connect((target_host, port))
        print(f"Port {port} is open.")
    except:
        pass

# Close the socket
client.close()


