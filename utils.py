import random

def join(var_list, sep=""):
    count = 0
    str_value = ""

    for item in var_list:
        if count == (len(var_list) - 1):
            sep=""
        str_value += (item + sep)
        count += 1
    return str_value

def swapchar(str_value, pos, item):
    str_list = list(str_value)
    str_list[pos] = item
    
    return join(str_list)

def pick_random_letter(word):
    return random.choice(word.split())

def get_char(prompt, chars=[]):
    prompt = chars and f"({join(chars, ', ')}) {prompt}" or prompt

    user_input = input(f'{prompt}> ')
    while len(user_input) > 1 or len(user_input) == 0:
        user_input = input("one letter, allowed> ")

    if chars:
        try:
            chars.index(user_input)
        except Exception as e:
            print(f"{e}")
            return get_char("<- Pick from list", chars)
    return user_input
