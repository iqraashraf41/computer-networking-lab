# udp_client_limited.py
import socket

HOST = "127.0.0.1"  # Server IP
PORT = 12345        

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f" Connected to UDP Server at {HOST}:{PORT}")

    max_messages = 5

    for i in range(max_messages):
        msg = input(f"You ({i+1}/{max_messages}): ")
        client_socket.sendto(msg.encode(), (HOST, PORT))

        if msg.lower() == "exit":
            print("Closing connection...")
            break

        data, _ = client_socket.recvfrom(1024)
        print("Server:", data.decode())

    print("Message limit reached or connection closed.")
    client_socket.close()

if __name__ == "__main__":
    main()
