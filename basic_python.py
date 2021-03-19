###################################################
# ////////////////////////////////////////data type
# print(type(100))  # int => Integer
# print(type(-100))  # int => Integer

# print(type(100.8))  # float => Floating Point Numbers
# print(type(-100.8000000))  # float => Floating Point Numbers

# print(type("python"))  # str => String

# print(type([1, 2, 3, 4]))  # list => List

# print(type((1, 2, 3, 4)))  # tuple => Tuple

# print(type({"One": 1, "Two": 2, "Three": 3}))  # dict => Dictionary
# print(type(2 == 2))  # bool => Boolean


###################################################
# ////////////////////////////////////////variables
# name = "ayoub"  # single words =>  Normal
# myName = "ayoub"  # Two words => camelCase
# my_name = "ayoub"  # Two words => snake_case

###################################################
# /////////////////////////////////reserved keyword
# help("keywords")
###################################################

# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)

###################################################
# //////////////////////Escape Sequences Characters
# back space
# print("hello\b ayoub")  # will remove "o"
# # escape new line + \
# print("hello\
#  ayoub")
# # escape \
# print(" python \" ")
# print(" python \\ ")  # escape with print

# # escape single cuote
# print("i love \'python\' ")
# # escape double cuote
# print("i love \"python\" ")

# # line feed
# print("hello \n ayoub")

# # carriage return
# print("12345\rabcd")

# # Horizontal Tab

# print("hello\tpython")a

# # character hex value
# print("\x4f")
###################################################
# ////////////////////////////////////Concatenation

# msg = "i love"
# lang = "python"
# print(msg + lang)


###################################################
# //////////////////////////////////////////Strings

# myString = "ayoub smatti"

# multipleLIne = '''a
# b
# c
#  '''
# print(multipleLIne)

###################################################
# //////////////////////////////////Indexing-slicing
# Indexing (access single item)

# myString = "I love python"
# print(myString[0])  # first carracter from begin
# print(myString[-1]  # first carracter from end

# Slicing (access multiple sequence items)
# [Start:end] end is not enclude
# [Start:end:steps]
# myString1 = "I love python"
# print(myString1[2:6])  # love
# print(myString1[:6])  # start from 0
# print(myString1[6:])  # start from 6 untile the end
# print(myString1[:])  # full string

# print(myString1[::1])  # full string
# print(myString1[::2])  # full string
###################################################
# ///////////////////////////////////String Methods
# a = "i love python"
# print(len(a))  # calculate number of caracters with spaces

# //////////////////////////strip() rstrip() lstrip()
# b = "        i love  python        "

# print(b.strip())
# print(b.rstrip())
# print(b.lstrip())

# c = "#######i love  python##########"
# print(c.strip('#'))
# print(c.rstrip('#'))
# print(c.lstrip('#'))

# /////////////////////////////////////////////title()

# b = "i love python and c sharp"
# print(b.title())

# /////////////////////////////////////////capitalize()

# print(b.capitalize())

# ///////////////////////////////////////////////zfill()
# c,d,e = "1","11","120"
# print(c.zfill(3))
# print(d.zfill(3))
# print(e.zfill(3))

# /////////////////////////////////////////upper()lower()
# g = "ayoub"
# print(g.upper())
# print(g.lower())

# ////////////////////////////////////////split() rsplit()

# a = " i love python and django"
# print(a.split())

# b = " i-love-python-and-django"
# print(b.split("-"))

# c = " i-love-python-and-django"
# print(c.split("-", 2))  # max split

# d = " i-love-python-and-django"
# print(c.rsplit("-", 2))  # split from th right

# /////////////////////////////////////////////////center()
# a = "ayoub"
# print(a.center(9))  # spaces
# print(a.center(9, '#'))  # hash
# print(a.center(9, '@'))  # @

# /////////////////////////////////////////////////count()

# a = " i love python and django and"
# print(a.count("and", 0, 35))

# //////////////////////////////////////////////swapcase()

# a = " L love Python and django and"
# print(a.swapcase())
# //////////////////////////////////////////////startwith()
# a = " L love Python and django and"
# print(a.startswith("L",0,32))

# //////////////////////////////////////////////endswith()
# a = " L love Python and django and"
# print(a.endswith("L", 0, 32))
# ///////////////////////////////index(substring, start, end)
# a = " L love Python and django and"
# print(a.index("P")) # index 8
# print(a.index("P", 0, 10)) # index 8
# print(a.index("P", 0, 5)) # THrough Error

# ///////////////////////////////find(substring, start, end)

# a = " L love Python and django and"
# print(a.find("P"))  # index 8
# print(a.find("P", 0, 10))  # index 8
# print(a.find("P", 0, 5))  # -1
# //////////////// rjust(width, fill char) ljust(width, fill char)

# a = "ayoub"
# print(a.rjust(10))
# print(a.rjust(10, "#"))

# print(a.ljust(10))
# print(a.ljust(10, "#"))

# //////////////////////////////////////// splitlines()

# e = """first line
# second line
# third line"""
# print(e.splitlines())

# d = "first line\nsecond line\nthird line"

# print(d.splitlines())
# //////////////////////////////////////////// expandtabs()
# d = "first line\tsecond line\tthird line"
# print(d.expandtabs(2)) # 2 is the number of tabs

# ////////////////////////////istitle()

# a = "I Love Python"
# print(a.istitle()) # true

# b = "I love python"
# print(b.istitle()) # false

# ////////////////////////////////isspace()
# tree =" "
# print(tree.isspace())

# ////////////////////////////////islower()
# a =" "
# print(a.islower())

# ////////////////////////////////islower()
# a =" "
# print(a.islower())


# ////////////////////////////////isidentifier()
# a =" ayoubsmatti"
# b =" ayoubsmatti"
# c =" ayoubsmatti"
# print(a.isidentifier()) #true
# print(b.isidentifier()) #true
# print(c.isidentifier()) #false

# ////////////////////////////////isalpha()

# x = "fdfsqggqd"
# y = "ffezfze6545454"
# print(x.isalpha())
# print(y.isalpha())

# ////////////////////////////////isalpha()
# x = "fdfsqggqd"
# y = "ffezfze6545454"
# print(x.isalnum())
# print(y.isalnum())

# ////////////////////////////////replace(old value, new value, count)

# a = "hello one two three one one"
# print(a.replace("one", "1", 2))

# ///////////////////////////////////join(Iterable)
# mylist = ["ayoub", "smatti", "saber"]
# print("-".join(mylist))

###################################################
# //////////////////////////////////String formating

# ////////////Old Method %d digit %s string %f float

# name = "saber"
# age = 36
# rank = 10
# print("my name is: %s" % "saber")
# print("my name is: %s" % name)
# print("my name is: %s and my age is: %d" % (name, age))
# print("my name is: %s and my age is: %d and my age is: %f" % (name, age, rank))

# control floating  point numbers
# mynumber = 10
# print("my numbers is: %f" % mynumber)
# print("my numbers is: %.2f" % mynumber)  # two number after point

# Truncate string

# string1 = "hello i am here dady"
# print("Message is %.5s" % string1) # the first 5 caracter

# ///////////////////////////////New Method


# name = "saber"
# age = 36
# rank = 10
# print("my name is: {}" .format("saber"))
# print("my name is: {}" .format(name))
# print("my name is: {} and my age is: {}" .format(name, age))
# print("my name is: {:s} and my age is: {:d} and my age is: {:.2f}" .format(name, age, rank))

# ////////format money

# money = 564852084751
# print("money in account is: {:d}" .format(money))
# print("money in account is: {:_d}" .format(money))
# print("money in account is: {:,d}" .format(money))

# ////////rerange item

# a, b, c = "one", "two", "three"
# print("hello {} {} {}".format(a, b, c))  # hello one two three
# print("hello {1} {2} {0}".format(a, b, c))  # hello one two three one


# z, x, y = 2, 3, 4
# print("hello {} {} {}".format(z, x, y)) #hello 2 3 4
# print("hello {1:d} {2:.3f} {0:d}".format(z, x, y))#hello 3 4.000 2

# Format in version 3.6+

# z, x, y = 2, 3, 4

# print(f"z:{z} , x:{x} , y:{y}")


###################################################
# //////////////////////////////////////////Numbers
# integer float complex

# mycomplex = 5 + 6j
# print("reel part is: {}" .format(mycomplex.real))
# print("imaginary part is: {}" .format(mycomplex.imag))
# complex type can't change to any
# integer or float can change to any
# int() float() complex()
# /////////////////////////////////Numbers operators
# addition
print(10+30)  # 30
# substraction
print(10-30)  # -20
print(10 - - 10)  # 20
# multiplication
print(10*30)
print(5 + 10*5)  # 1005
# divition
print(100/5)
# modulus
print(8 % 5)  # 3
# exponent
print(2**5)  # 2*2*2*2*2 = 32
# floor devition
print(100 // 20)  # 5
print(110//20)  # 5
