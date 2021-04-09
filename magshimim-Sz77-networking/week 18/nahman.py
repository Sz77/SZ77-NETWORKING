import requests


def extract_password_from_site():
    """
    this function extracts the password from the files in the site
    :return:the password
    :rtype:str
    """
    password = ''
    for i in range(11, 35):
        url = "http://webisfun.cyber.org.il/nahman/files/file{}.nfo".format(str(i))
        file = requests.get(url)
        password += file.text[99]
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
    password = ''
    my_words = (open(path, "r").read().split())
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
        password += count[i][0] + ' '
    password = password[:-1]  # removing the last spaces
    return password


def my_key(lst):
    """
    the key function for sorting
    :param lst: the list
    :return: the thing to sort with
    """
    return lst[-1]


def main():
    option = int(input("enter the option you wish to use "))
    if option == 1:
        password = extract_password_from_site()
        print(password)
    elif option == 2:
        password = find_most_common_words("words.txt", 6)
        print(password)


if __name__ == "__main__":
    main()
