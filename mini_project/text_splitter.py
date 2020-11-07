import os


def text_split(text):
    """Filters out everything that is not in the allowd string
    Allowed string = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ\n"

    :param text: a string
    :return: Filtered string
    """
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
    
    text = text_split(text)
    text_list = text.split()

    return text_list


def get_text_as_word_list(file_path):
    """
    Reads a file and returning it as a str list
    with "a" and "I" counting as words

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


def to_lower_and_removing_letters(lines):
    """ 
    words to lower case and removing words of length 1 except "a" and "I"
    :param lines: string list
    :return: string list with no duplicates and "a" and "i" as a word 
    """
    temp = [word.lower() for word in lines]
    temp_ = [word for word in temp if len(word) > 1 or (len(word) == 1 and (word == "a" or word == "i"))]

    return temp_

def write_file(str_list, file_path):
    """
    Takes a str list and write that list to a file

    :param str_list: list to write to file
    :param file_path: path to where the file will be saved
    :except IOError
    """
    temp = to_lower_and_removing_letters(str_list)
    try:
        print("write to file...")
        with open(file_path, "w") as file:
            for word in temp:
                file.write(word + " ")
    except IOError as e:
        print(e)

# Paths to read and write holy_grail.txt
# path = os.getcwd() + "/holy_grail.txt"
# path_w = os.getcwd() + "/holy_grail_list.txt"
# text_list = read_file(path)
# write_file(text_list, path_w)

# # Path to read and write eng_news_100K
# path = os.getcwd() + "/eng_news_100K-sentences.txt"
# path_w = os.getcwd() + "/eng_news_100K-sentences_list.txt"
# text_list = read_file(path)
# write_file(text_list, path_w)











