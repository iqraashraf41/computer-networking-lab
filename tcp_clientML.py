
import socket

HOST =  "localhost"   # Server IP (use your server’s IP if remote)
PORT = 8080

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"TCP Server is running on {HOST}:{PORT}")
    max_messages = 5

    for i in range(max_messages):

        msg = input(f"You ({i+1}/{max_messages}): ")
        client_socket.send(msg.encode())

        if msg.lower() == "exit":
            print("Closing connection...")
            break

        data = client_socket.recv(1024).decode()
        print("Server:", data)

    print("Message limit reached or connection closed.")
    client_socket.close()

if __name__ == "__main__":
    main()
