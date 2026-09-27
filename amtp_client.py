import socket

SERVER_IP = "127.0.0.1"   # Replace with your PC IP if using two computers
PORT = 1025

def recv(sock):
    print("SERVER:", sock.recv(1024).decode(), end="")

def send(sock, msg):
    print("CLIENT:", msg)
    sock.send((msg + "\r\n").encode())

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_IP, PORT))

    recv(sock)   # Server greeting

    send(sock, "HELO client")
    recv(sock)

    send(sock, "MAIL FROM:<iqraashraf841@gmail.com>")
    recv(sock)

    send(sock, "RCPT TO:<iqra624@gamil.com>")
    recv(sock)

    send(sock, "DATA")
    recv(sock)

    send(sock, "This is a test mail.")
    send(sock, "Hello from client!")
    send(sock, ".")     # End message
    recv(sock)

    send(sock, "QUIT")
    recv(sock)

    sock.close()
    print("\nConnection closed.")

if __name__ == "__main__":
    main()
