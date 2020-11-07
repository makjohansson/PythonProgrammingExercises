import os
"""
A python script used to print the number of times a letter [a-z] occurs in a text file and prints the 
result from the computation in the terminal as a histogram.
"""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def text_file_to_dict(path):
    """Return a dictionary in containing the amount of times a letter [a-z] occur in a a file
    and one dictionary containing the percentage each letter occur

    :parameter path: path to file
    :except IOError
    """
    try:
        with open(path) as file:
            text = file.read().lower()
            letter_dict = {letter: text.count(letter) for letter in letters}
            percentage_dict = {letter: round((letter_dict[letter] / sum(letter_dict.values()) * 100), 2)
                               for letter in letters}
            return letter_dict, percentage_dict
    except IOError as e:
        print(e)


def print_histogram(dct, divider=1):
    """Prints the amount of occurrences of each letter in a dictionary with the number of times a letter
    occurs represented by a star. By playing around with the value of the divider parameter different print results
    are achieved.

    :param divider: < num, less stars are printed
    :param dct: dictionary with values to print
    """
    for key in dct:
        print(key + " | ", end=" ")
        for star in range(dct[key] // divider):
            print("*", end="")
        print()


def print_result(path, divider=1):
    """Prints the result specific to the exercise 6

    :param divider: < num, less stars are printed
    :param path: path to file
    """
    letter_and_counts, letter_and_percentage = text_file_to_dict(path)
    print("\nReading from the file:", path)
    print("Total number of letters:", sum(letter_and_counts.values()))
    print(f"\nHistogram (where each star represents {divider} occurrences)")
    print_histogram(letter_and_counts, divider=divider)
    print_percentage = "".join([f"{key}: {value}%, " for key, value in letter_and_percentage.items()])
    return print_percentage


file_path_grail = os.getcwd() + "/large_texts/holy_grail.txt"
file_path_eng_news = os.getcwd() + "/large_texts/eng_news_100K-sentences.txt"

percentage_grail = print_result(file_path_grail, divider=30)
percentage_eng_news = print_result(file_path_eng_news, divider=8000)

# From the histogram I can see that the character frequency in the two files are very similar
# but just for fun I also print the percentage of each letter in the two files and this makes it very clear
# that the two files have a very similar character frequency.
print("\nPercentage for each letter in holy_grail: ", percentage_grail)
print("Percentage for each letter in eng_news  : ", percentage_eng_news)
