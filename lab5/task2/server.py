import math
import threading
import socket

ADDR = ("localhost", 5050)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT"
MAX_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def pythagorean_theorem(a: int, b: int):
    return math.sqrt(a**2 + b**2)


def get_input(msg: str) -> tuple[int, int]:
    a, b = (int(item) for item in msg.split(","))
    return a, b


def handle_client(conn: socket.socket, addr: tuple[str, int]):
    print(f"Connected: {addr}")

    connected = True
    while connected:
        msg = conn.recv(MAX_SIZE).decode(FORMAT)
        if not msg:
            break
        try:
            a, b = get_input(msg)
            conn.send(
                f"{a=}, {b=} => c={pythagorean_theorem(a, b):.2f}".encode(FORMAT)
            )
        except ValueError:
            conn.send(f"'{msg}' is a wrong input.".encode(FORMAT))

        if msg == DISCONNECT_MESSAGE:
            connected = False

        print(f"[{addr}] {msg}")

    conn.close()


def start():
    print("Starting server...")
    server.bind(ADDR)
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    start()
