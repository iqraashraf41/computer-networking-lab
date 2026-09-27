# DateTime UDP Client
import socket
import time

# 1. Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Define server IP and port
server_address = ('localhost', 12345)

# 3. Send request to server
start_time=time.time()
message = "Requesting date and time"
client_socket.sendto(message.encode(), server_address)

# 4. Receive response from server
data, server = client_socket.recvfrom(1024)
end_time=time.time()
rtt=(end_time-start_time)*1000
# 5. Display received date and time
print("Current Date & Time from Server:",data.decode())
print(f"round trip time RTT:{rtt:.2f}ms")

# 6. Close socket
client_socket.close()