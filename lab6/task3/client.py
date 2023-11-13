import socket

from server import ADDR, FORMAT, MAX_SIZE


def start():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    response = client.recv(MAX_SIZE).decode(FORMAT)
    print(response)
    print("Disconnected.")


if __name__ == "__main__":
    start()
