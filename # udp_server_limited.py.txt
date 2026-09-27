# udp_server_limited.py
import socket

HOST = "0.0.0.0"  
PORT = 12345      

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    print(f" UDP Server running on {HOST}:{PORT}")

    message_limit = 5
    count = 0

    while count < message_limit:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()
        count += 1

        print(f"Message {count}/{message_limit} from {addr}: {message}")

        if message.lower() == "exit":
            print("Client requested to close connection.")
            break

        response = f"Echo: {message}"
        server_socket.sendto(response.encode(), addr)

    print("Message limit reached or connection closed.")
    server_socket.close()

if __name__ == "__main__":
    main()
