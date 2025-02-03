import socket

# 소켓 생성 (TCP or UDP, IP 주소 버전: v4 or v6)
# TCP: socket.SOCK_STREAM
# UDP: socket.SOCK_DGRAM
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind((ip 주소, port 주소))
server_socket.bind(("127.0.0.1", 5500))

# listen(큐의 개수)
server_socket.listen(5)

# accept(), 사용자로부터 연결 요청을 받았을 때 새로운 소켓 생성
# blocking 함수
server_socket.accept()

print("Hello")