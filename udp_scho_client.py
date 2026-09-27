import socket

SERVER_IP = "127.0.0.1"  # Server IP (localhost)
SERVER_PORT = 12345      # Same port as server

def main():
    # Create UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"Connected to UDP Echo Server at {SERVER_IP}:{SERVER_PORT}")

    while True:
        msg = input("You: ")
        client_socket.sendto(msg.encode(), (SERVER_IP, SERVER_PORT))

        if msg.lower() == "exit":
            print("Closing connection...")
            break

        # Receive reply from server
        data, _ = client_socket.recvfrom(1024)
        print("Server:", data.decode())

    client_socket.close()

if __name__ == "__main__":
    main()
