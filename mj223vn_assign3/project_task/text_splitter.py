import os


def text_split(text):
    allowed = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ\n"
    temp = "".join(filter(allowed.__contains__, text))
    return temp


def read_file(file_path):
    """
    Reads a file and returning it as a str list

    :param file_path: path to file to read
    :return: file as a string
    :except IOError
    """
    text = ""
    try:
        with open(file_path, "r") as file:
            for line in file:
                text += text_split(line)
    except IOError as e:
        print(e)

    return text


def read_file_list(file_path):
    """
    Reads a file and returning it as a str list

    :param file_path: path to file to read
    :return: file as a list of type str
    :except IOError
    """
    lines = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                lines = line.split()
    except IOError as e:
        print(e)

    return lines


def write_file(str_list, file_path):
    """
    Takes a str list and write that list to a file

    :param str_list: list to write to file
    :param file_path: path to where the file will be saved
    :except IOError
    """
    try:
        print("write to file...")
        with open(file_path, "w") as file:
            for word in str_list:
                file.write(word + " ")
    except IOError as e:
        print(e)







path = os.getcwd() + "/eng_news_100K-sentences.txt"
path_w = os.getcwd() + "/eng_news_100K-sentences_list"

# text = read_file(path)
# text = text_split(text)
# text_list = text.split()
#
# write_file(text_list, path_w)

text = read_file_list(path_w)
print(len(text))
print(len(set(text)))



