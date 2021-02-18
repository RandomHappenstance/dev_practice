import random


def generate_str():
    """ Returns a random string of a size between 3 and 10 characters and its reverse. """
    string_size = random.randint(5, 7)
    string_output = ""

    # TODO A good exercise wold be to generate the forward and reverse strings in one pass.
    for _ in range(string_size):
        string_output += chr(random.randint(64, 122))
    return string_output, string_output[::-1]
