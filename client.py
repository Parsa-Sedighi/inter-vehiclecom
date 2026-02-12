import socket

# REPLACE with the Server's Local IP (e.g., '192.168.1.15')
SERVER_IP = '192.168.0.250' 
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((SERVER_IP, PORT))
        # Receive the server's hello
        data = s.recv(1024)
        print(f"Received from server: {data.decode()}")
        
        # Send a hello back
        s.sendall(b"Hello from the Client!")
    except ConnectionRefusedError:
        print("Could not connect. Is the server running and the IP/Port correct?")