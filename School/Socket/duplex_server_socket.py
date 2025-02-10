import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen(5)

is_active = [True]

def handler_tx(client_socket:socket.socket, client_address):
    while is_active[0]:
        send_msg = input(f"[{client_address}]: ")

        if send_msg.lower() == "exit":
            client_socket.close()
            is_active[0] = False
            break

        client_socket.sendall(send_msg.encode("utf-8"))

def handler_rx(client_socket:socket.socket, client_address):
    while is_active[0]:
        recv_msg = client_socket.recv(1024).decode("utf-8")

        if not recv_msg:
            break

        print(f"[{client_address}]: {recv_msg}")

    is_active[0] = False
    client_socket.close()

while True:
    client_socket, client_address = server_socket.accept()

    thread_tx = threading.Thread(target=handler_tx, args=(client_socket, client_address))
    thread_rx = threading.Thread(target=handler_rx, args=(client_socket, client_address))

    thread_tx.start()
    thread_rx.start()
