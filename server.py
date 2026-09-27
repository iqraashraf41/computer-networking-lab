# DateTime UDP Server
import socket
import datetime

# 1. Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Bind server to IP & port
server_socket.bind(('localhost', 12345))
print("UDP Server is running and waiting for client request...")


while True:
    # 3. Receive message from client
    data, address = server_socket.recvfrom(1024)  # no accept() in UDP
    print("Received message from client:", data.decode())

        # 5. Get current date & time
    now = datetime.datetime.now().strftime("asslamoalaikum %Y-%m-%d %H:%M:%S")

  # 5. Send date and time back to client
    server_socket.sendto(now.encode(),address)

    
