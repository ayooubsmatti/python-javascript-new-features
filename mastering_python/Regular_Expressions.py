# ----------------------------------------------
# ---------      Regular Expressions -----------
# ----------------------------------------------

# [1] Sequeence of characteers that define a search pattern
# [2] Regular Expression is not In python its General concept
# [3] Used In [Credit Cartd Validaton, Ip Address Validation, Email Validation]
# [4] Test Regex "https://pythex.org"
# https://regex101.com/
# [5] Characters Sheet "https://www.debuggex.com/cheatsheet/regex/python"
# ----------------------------------------------


# ----------------------------------------------
# --Regular Expressions => Quantifiers ---------
# ----------------------------------------------
# * 0 or more
# + 1 or more
# ? 0 or 1 o
# {2} Exactly 2
# {2,5} Between 2 and 5
# {2,}  2 or more
# {,5}  Up to 5
# ----------------------------------------------


# ----------------------------------------------
# --Regular Expressions => Characters Classes Training's
# ----------------------------------------------
# [0-9]
# [^0-9]
# [A-Z]
# [^A-Z]
# [a-z]
# [^a-z]
# ----------------------------------------------

# ----------------------------------------------
# --Regular Expressions => Assertions & Email Pattern
# ----------------------------------------------
# ^ Start of string
# $ End of String
# ----------------------------------------------
# Match e-mail
# [A-z0-9\.]+@[A-z0-9]+\.+[A-z]+
# [A-z0-9\.]+@[A-z0-9]+\.(com|net|info)
# ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|info)$


# ----------------------------------------------
# --Regular Expressions => Logical Or & Escaping
# ----------------------------------------------
# | or
# \ Escape Special Characters
# () Separate Group
# ----------------------------------------------
# (\d-|\d\|\d>)(\w+)
# (\d{3})(\d{4})(\d{3}|\(\d{3}\))
# 1-HTML
# 2-CSS
# 3-PHP

# 1)HTML
# 2)CSS
# 3)PHP

# 1> HTML
# 2> CSS
# 3> PHP
# ----------------------------------------------
# ^(https?://)(www\.)?(\w+)\.(net|org|com|info|me)
# https://www.elzero.net
# http://elzero.org
# https://www.elzero.com
# ----------------------------------------------


# ----------------------------------------------
# --Regular Expressions => Re Module Search and FindAll
# ----------------------------------------------
# search() => search a string for A match and return a first match only
# findall() => Return a list of all matches and empty list if no match
# ----------------------------------------------
# Email pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------
# import re

# my_search = re.search(r"[A-Z]{2}", "AAyoubSmatti")

# print(my_search)  # <re.Match object; span=(5, 6), match='S'>
# print(my_search.span())
# print(my_search.string)
# print(my_search.group())

# ----------------------------------------------
# import re
# is_email = re.search(
#     r"[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)", "saber@gmail.com")

# if is_email:
#     print("This is a valid email")
#     print(is_email.span())
#     print(is_email.string)
#     print(is_email.group())

# else:
#     print("This is a Not valid email")

# ----------------------------------------------
# import re
# email_input = input("Please write your Email: ")
# search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net|org|info", email_input)

# empty_list = []

# if search != []:
#     empty_list.append(search)
#     print("Email Added")

# else:
#     print("Invalid Email")

# for email in empty_list:
#     print(email)
# ----------------------------------------------

# ----------------------------------------------
# --Regular Expressions => Re Module Split & Sub
# ----------------------------------------------
# split(pattern, String, MaxSplit) => Return A list of Elements Splitted on each match
# sub(pattern, Replace, String, ReplaceCount) replace matches with what you want
# ----------------------------------------------
# import re
# string_one = "i love python programing language"
# search_one = re.split(r"\s", string_one, 1)
# print(search_one)

# print("#"*50)

# string_two = "i_How-To_Write_A_Very-Good-Article"
# search_two = re.split(r"-|_", string_two)
# print(search_two)

# # Get words from URL
# for counter, word in enumerate(search_two, 1):
#     if len(word) == 1:
#         continue

#     print(f"word Number: {counter} => {word.lower()}")

# print("#"*50)

# my_string = "I love python"

# print(re.sub(r"\s","-",my_string,1))

# ----------------------------------------------
# --Regular Expressions => Group Training's & Flags
# ----------------------------------------------
import re
# (https?)://(www)?\.?(w+)\.(\w+):?(\d+)?/?(.+)
# https://www.ayoub.org:8080/category.php?article=105?name=how-to-do
# https://www.ayoub.org/category.php?article=105?name=how-to-do
# https://ayoub.org/category.php=50?article=105?name=how-to-do
# https://ayoub.org/category.php?article=105?name=how-to-do
# https://ayoub.org
# https://ayoub.net

my_web = "https://www.ayoub.org:8080/category.php?article=105?name=how-to-do"
search = re.search(r"(https?)://(www)?\.?(w+)\.(\w+):?(\d+)?/?(.+)", my_web)
print(f"Protocol: {search.group(1)}")
print(f"Sub Domain: {search.group(2)}")
print(f"Domain Name: {search.group(3)}")
print(f"Top Level Domain: {search.group(4)}")
print(f"Port: {search.group(5)}")
print(f"Query String: {search.group(6)}")
# ----------------------------------------------
