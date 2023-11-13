import socket

from server import ADDR, FORMAT, DISCONNECT_MESSAGE, MAX_SIZE


def send(client: socket.socket, msg: str):
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    while True:
        msg = input("Input (q - quit): ")
        if msg == "q":
            break
        send(client, msg)

    send(client, DISCONNECT_MESSAGE)
    print("Disconnected.")


if __name__ == "__main__":
    start()
