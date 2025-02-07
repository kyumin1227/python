import socket
import threading

def handler_client(client_socket: socket.socket, client_address: tuple[str, int]) -> None:
    """클라이언트 마다 쓰레드를 통해 동작하는 함수"""
    while True:
        recv_data = client_socket.recv(1024).decode("utf-8")

        if not recv_data:
            print(f"[{client_address}]: 클라이언트의 연결이 종료 되었습니다.")
            break

        print(f"[{client_address}]: {recv_data}")
        client_socket.sendall(recv_data.encode("utf-8"))

    client_socket.close()

# 소켓 생성 (TCP or UDP, IP 주소 버전: v4 or v6)
# TCP: socket.SOCK_STREAM
# UDP: socket.SOCK_DGRAM
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind((ip 주소, port 주소))
server_socket.bind(("127.0.0.1", 5500))

# listen(큐의 개수)
server_socket.listen(5)

threading.Thread

while True:
    # accept(), 사용자로부터 연결 요청을 받았을 때 새로운 소켓 생성
    # blocking 함수
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handler_client, args=(client_socket, client_address))
    client_thread.start()
