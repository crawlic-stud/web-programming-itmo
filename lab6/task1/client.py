import socket

from server import ADDR, FORMAT, MAX_SIZE


def send(client: socket.socket, msg: str):
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    send(client, "hello, server!")
    while True:
        response = client.recv(MAX_SIZE).decode(FORMAT)
        print(f"Response from server: {response}")
        q = input("Press q to quit: ")
        if q == "q":
            break

    client.close()


if __name__ == "__main__":
    start()
