import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen(5)

connect_client = set()

def handler_tx(client_socket:socket.socket, client_address):
    while client_address in connect_client:
        send_msg = input("> ")

        if send_msg.lower() == "quit":
            break

        client_socket.sendall(send_msg.encode("utf-8"))
    
    client_socket.close()
    connect_client.remove(client_address)

def handler_rx(client_socket:socket.socket, client_address):
    while client_address in connect_client:
        recv_msg = client_socket.recv(1024).decode("utf-8")
        
        if not recv_msg:
            break

        print(f"Response: {recv_msg}")

    client_socket.close()
    connect_client.remove(client_address)

def send_msg():
    pass

while True:
    client_socket, client_address = server_socket.accept()

    connect_client.add(client_address)

    thread_tx = threading.Thread(target=handler_tx, args=(client_socket, client_address))
    thread_rx = threading.Thread(target=handler_rx, args=(client_socket, client_address))

    thread_tx.start()
    thread_rx.start()
