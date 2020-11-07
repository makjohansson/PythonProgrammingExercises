class integer_file_to_list:
    """
    A class used to read the .txt files "10000_integers/file_10000integers_A" and
    10000_integers/file_10000integers_B and returning the integers from the text files as
    a list of integers
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def file_to_int_list(self):
        """
        Reads and return integers from the two text files

        :return: list of integers
        """
        int_list = []
        try:
            with open(self.file_path, "r") as (file):
                for line in file:
                    the_line = line.strip().split(", ") if file.name.endswith("A.txt") else line.strip().split(":")
                    for number in the_line:
                        int_list.append(int(number))
            return int_list
        except IOError as e:
            print(e)
