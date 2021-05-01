import socket
import datetime

SERVER_IP = "34.218.16.79"
SERVER_PORT = 77


def main():
    city_name = input("enter the full city name ")
    option = int(
        input("enter the option \n (1 - today's weather \n 2 -full 4 day broadcast) ")
    )
    if option == 1:
        today_weather(city_name)
    if option == 2:
        full_broadcast(city_name)


def today_weather(city_name):
    """
    this function prints today's weather
    :param city_name: the city to check
    :type city_name: str
    :return: none
    """
    output = (
        datetime.date.today().strftime("%d/%m/%Y")
        + "Temperature: "
        + "{}".format(
            get_weather(city_name, datetime.date.today().strftime("%d/%m/%Y"))
        )
    )
    print(output)


def full_broadcast(city_name):
    """
    this function prints the weather for today and 3 more days.
    :param city_name: the city to check
    :type city_name: str
    :return: none
    """
    today_weather(city_name)
    for i in range(1, 4):
        output = (
            (datetime.date.today() + datetime.timedelta(days=i)).strftime("%d/%m/%Y")
            + "Temperature: "
            + "{}".format(
                get_weather(
                    city_name,
                    (datetime.date.today() + datetime.timedelta(days=i)).strftime(
                        "%d/%m/%Y"
                    ),
                )
            )
        )
        print(output)


def get_weather(city_name, date):
    """
    this function talks to the weather server and gets the weather data
    :param city_name: the city to check
    :type city_name: str
    :param date: the date to check
    :type date:str
    :return: the weather data
    :rtype:tuple
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        server = (SERVER_IP, SERVER_PORT)
        sock.connect(server)

        sock.recv(1024)

        msg = "100:REQUEST:city={}&date={}&checksum={}".format(
            city_name, date, checksum(city_name, date)
        )
        sock.sendall(msg.encode())
        server_msg = sock.recv(1024)
        server_msg = server_msg.decode()
        if "500" not in server_msg:
            output = server_msg[server_msg.index("temp=") + 5 :].split("&")
            output[1] = output[1][5:]
            (tuple(output))
        else:
            output = (
                999,
                server_msg[server_msg.find("500:ERROR:") + len("500:ERROR:") : -1],
            )
        return output


def checksum(city_name, date):
    """
    this function return the checksum for a given city and date
    :type city_name: str
    :param date: the date to check
    :type date:str
    :return: the weather data
    :return: the checksum
    :rtype:str
    """
    second_part = 0
    first_part = sum(ord(c) - ord("a") + 1 for c in city_name.lower())
    date = date.split("/")
    for i in date:
        for j in i:
            second_part += int(j)
    return "{}.{}".format(first_part, second_part)


if __name__ == "__main__":
    main()
