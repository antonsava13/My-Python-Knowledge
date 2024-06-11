import random


# ------- Helper functions -------
def generate_matrix_with_random_numbers(I: int, J: int) -> list:
    """Gvien I - the number of rows and J - the length of each row, create a matrix with random numbers

    Args:
        I (int): _description_
        J (int): _description_

    Returns:
        matrix: list of lists
    """
    matrix = []
    for i in range(I):
        row = []
        for j in range(J):
            random_number = random.randint(0, 9)
            row.append(random_number)
        matrix.append(row)
    return matrix



# ------- Exercise 1.3 -------
def replace_spaces(input: str, length: int = 0):

    """Exercise 1.3 - URLify"""

    if length == 0:
        output = ""
        for char in input:
            if char == " ":
                output += "%20"
            else:
                output += char

    else:
        # This is not very efficient way of doing things since:
        # - Converting string to list takes O(n)
        # - Calculating len(input) probably takes O(n)
        # - Converting string to list also takes O(n)
        start_replasing_spaces = False
        move_to_poition = len(input)-1

        input_list = list(input)

        for i in reversed(range(len(input_list))):
            # First few characters will be spaces
            # Find first non-space character
            if input_list[i] != " " and not start_replasing_spaces:
                start_replasing_spaces = True

            if start_replasing_spaces:
                if input_list[i] != " ":
                    input_list[move_to_poition] = input_list[i]
                    move_to_poition -= 1
                else:
                    for j in "02%":
                        input_list[move_to_poition] = j
                        move_to_poition -=1

        output = "".join(input_list)

    return output


# ------- Exercise 1.4 -------
def is_string_palindrome_permutation(string):

    from collections import Counter

    """ Exercise 1.4 - Palindrome Permutation"""

    # If string is palindrome there can be to cases:
    # 1. If the length is even - the frequency of each letter is even
    # 2. If the length is odd - one letter will have and odd frequency
    #    and the rest will have even frequencies

    string_length = len(string)

    counter = Counter(string)
    del counter[" "]

    if string_length % 2 == 0:
        # string length is even - the frequency of each letter is even

        for key in counter:
            if counter[key] % 2 != 0:
                return False
        return True

    else:
        # string length is odd - one letter will have and odd frequency
        # and the rest will have even frequencies

        has_single_odd_frequency = False

        for key in counter:

            # print(f"going throug: {key}: fr: {counter[key]}")
            if counter[key] % 2 != 0:
                if has_single_odd_frequency:
                    # We can get here only in the case were one character with odd fequency was already found and we have found a second one
                    return False
                else:
                    has_single_odd_frequency = True

        return True


# ------- Exercise 1.5 -------
def one_away(str_1, str_2):
    """
    There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
    EXAMPLE
    pale, ple -> true
    pales, pale -> true
    pale, bale -> true
    pale, bake -> false
    """
    length_differnece = len(str_1) - len(str_2)
    if length_differnece == 0:
        # Same lenght, check for character replacement
        # All but one letter will be in place
        no_of_different_letters = 0
        for position, l in enumerate(str_1):
            if l != str_2[position]:
                no_of_different_letters += 1
        if no_of_different_letters <= 1:
            return True
        else:
            return False

    elif length_differnece == -1: # Possibly a character was inserted to str_1

        found_inserted_letter = False
        for position, l in enumerate(str_1):

            if l != str_2[position] and not found_inserted_letter:
                found_inserted_letter = True

            if found_inserted_letter:
                position += 1

            if l != str_2[position] and found_inserted_letter:
                return False

        return True

    elif length_differnece == 1: # Possible a character was removed from str_1

        found_inserted_letter = False
        for position, l in enumerate(str_2):

            if l != str_1[position] and not found_inserted_letter:
                found_inserted_letter = True

            if found_inserted_letter:
                position += 1

            if l != str_1[position] and found_inserted_letter:
                return False

        return True

# ------- Exercise 1.6 -------
def string_compression(string):
    """
    String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).
    """
    i = 0
    compressed_string = ""
    buffer = ""
    while i < len(string):

        if len(buffer) == 0:
            buffer += string[i]

        else:
            if string[i] == buffer[0]:
                buffer += string[i]
            else:
                compressed_string += buffer[0]
                compressed_string += str(len(buffer))
                buffer = string[i]

        i += 1
    compressed_string += buffer[0]
    compressed_string += str(len(buffer))

    if len(compressed_string) < len(string):
        return compressed_string
    else:
        return string


# ------- Exercise 1.7 -------
def rotate_matrix(matrix):
    """
    Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
    """
    # Find avarage row lenth
    sum_of_row_lengths = 0
    no_of_columns = len(matrix)

    for row in matrix:
        sum_of_row_lengths += len(row)

    # Check if all length of each row is the same the number of columns
    if sum_of_row_lengths % no_of_columns != 0:
        return "This is not a matrix"

    else:
        end = len(matrix) - 1
        center = int(no_of_columns/2)
        for i in range(center):
            for j in range(i, no_of_columns - 1 - i):
                matrix[i][j], matrix[j][end-i], matrix[end-i][end-j], matrix[end-j][i] = matrix[end-j][i], matrix[i][j], matrix[j][end-i], matrix[end-i][end-j]
        return matrix

# ------- Exercise 1.8 -------
def zero_matrix(matrix):
    """
    Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
    """
    # Get matrix dimentions
    I = len(matrix)
    J = len(matrix[0])

    # Find the positions of all zero eliments
    rows_with_zeroes = []
    columns_with_zero = []

    for i in range(I):
        for j, el in enumerate(matrix[i]):
            if el == 0:
                if i not in rows_with_zeroes:
                    rows_with_zeroes.append(i)
                if j not in columns_with_zero:
                    columns_with_zero.append(j)

    # Change rows and collums with zeroes to be all zeroes
    for i in range(I):
        for j in range(J):
            if i in rows_with_zeroes:
                matrix[i][j] = 0
            elif j in columns_with_zero:
                matrix[i][j] = 0
    return matrix


if __name__ == "__main__":

    pass
