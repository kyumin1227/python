import socket

# 소켓 생성 (TCP or UDP, IP 주소 버전: v4 or v6)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect (서버 주소, 서버 포트)
client_socket.connect(("127.0.0.1", 5500))
while True:
    send_msg = input("> ")

    if send_msg == "Q":
        break

    client_socket.sendall(send_msg.encode("utf-8"))
    print(client_socket.recv(1024).decode("utf-8"))

print("종료 요청")
client_socket.close()