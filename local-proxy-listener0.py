import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(4096)
        if len(data) == 0:
            break
        print(f"Received: {data.decode('utf-8')}")

def proxy_listener(bind_host, bind_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_host, bind_port))
    server.listen(5)

    print(f"[*] Listening on {bind_host}:{bind_port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

def main():
    bind_host = "127.0.0.1"
    bind_port = 8088

    proxy_listener(bind_host, bind_port)

if __name__ == "__main__":
    main()
