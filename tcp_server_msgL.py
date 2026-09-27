
import socket

HOST = "10.75.51.99"  # Listen on all network interfaces
PORT = 8080        # Port number

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"TCP Server is running on {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    print(f"🔗 Connected with {addr}")

    message_limit = 5
    count = 0

    while count < message_limit:
        data = conn.recv(1024).decode()
        if not data:
            break

        count += 1
        print(f"Client ({count}/{message_limit}): {data}")

        if data.lower() == "exit":
            print("Client requested to close connection.")
            break

        response = f"Echo: {data}"
#current dtae and time
now=datetime.datetime.now().strftime(" %Y-%m-%d %H:%M:%S")

        conn.send(response.encode(),now.encode())

    print("Message limit reached or connection closed.")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()
