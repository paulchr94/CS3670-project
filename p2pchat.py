import socket
import ssl
import threading


def start_server(host='127.0.0.1', port=8443):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="peer_cert.pem", keyfile="peer_key.pem")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"[*] Server listening on {host}:{port}")

    client_socket, addr = server_socket.accept()
    ssl_socket = context.wrap_socket(client_socket, server_side=True)
    print(f"[+] Connection from {addr}")

    while True:
        try:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Peer:", data.decode())
        except:
            break
    ssl_socket.close()
    server_socket.close()


def start_client(host='127.0.0.1', port=8443):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE  # For self-signed certs (use CERT_REQUIRED for real verification)

    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_socket = context.wrap_socket(raw_socket, server_hostname=host)

    ssl_socket.connect((host, port))
    print(f"[+] Connected securely to {host}:{port}")

    while True:
        msg = input("You: ")
        ssl_socket.send(msg.encode())


if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server)
    client_thread = threading.Thread(target=start_client)

    server_thread.start()
    client_thread.start()

    server_thread.join()
    client_thread.join()
