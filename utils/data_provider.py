import random


def generate_random_array(start, end, size):
    """Generate random array of numbers"""
    list_array = []

    for i in range(0, size):
        list_array.append(random.randint(start, end))

    return list_array
