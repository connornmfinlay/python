import socket

def port_scan(target_host, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout value for the connection attempt
        sock.settimeout(1)
        # Connect to the target host and port
        result = sock.connect_ex((target_host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        # Close the socket connection
        sock.close()
    except socket.error:
        print(f"Could not connect to {target_host}")

# Define the target host and range of ports to scan
target_host = "127.0.0.1"  # Update with the desired target IP address or hostname
start_port = 1
end_port = 100  # Update with the desired range of ports to scan

# Perform the port scan
for port in range(start_port, end_port+1):
    port_scan(target_host, port)