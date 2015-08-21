import string
import random


def generate_random_string_64():
    return ''.join(random.choice(string.letters+string.digits) for i in range(64))


def generate_random_string_4():
    return ''.join(random.choice(string.ascii_uppercase+string.digits) for i in range(4))

def generate_random_number_4():
    return ''.join(random.choice(string.digits) for i in range(4))
