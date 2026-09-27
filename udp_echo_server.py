import socket

HOST = "0.0.0.0"   # Listen on all interfaces
PORT = 12345       # Same port for server

def main():
    # Create UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    print(f"UDP Echo Server running on {HOST}:{PORT}")

    while True:
        # Receive data from client
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()
        print(f"Received from {addr}: {message}")

        # Exit condition
        if message.lower() == "exit":
            print(f"Client {addr} requested to close connection.")
            break

        # Echo message back
        response = f"Echo: {message}"
        server_socket.sendto(response.encode(), addr)

    server_socket.close()
    print("Server closed.")

if __name__ == "__main__":
    main()
