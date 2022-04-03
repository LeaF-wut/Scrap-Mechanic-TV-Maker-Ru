import random
import string

def get_random_string(length):
    letters = ['I','l']
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(length, result_str)

get_random_string(128)
