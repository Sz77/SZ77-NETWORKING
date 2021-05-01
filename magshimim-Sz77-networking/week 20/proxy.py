import socket

FILM4ME_IP = "54.71.128.194"
FILM4ME_PORT = 92
SERVER_IP = "127.0.0.1"
SERVER_PORT = 9090


def main():

    client()


def client():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listening_sock:
            listening_sock.bind((SERVER_IP, SERVER_PORT))
            listening_sock.listen(1)
            client_soc, client_address = listening_sock.accept()
            with client_soc:
                client_msg = client_soc.recv(1024)
                client_msg = client_msg.decode()
                print(client_msg)
                client_soc.sendall(proxy_server(client_msg).encode())


def proxy_server(client_msg):
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        server_address = (FILM4ME_IP, FILM4ME_PORT)
        sock.connect(server_address)
        sock.sendall(client_msg.encode())
        msg = sock.recv(1024)
        msg = msg.decode()
        print(msg)
        msg = fix_msg(msg)
        print(msg)
        return msg


def fix_msg(msg):
    msg = fix_image(msg)
    msg = html_error(msg)
    msg = ban(msg)
    return msg


def fix_image(msg):
    if "jpg" in msg:
        msg = msg[: msg.index("jpg")] + ".jpg" + msg[msg.index('"&id') :]
    return msg


def html_error(msg):
    if "SERVERERROR" in msg:
        msg = "ERROR" + msg[msg.index("#") :]
    return msg


def ban(msg):
    if "France" in msg:
        msg = 'ERROR#"France is banned!"'
    return msg


if __name__ == "__main__":
    main()
