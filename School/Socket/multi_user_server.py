import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

client_list = list()
client_list_lock = threading.Lock()

def handler_client(client_socket:socket.socket, client_address):
    try:
        with client_list_lock:
            client_list.append(client_socket)
            print

        while True:
            recv_msg = client_socket.recv(1024).decode("utf-8")

            if not recv_msg:
                print(f"클라이언트 종료 요청: {client_address}")
                break

            send_msg = f"[{client_address}] {recv_msg}"

            with client_list_lock:
                for other_client in client_list:
                    if client_socket != other_client:
                        try:
                            other_client.sendall(send_msg.encode("utf-8"))

                        except:
                            print(f"메시지 전송 오류 발생: {client_address}")
                            raise

    finally:
        with client_list_lock:
            if client_list in client_socket:
                client_list.remove(client_socket)
        client_socket.close()
        print(f"클라이언트 연결 종료: {client_address}")

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handler_client, args=(client_socket, client_address), daemon=True)
            client_thread.start()

        except {socket.error, OSError} as e:
            print(f"클라이언트 연결 오류 발생: {e}")

except Exception as e:
    print(f"서버 실행 중 오류 발생: {e}")

finally:
    server_socket.close()
    print("서버 종료")
