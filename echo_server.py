import socket

HOST = "0.0.0.0"   # Listen on all network interfaces
PORT = 12345       # Any available port above 1024

def main():
    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)  # Only one client at a time
    print(f"Echo Server is running on {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Client: {data}")

        if data.lower() == "exit":
            print("Client requested to close the connection.")
            break

        # Send back echoed message
        response = f"Echo: {data}"
        conn.send(response.encode())

    conn.close()
    server_socket.close()
    print("Server closed.")

if __name__ == "__main__":
    main()
