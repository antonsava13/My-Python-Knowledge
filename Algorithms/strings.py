def convert_char_to_ord(char):
 return ord(char)

def convert_ord_to_char(order):
    if type(order) is int:
        return chr(order)

def is_strings_permutations(string_1: str, string_2: str) -> bool:

    # If sting_2 is a permutation of string_1 than their length is the same:
    if len(string_1) != len(string_2):
        return False
    else:
        # Assume that string contain only ASCII characters
        # It follwos that there are 127 variations of characters

        # Create a list of charracter frequencies
        frequencies = [0 for x in range(0, 127)]

        # Count frequencies in string_1 and record in frequencies
        for char in string_1:
            char_order = ord(char)
            frequencies[char_order] +=1

        # For every character in string_2 substract from frequencies
        # If the frequency drops bellow zero string_2 is not a permutation of string_1

        for char in string_2:
            char_order = ord(char)
            frequencies[char_order] -=1
            if frequencies[char_order] < 0:
                return False

    return True


if __name__ == "__main__":

    print(is_strings_permutations("abs", "abs"))
    print(convert_ord_to_char(64))