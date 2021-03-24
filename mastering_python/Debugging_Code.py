# ----------------------------------------------
# ---------   Debugging Code         -----------
# ----------------------------------------------

my_list = [1, 2, 3, 4, 5, 6]
my_dictionary = {"Name": "ayoub", "Age": 25, "country": "Algeria"}

for num in my_list:
    print(num)

for key, value in my_dictionary.items():
    print(f"{key} => {value}")


def function_one():
    print("Hello From Function One")


function_one()
