import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 42069

WELCOME_REQ = "0"
WELCOME_MSG = "^res~Welcome!"

ALBUM_LIST_REQ = "1"
SONGS_IN_ALBUM_REQ = "2"
LEN_REQ = "3"
LYRIC_REQ = "4"
FIND_ALBUM_REQ = "5"
SEARCH_BY_NAME_REQ = "6"
SEARCH_BY_LYRIC_REQ = "7"
EXIT_REQ = "8"

EXIT_RES = "Goodbye!"

# Temporary
NONE = "NONE"
NONE_LIST = ["NONE", "NONE"]
LEN = "0:00"
LYRIC = "NONE"


def main():
    header = 0
    welcome = True

    while header != "8":  # Closing the connection if the user will enter '8'
        header = connect(welcome)
        welcome = False


def connect(welcome_check):
    """
    This function will connect with the client, and answer his request
    :param welcome_check: If true, the function will send a welcome message
    :return: The last chosen option by the client
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((SERVER_IP, SERVER_PORT))
        sock.listen(1)

        client_sock, client_addr = sock.accept()

        if welcome_check:
            client_sock.sendall(WELCOME_MSG.encode())
            return None

        client_msg = client_sock.recv(1024).decode()
        print(client_msg)

        data = ans(client_msg[1], client_msg[3:])

        res = "^" + "res" + "~" + data

        client_sock.sendall(res.encode())

        return client_msg[1]


def find_album():
    # todo do the real search from data.py
    return NONE


def find_lyrics():
    # todo do the real search from data.py
    return LYRIC


def find_len():
    # todo do the real search from data.py
    return LEN


def find_songs_in_albums():
    # todo do the real search from data.py
    return NONE_LIST


def get_albums():
    # todo do the real search from data.py
    return NONE_LIST


def songs_by_name():
    # todo do the real search from data.py
    return NONE_LIST


def search_by_lyrics():
    # todo do the real search from data.py
    return NONE_LIST


def ans(header, data):
    """
    This function will prepare the information that we will send back to the client
    :param header: The option that the client had chosen
    :param data:  The extra information, only if needed (For example - a name of a song)
    :return: the header and the data of the response
    """
    msg = ""

    if header == ALBUM_LIST_REQ:  # All the albums
        msg = ", ".join(get_albums())
    elif header == SONGS_IN_ALBUM_REQ:  # All the songs in an album
        msg = ", ".join(find_songs_in_albums())

    elif header == LEN_REQ:  # Length of a song
        msg = find_len()

    elif header == LYRIC_REQ:  # Lyrics of a song
        msg = find_lyrics()

    elif header == FIND_ALBUM_REQ:  # Album of a song
        msg = find_album()

    elif header == SEARCH_BY_NAME_REQ:  # Search by name
        msg = ", ".join(songs_by_name())

    elif header == SEARCH_BY_LYRIC_REQ:  # Search by lyrics
        msg = ", ".join(search_by_lyrics())

    elif header == EXIT_REQ:  # Exit
        msg = EXIT_RES

    return msg


if __name__ == "__main__":
    main()
