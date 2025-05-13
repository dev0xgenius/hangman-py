import random

def join(list):
    str_value = ""
    for item in list:
        str_value += item
    return str_value

def swapchar(str_value, pos, item):
    str_list = list(str_value)
    str_list[pos] = item
    
    return join(str_list)

def pick_random_letter(word):
    return random.choice(word.split())

def get_char(prompt):
    user_input = input(f'{prompt}> ')
    while len(user_input) > 1 or len(user_input) == 0:
        user_input = input("one letter, allowed> ")
    return user_input
