
# -----------------------------------------------------------
# ----- Advanced_lessons Generate Random Serial --- ---------
# -----------------------------------------------------------

import string
import random

# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)


def make_serial(count):
    all_chars = string.ascii_letters + string.digits
    # print(all_chars) #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
    chars_count = len(all_chars)
    # print(chars_count)
    serial_list = []
    while count > 0:
        random_number = random.randint(0, chars_count - 1)
        random_character = all_chars[random_number]
        serial_list.append(random_character)
        count -= 1
    print("".join(serial_list))


make_serial(20)
