import socket

# Use '0.0.0.0' to listen on all available network interfaces
HOST = '192.168.0.250'  
PORT = 65432      # Non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server is listening on port {PORT}...")
    
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        # Send a greeting message
        conn.sendall(b"Hello from the Server!")
        
        # Receive a response
        data = conn.recv(1024)
        print(f"Received from client: {data.decode()}")