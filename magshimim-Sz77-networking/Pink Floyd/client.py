import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 42069

VALID_LIST = ["1", "2", "3", "4", "5", "6", "7", "8"]

HEADER_DICT = {
    "1": "List of the albums: ",
    "2": "Songs in the album: ",
    "3": "Length of the song: ",
    "4": "Lyrics of the song: ",
    "5": "The song is in the album: ",
    "6": "The results for the search are: ",
    "7": "The results for the search are: ",
    "8": "",
    "0": "",
}

WELCOME = "0"

ALBUM_SEARCH = "2"
LEN = "3"
LYRICS = "4"
FIND_ALBUM = "5"
FIND_BY_NAME = "6"
FIND_BY_LYRIC = "7"
EXIT = "8"


def main():
    choice = 0
    request()  # Getting the server's welcome message, and printing it
    while choice != EXIT:
        choice = input(
            """
Choose an option:
1. Print all the albums.
2. Print the songs in album.
3. Print the length of a song.
4. Print the lyrics of a song.
5. Find the album of the song.
6. Find songs by name.
7. Find songs by lyrics.
8. Exit
Your choice: """
        )

        while not valid_check(choice):  # If the input is invalid
            choice = input("Try again (1-8): ")

        data = add_data(int(choice))
        choice = request(choice, data)


def valid_check(choice):
    """
    This function will check if the param 'choice' is valid (in range between 1-8)
    :param choice: The param that will be check for it's valid
    :return: True or false, if the input is valid or not
    """
    if choice not in VALID_LIST:
        return False

    return True


def request(header=WELCOME, data="DATA"):
    """
    This function will connect to the data server and send a request
    :param header: The header of the request (which action to do)
    :param data: The secondary information that will help the header (for example the name of the song and more)
    :return: The last chosen option by the user
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((SERVER_IP, SERVER_PORT))
        except socket.error:  # In case of trouble with the connection to the server
            print("ERROR: The server closed the connection!")
            return EXIT

        req = "^" + header + "~" + data

        # Sending the request
        sock.sendall(req.encode())

        server_ans = sock.recv(1024).decode()

        ans(header, server_ans[5:])

        return header


def ans(header, server_ans):
    """
    This function will turn the server's answer to more readable text, then print it
    :param header: The chosen operation number
    :param server_ans: The data that the server sent
    :return: NONE
    """
    msg = HEADER_DICT[header] + server_ans
    print(msg)


def add_data(choice):
    """
    This function will take input of a secondary data, if necessarily
    :param choice: The chosen option
    :return: The data
    """
    data = None
    choice = str(choice)

    if choice == ALBUM_SEARCH:  # In case of printing the songs in the album (case 2)
        data = input("Enter the name of the album: ")
    elif choice == LEN or choice == LYRICS or choice == FIND_ALBUM:  # In cases 3, 4, 5
        data = input("Enter the name of the song: ")
    elif choice == FIND_BY_LYRIC or choice == FIND_BY_NAME:  # In cases 6, 7
        data = input("Enter the text: ")
    else:
        data = "DATA"

    return data


if __name__ == "__main__":
    main()
