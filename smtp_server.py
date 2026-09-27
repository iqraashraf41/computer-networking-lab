import socket
import threading

HOST = "0.0.0.0"
PORT = 1025

def handle_client(conn, addr):
    print(f"[+] Connected with {addr}")
    conn.send(b"220 Simple SMTP Server Ready\r\n")

    sender = ""
    recipient = ""
    is_data = False
    mail_body = []

    while True:
        data = conn.recv(1024).decode().strip()
        if not data:
            break

        print("CLIENT:", data)

        # SMTP commands
        if data.upper().startswith("HELO"):
            conn.send(b"250 Hello\r\n")

        elif data.upper().startswith("MAIL FROM:"):
            sender = data[10:].strip()
            conn.send(b"250 OK\r\n")

        elif data.upper().startswith("RCPT TO:"):
            recipient = data[8:].strip()
            conn.send(b"250 OK\r\n")

        elif data.upper() == "DATA":
            is_data = True
            conn.send(b"354 End with <CR><LF>.<CR><LF>\r\n")

        elif data == "." and is_data:
            is_data = False

            # Save email to file
            with open("mailbox.txt", "a") as f:
                f.write(f"From: {sender}\nTo: {recipient}\n")
                f.write("\n".join(mail_body))
                f.write("\n" + "-"*40 + "\n")

            conn.send(b"250 Message received\r\n")
            mail_body = []

        elif data.upper() == "QUIT":
            conn.send(b"221 Bye\r\n")
            break

        elif is_data:
            mail_body.append(data)

        else:
            conn.send(b"500 Command not recognized\r\n")

    conn.close()
    print(f"[-] Connection closed with {addr}")

def main():
    print(f"SMTP Server Running on {HOST}:{PORT}")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()
