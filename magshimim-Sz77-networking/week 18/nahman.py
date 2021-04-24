import requests

URL = "http://webisfun.cyber.org.il/nahman/files/file{}.nfo"
LETTER_TO_GET = 99
PATH = "words.txt"


def extract_password_from_site():
    """
    this function extracts the password from the files in the site
    :return:the password
    :rtype:str
    """
    password = ""
    for i in range(11, 35):
        url = URL.format(str(i))
        file = requests.get(url)
        password += file.text[LETTER_TO_GET]
    return password


def find_most_common_words(path, num_words_in_the_sentence):
    """
    this function finds the most common words in the and strings them together
    :param path: the path to the file
    :param num_words_in_the_sentence: how many words to string
    :type path:file
    :type num_words_in_the_sentence: int
    :return:the password
    :rtype:str
    """
    count = dict()
    password = ""

    with open(path, "r").read() as my_words:
        my_words.split()
        # the counting
        for word in my_words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
                # sorting by frequency
        count = sorted(count.items(), key=my_key, reverse=True)
        # string
        for i, value in enumerate(count):
            if i == num_words_in_the_sentence:
                break
            password += count[i][0] + " "
        password = password[:-1]  # removing the last spaces
        return password


def my_key(lst):
    """
    the key function for sorting returns the a last value in the list
    :param lst: the list
    :return: the thing to sort with
    """
    return lst[-1]


def main():
    password = ""
    option = int(input("enter the option you wish to use "))
    if option == 1:
        password = extract_password_from_site()

    elif option == 2:
        password = find_most_common_words(PATH, 6)

    print(password)


if __name__ == "__main__":
    main()
