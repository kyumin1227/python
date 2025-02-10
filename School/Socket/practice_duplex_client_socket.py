import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

is_activate = [True]

def handler_tx():
    while is_activate[0]:
        send_msg = input("> ")

        if send_msg.lower() == "quit":
            break

        client_socket.sendall(send_msg.encode("utf-8"))
    
    client_socket.close()
    is_activate[0] = False

def handler_rx():
    while is_activate[0]:
        recv_msg = client_socket.recv(1024).decode("utf-8")
        
        if not recv_msg:
            break

        print(f"Response: {recv_msg}")

    client_socket.close()
    is_activate[0] = False

thread_tx = threading.Thread(target=handler_tx)
thread_rx = threading.Thread(target=handler_rx)

thread_tx.start()
thread_rx.start()

thread_tx.join()
thread_rx.join()
