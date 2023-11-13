import threading
import socket

ADDR = ("localhost", 5050)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT"
MAX_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients: set[socket.socket] = set()


def handle_client(conn: socket.socket, addr: tuple[str, int]):
    print(f"Connected: {addr}")

    connected = True
    while connected:
        msg = conn.recv(MAX_SIZE).decode(FORMAT)
        if not msg:
            break

        if msg == DISCONNECT_MESSAGE:
            connected = False

        for client in clients:
            client.sendall(f"From {addr[-1]}: {msg}".encode(FORMAT))

        print(f"[{addr}] {msg}")

    conn.close()


def start():
    print("Starting server...")
    server.bind(ADDR)
    server.listen()
    while True:
        conn, addr = server.accept()
        clients.add(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    start()
