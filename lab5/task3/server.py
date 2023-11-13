import threading
import socket

ADDR = ("localhost", 5050)
FORMAT = "utf-8"
MAX_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def handle_client(conn: socket.socket, addr: tuple[str, int]):
    print(f"Connected: {addr}")

    with open("index.html", "r") as file:
        html_content = file.read()
    http_response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html_content
    conn.send(http_response.encode(FORMAT))
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
