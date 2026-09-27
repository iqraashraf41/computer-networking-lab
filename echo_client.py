import socket

HOST = "127.0.0.1"  # Server IP (use same IP as server)
PORT = 12345        # Same port as server

def main():
    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"Connected to Echo Server at {HOST}:{PORT}")

    while True:
        msg = input("You: ")
        client_socket.send(msg.encode())

        if msg.lower() == "exit":
            print("Closing connection...")
            break

        # Receive echoed message
        data = client_socket.recv(1024).decode()
        print("Server:", data)

    client_socket.close()

if __name__ == "__main__":
    main()
