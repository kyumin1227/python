import socket

# 소켓 생성 (TCP or UDP, IP 주소 버전: v4 or v6)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect (서버 주소, 서버 포트)
client_socket.connect(("127.0.0.1", 5500))