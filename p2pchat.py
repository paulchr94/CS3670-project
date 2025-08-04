import socket

HOST = '127.0.0.1'  # change to peer's IP
PORT = 12345        # any unused port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
