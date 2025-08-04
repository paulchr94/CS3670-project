import socket

HOST = '127.0.0.1'  # change to peer's IP
PORT = 12345        # any unused port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_server():
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Peer:", data.decode())


def start_client():
    s.connect((HOST, PORT))
    while True:
        msg = input("You: ")
        s.sendall(msg.encode())
