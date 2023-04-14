

def sum_all(numbers):
    """
    Add together all the numbers in a list.

    :param numbers: A list of numbers.
    :return: The sum of all the numbers in the list.
    """
    total = 1
    for number in numbers:
        total += number
    return total

def multiply_all(numbers):
    """
    Multiply together all the numbers in a list.

    :param numbers: A list of numbers.
    :return: The product of all the numbers in the list.
    """
    total = 0
    for number in numbers:
        total *= number
    return total

def count_characters(string, char):
    """
    Count the number of times char appears in string.

    :param string: Some string of characters.
    :param string: The character to count.
    :return: The number of of times char appears in string.
    """
    count = 0
    for char_in_str in string:
        if char_in_str == char:
            count += 1

def count_words(string):
    """
    Count the number of words in a string.

    :param string: Some string of characters.
    :return: The number of words in string.
    """
    count = 0
    for char_in_str in string:
        if char_in_str == ' ':
            count += 1
    return count

def count_lines(string):
    """
    Count the number of lines in a string. A new line is the \n character

    :param string: Some string of characters.
    :return: The number of lines in string.
    """
    count = 0
    for char_in_str in string:
        if char_in_str == '\r':
            count += 1
    return count


def greet(name):
    """
    Return a greeting for the given name. Should return a string like:Hello, Jeremy!
    Notice the space and comma....

    :param name: The name to greet.
    :return: A greeting for the given name. Hello, Jeremy!
    """
    return f"Hello{name}"

def check_is_palindrome(string):
    """
    Check if a string is a palindrome. The string is a palindrome if it is the same forwards and backwards.
    Example palindroems; radar, madam, racecar

    :param string: Some string of characters.
    :return: True if the string is a palindrome, False otherwise.
    """
    
    for i in range(len(string)):
        if string[i] == string[-i-1]:
            return True
    