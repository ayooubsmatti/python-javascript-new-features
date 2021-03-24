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
# ////addition
# print(10+30)  # 30
# ////substraction
# print(10-30)  # -20
# print(10 - - 10)  # 20
# ////multiplication
# print(10*30)
# print(5 + 10*5)  # 1005
# ////divition
# print(100/5)
# ////modulus
# print(8 % 5)  # 3
# /////exponent
# print(2**5)  # 2*2*2*2*2 = 32
# ////floor devition
# print(100 // 20)  # 5
# print(110//20)  # 5


###################################################
# /////////////////////////////////////////////lists
# mutabale (add,delett..)/ have defrents type data
# mylist = ["one", "two", "one", 1, 100.5, True]

# print(mylist)
# print(mylist[1])  # full liste
# print(mylist[-1])  # true
# print(mylist[-3])  # 1

# print(mylist[1:4])  # ['two', 'one', 1]
# print(mylist[:4])  # ['one', 'two', 'one', 1]
# print(mylist[1:])  # ['two', 'one', 1, 100.5, True]
# print(mylist[::1])  # ['two', 'one', 1, 100.5, True]
# print(mylist[::2])  # ['one', 'one', 100.5]

# mylist[1] = 2
# print(mylist)  # ['one', 2, 'one', 1, 100.5, True]
# mylist[0:2] = []
# print(mylist)  # ['one', 1, 100.5, True]

# ////////////////////append()

# myfriend = ["ayoub", "oussama", "alla"]
# myoldfriend = ["saber", "ilyas"]
# print(myfriend)  # ['ayoub', 'oussama', 'alla']
# myfriend.append("youcef")
# print(myfriend)  # ['ayoub', 'oussama', 'alla', 'youcef']
# myfriend.append(100)
# print(myfriend)  # ['ayoub', 'oussama', 'alla', 'youcef', 100]
# myfriend.append(myoldfriend)
# ['ayoub', 'oussama', 'alla', 'youcef', 100, ['saber', 'ilyas']]
# print(myfriend)
# print(myfriend[5][1])  # ilyas

# //////////////////////extend()

# a = [1, 2, 3, 4]
# b = ["a", "b", "b"]
# print(a)#[1, 2, 3, 4]
# a.extend(b)
# print(a)#[1, 2, 3, 4, 'a', 'b', 'b']
# //////////////////////remove()

# x = [1, 2, 3, 4, 'a', 'b', 'b']
# x.remove("b")
# print(x)# delete just the first b
# //////////////////////sort()
# y = [1, 2, 3, 566, 21, 42, 36, 17]
# y.sort()
# print(y)  # [1, 2, 3, 17, 21, 36, 42, 566]
# y.sort(reverse=True)
# print(y)  # [566, 42, 36, 21, 17, 3, 2, 1]

# //////////////////////reverse()
# y = [1, 2, 3, 566, 21, 42, 36, 17]
# y.reverse()
# print(y)#[17, 36, 42, 21, 566, 3, 2, 1]

# //////////////////////clear()
# a = [1, 2, 3, 566, 21, 42, 36, 17]
# a.clear()
# print(a)
# //////////////////////copy()
# a = [1, 2, 3, 566, 21, 42, 36, 17]
# c = a.copy()
# print(c)


# ///////////////////////count()
# d = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8]
# print(d.count(5))  # 3
# ///////////////////////index()
# d = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8]
# print(d.index(5))  # 4
# ///////////////////////insert()
# d = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8]
# d.insert(0, "a")  # insert object befor insert
# print(d)  # ['a', 1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8]
# ///////////////////////pop()
# d = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8]
# print(d.pop(6))  #5

###################################################
# /////////////////////////////////////////////Tuplle

# mytuple = ("as", "dez")
# mytuple1 = "sa", "54"
# print(mytuple)
# print(mytuple1)

# ///////tuple indexing

# mytuple = ("as", "dez")
# print(mytuple[1])

# ///////////tuple assign values

# mytuple = ("as", "dez")
# print(mytuple[2]) = "2" #error cannot assign to function call


# mytuple = ("as", "dez",2)
# print(mytuple[1]) #dez
# print(mytuple[-1]) #2


# # //////////////////////////////////////tuple methods
# #######tuple with one elements
# mytuple = ("ayoub",)
# print(type(mytuple))
# #######tuple concatinations
# a = (1, 2, 3)
# b = (4, 5)
# d = a+b
# print(d)#(1, 2, 3, 4, 5)
# #######tuple, list, string repeat(*)
# a = (1, 2, 3)
# print(a*6)#(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
# "##############index
# a = (1, 2, 3)
# print(f"the index of 1 is : {a.index(1)}")
# ##############tuple destruct
# a = ("a", "b", "c", "f")
# x, y, _, z = a
# print(x)#a
# print(y)#b
# print(z)#f

###################################################
# /////////////////////////////////////////////Set

# not orderd
# mySetOne = {"1", "ayoub", 100}
# print(mySetOne)
# print(mySetOne[0])#error
# not slicing
# print(mySetOne[:2])#error
# immutable
# mySetOne = {"1", "ayoub", 100,[1,2,3]}#error unhachable with list
# mySetOne = {"1", "ayoub", 100, (1, 2, 3)}
# print(mySetOne)#{'ayoub', (1, 2, 3), 100, '1'}

# item must be unique

# myset = {1, 2, 3, 2, 3, 5, 4}
# print(myset)  # {1, 2, 3, 4, 5}
# ####################clear()
# myset = {1, 2, 3, 2, 3, 5, 4}
# myset.clear()
# #####################"union()

# myset = {1, 2, 3, 2, 3, 5, 4}
# myset1 = {1, 2, 3, 4}
# print(myset | myset1)#{1, 2, 3, 4, 5}
# print(myset.union(myset1))#{1, 2, 3, 4, 5}
# #####################"add()

# myset = {1, 2, 3, 2, 3, 5, 4}
# myset.add(10)
# print(myset)  # {1, 2, 3, 4, 5, 10}
# #####################"copy()

# myset = {1, 2, 3, 4, 5}
# myset1 = myset.copy()
# print(myset1)  # {1, 2, 3, 4, 5}
# #####################"remove()

# myset = {1, 2, 3, 4, 5}
# myset.remove(3)
# print(myset)  # { 2, 3, 4, 5}
# #####################"discart()
# the same with remove else dosent show the error
# myset = {1, 2, 3, 4, 5}
# myset.discard(7)
# print(myset)  # {1, 2, 3, 4, 5}
# ##########################"pop()
# myset = {1, 2, 3, 4, 5}
# print(myset.pop())  # random elements
# ##########################"update()
# myset = {1, 2, 3, 4, 5}
# myset1 = {1, 2, "a", "b"}
# myset.update(myset1)
# print(myset)  # {1, 2, 3, 4, 5, 'a', 'b'}
# ##########################"defference()
# myset = {1, 2, 3, 4, 5}
# myset1 = {1, 2, "a", "b"}
# print(myset)  # {1, 2, 3, 4, 5}
# print(myset.difference(myset1))  # myset-myset1
# myset.difference_update(myset1)
# print(myset)#{3, 4, 5}

# ##########################"intersection()
# myset = {1, 2, 3, 4, 5}
# myset1 = {1, 2, "a", "b"}
# print(myset)  # {1, 2, 3, 4, 5}
# print(myset.intersection(myset1))  # {1, 2}
# myset.intersection_update(myset1)
# print(myset)  # {1, 2}
# ##########################"symetrique defrent()
# myset = {1, 2, 3, 4, 5}
# myset1 = {1, 2, "a", "b"}
# print(myset)  # {1, 2, 3, 4, 5}
# print(myset.symmetric_difference(myset1))  # {3, 'b', 4, 5, 'a'}
# myset.symmetric_difference_update(myset1)
# print(myset)  # {3, 'b', 4, 5, 'a'}
# # ##########################"issubset()
# myset = {1, 2, 3, 4, 5}
# myset1 = {1, 2, "a", "b"}
# print(myset)  # {1, 2, 3, 4, 5}
# print(myset.issubset(myset1))  # false

# # ##########################"issuerset()
# myset = {1, 2, 3, 4, 5}
# myset1 = {1, 2}
# print(myset)  # {1, 2, 3, 4, 5}
# print(myset.issuperset(myset1))  # True
# # ##########################"isjoint()
# myset = {1, 2, 3, 4, 5}
# myset1 = {1, 2}
# print(myset)  # {1, 2, 3, 4, 5}
# print(myset.isdisjoint(myset1))  # false


###################################################
# ///////////////////////////////////////Dictionary
# key: value
# user = {
#     "name": "ayoub",
#     "age": 25,
#     "country": "algeria",
# }
# print(user['name'])#ayoub
# print(user.get('name'))#ayoub
# print(user.keys())#dict_keys(['name', 'age', 'country'])
# print(user.values())#dict_values(['ayoub', 25, 'algeria'])
# two dimensional dictionary
# user = {

#     "one": {
#         "name": "ayoub",
#         "age": 25,
#         "country": "algeria",
#     },

#     "two": {
#         "name": "ali",
#         "age": 25,
#         "country": "france",
#     }
# }
# # {'one': {'name': 'ayoub', 'age': 25, 'country': 'algeria'}, 'two': {'name': 'ali', 'age': 25, 'country': 'france'}}
# print(user)
# print(user['one']['name'])#ayoub

# two dimensional dictionary
# user = {

#     "one": {
#         "name": "ayoub",
#         "age": 25,
#         "country": "algeria",
#     }
# }
# # {'one': {'name': 'ayoub', 'age': 25, 'country': 'algeria'}, 'two': {'name': 'ali', 'age': 25, 'country': 'france'}}
# print(user)#{'one': {'name': 'ayoub', 'age': 25, 'country': 'algeria'}}
# print(user.clear())#None

# update
# user = {

#     "one": {
#         "name": "ayoub",
#         "age": 25,
#         "country": "algeria",
#     }
# }
# # {'one': {'name': 'ayoub', 'age': 25, 'country': 'algeria'}, 'two': {'name': 'ali', 'age': 25, 'country': 'france'}}
# print(user)  # {'one': {'name': 'ayoub', 'age': 25, 'country': 'algeria'}}
# user.update({"ranking": 52})
# print(user)
# setdefault()
# user = {
#     "name": "ayoub",
#     "age": 25,
#     "country": "algeria",
# }

# # {'one': {'name': 'ayoub', 'age': 25, 'country': 'algeria'}, 'two': {'name': 'ali', 'age': 25, 'country': 'france'}}
# print(user)  # {'one': {'name': 'ayoub', 'age': 25, 'country': 'algeria'}}
# user.setdefault("name", "oussama")
# print(user)
# ###########################popitem()
# user = {
#     "name": "ayoub",
#     "age": 25,
#     "country": "algeria",
# }

# # {'one': {'name': 'ayoub', 'age': 25, 'country': 'algeria'}, 'two': {'name': 'ali', 'age': 25, 'country': 'france'}}
# print(user)  # {'one': {'name': 'ayoub', 'age': 25, 'country': 'algeria'}}
# user.update({"ranking": "52"})
# print(user.popitem())# returne the last update item
# items()
# user = {
#     "name": "ayoub",
#     "age": 25,
#     "country": "algeria",
# }

# alliTems = user.items()
# print(user)#{'name': 'ayoub', 'age': 25, 'country': 'algeria'}
# user["age"] = 36
# print(alliTems)#dict_items([('name', 'ayoub'), ('age', 36), ('country', 'algeria')])
# fromkeys()
# a = ('dzad', 'dazda', 'ssfgr')
# b = "a"

# print(dict.fromkeys(a, b))#{'dzad': 'a', 'dazda': 'a', 'ssfgr': 'a'}


###################################################
# //////////////////////////////////////////Boolean
# True False

# # True value
# print(bool("ayoub"))
# print(bool(123))
# # False value
# print(bool(0))
# print(bool(''))
# print(bool(""))
# print(bool([]))
# print(bool({}))
# print(bool(False))
# ################# Boolean operator

# age = 26
# country = "algeria"
# # print(country == "france")  # false
# # print(age > 20 and country == "algeria")  # true
# # print(age > 30 or country == "algeria")  # true
# print(age > 30)  # not true = false
# print(not age > 30)  # not false = true

###################################################
# /////////////////////////////Assignment Operators

# x = 11
# y = 20
# z = x + y
# z = z + y  # z += y
# z = z - y # z -= y
# x //= 11
# x %= 11
# x /= 11
# x **= 2
###################################################
# /////////////////////////////Comparison Operators
#
# print(100 == 100)  # true
# print(100 == 100)  # true
# print(100 == 100.00)  # true
# print(100 != 100.00)  # false
# print(100 > 100)  # false
# print(100 < 100)  # false
# print(100 >= 100)  # true
# print(100 <= 100)  # true
###################################################
# /////////////////////////////type conversation

# str
# a = 10
# print(type(a))
# print(type(str(a)))
# tuple
# a = "sdasasa"  # string
# b = [1, 2, 3, 5]  # list
# c = {1, 5, 3, 6, 5}  # set
# e = {"a": 1, "b": 2}  # dictionary
# print(tuple(a))#('s', 'd', 'a', 's', 'a', 's', 'a')
# print(tuple(b))#(1, 2, 3, 5)
# print(tuple(c))#(1, 3, 5, 6)
# print(tuple(e))#('a', 'b')

# list
# a = "sdasasa"  # string
# b = [1, 2, 3, 5]  # list
# c = {1, 5, 3, 6, 5}  # set
# e = {"a": 1, "b": 2}  # dictionary

# print(list(a))  # ['s', 'd', 'a', 's', 'a', 's', 'a']
# print(list(b))  # [1, 2, 3, 5]
# print(list(c))  # [1, 3, 5, 6]
# print(list(e))  # ['a', 'b']
# ###############################set
# a = "sdasasa"  # string
# b = [1, 2, 3, 5]  # list
# c = [1, 5, 3, 6, 5]  # list
# e = {"a": 1, "b": 2}  # dictionary

# print(set(a))  # {'a', 's', 'd'}
# print(set(b))  # {1, 2, 3, 5}
# print(set(c))  # {1, 3, 5, 6}
# print(set(e))  # {'a', 'b'}

# dict
# c = (("a", 1), ("b", 2), ("c", 3))  # tuple
# b = [["one", 1], ["three", 1], ["two", 1]]  # list

# print(dict(c))  # {'a': 1, 'b': 2, 'c': 3}
# print(dict(b))  # {'one': 1, 'three': 1, 'two': 1}


###################################################
# ////////////////////////////////////// User input

# name = input('what\'is your name: ')
# lastname = input('what\'is your name: ')
# name = name.strip().capitalize()
# lastname = lastname.strip().capitalize()

# print(f"Hello {name} {lastname}")
# print(f"Hello { lastname:.1s} {name} ")

###################################################
# ////////////////////////////////////// Email slice

# email = "saberayoubsmatti@gmail.com"
# print(email[0:email.index("@")])#saberayoubsmatti
# print(email[(email.index("@")+1):])#gmail.com

###################################################
# /////////////////////Control Flow - If, Elif, Else

# name = "saber"
# if name == "saber":
#     print(True)
# else:
#     print(False)


# Control Flow - Ternary Conditional Operator
# age = 18
# print("you are less than 18 years old" if age <
#       18 else "you are able to request")


###################################################
# /////////////////////////////Membership Operators

# string
# name = "ayoub"
# print("s" in name)

# list
# friendlist = ["ayoub", "youcef", "saber"]
# print("ayoub" in friendlist)#True
# print("ayoub" not in friendlist)#false


###################################################
# /////////////////////////////Loop - While and Else

# a = 0
# while a < 15:
#     print(a)
#     a += 1
# a = 0

######################################
# mylist = ["sa", "ss", "sa", "asa"]
# a = 0
# while a < len(mylist):
#     print(mylist[a])
#     a += 1

###################################################
# /////////////////////////////Loop - for and Else

# mylist = ["sa", "ss", "sa", "asa"]
# for a in mylist:
#     print(a)
# else:
#     print("finished")
# add to list with for
# a = []
# for i in range(5):
#     a.append(input(""))
# print(a)
# for with dictionary

# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# for key in a_dict:
#     print(key, '->', a_dict[key])

# for with dictionary nested
# d = {
#     'dict1':
#         {'foo': 1, 'bar': 2},
#     'dict2':
#         {'baz': 3, 'quux': 4}
# }

# for keys, values in d.items(): #first method
#     print(f"{keys}:")
#     for key, val in values.items():
#         print(f"-{key} ----> {val}")


# for a in d:  # second method
#     print(a)
#     for s in d[a]:
#         print(d[a][s])

###################################################
# /////////////////////////////Break Continue Pass
# break
# a = [1, 2, 3, 4, 6, 7, 8]

# for c in a:
#     if c == 4:
#         continue # ignore numbre 4
#     print(c)
# break
# a = [1, 2, 3, 4, 6, 7, 8]

# for c in a:
#     if c == 4:
#         break  # break before numbre 4
#     print(c)


# pass
# a = [1, 2, 3, 4, 6, 7, 8]

# for c in a:
#     pass
###################################################
# /////////Function Packing, Unpacking Arguments *Args

# mylist = [1, 2, 3, 3, 4]
# print(*mylist)#1 2 3 3 4

# def say_hello(*persones):
#     for p in persones:
#         print(f"Hello! {p}")


# say_hello("saber", "ayoub", "smatti", "youcef")
#############################################################
# /////////Function Packing, Unpacking Arguments default value

# def say_hello(firsname, lastname="unknow"):
#     print(f"Hello! {firsname} , {lastname} ")

# say_hello("saasa")#Hello! saasa , unknow

#############################################################
# ///////////////Function Packing, Unpacking Arguments KWArgs

# def say_person(**persones):
#     for key, value in persones.items():
#         print(f"{key}: {value}")


# say_person(name="saber", lastname="smatti") # name: saber \n lastname: smatti


##############################################################
# mydictionary = {
#     "name": "saber",
#     "lastname": "smatti"
# }


# def say_person(**persones):
#     for key, value in persones.items():
#         print(f"{key}: {value}")


# say_person(**mydictionary)  # name: saber \n lastname: smatti


################################################################
# *Tuple **Dictionary

# def show_skills(name, *skills, **framworks):
#     print(f"skills {name} ")
#     for skill in skills:
#         print(f"-{skill}")

#     print(f"framworks is: ")
#     for framworkName, framwork in framworks.items():
#         print(f"-{framworkName} --> {framwork}")


# show_skills("skills", "java", "css", "html", framwork="django")
###################################################################
# ////////////////////////////////////////////// Function Recursion


# def clean_word(word):  # wwoooorld
#     if len(word) == 1:
#         return word

#     if word[0] == word[1]:
#         return clean_word(word[1:])

#     else:
#         return word[0]+clean_word(word[1:])
#     return word


# print(clean_word("wwoorld")) #world

#####################################################################
# def print_pyramid(a):
#     numofestral = 1
#     estreal = "* "
#     space = " "
#     numspace = a-1
#     while a > 0:
#         print(numspace * space + numofestral * estreal)
#         a -= 1
#         numspace -= 1
#         numofestral += 1


# print_pyramid(8)

#        *
#       * *
#      * * *
#     * * * *
#    * * * * *
#   * * * * * *
#  * * * * * * *
# * * * * * * * *

###################################################################
# //////////////////////////////////////////////////Function Lambda

# def say_hello(name):
#     return f"Hello {name}"


# print(say_hello("ayoub"))
# print(say_hello.__name__)

# hello = lambda: name, age : f"Hello {name} {age}"

# print(hello("ayoub",23))

###################################################################
# ///////////////////////////////////////////////////Files Handling
# import os
# # Main Current working directory
# print(os.getcwd())
# # Directory for the opened file
# print(os.path.dirname(os.path.abspath(__file__)))
# # change current working directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# myfile = open("/home/ayoub/ayoub.txt", "r")

# print(myfile)  # file data object
# print(myfile.name)  # name
# print(myfile.mode)  # mode
# print(myfile.encoding)  # encoding

# print(myfile.read())
# print(myfile.read(5))


# print(myfile.readline(2))
# print(myfile.readline())
# print(myfile.readline())
# print(myfile.readline())
# print(myfile.readline())
# print(myfile.readline())


# print(myfile.readlines())


# for line in myfile:
#     print(line)
#     if line.startswith("de"):
#         break

# best practice close the file after your complete the task

##############################################################
# ///////////////////////////////////Write and Append In Files

# myfile = open("/home/ayoub/ayoub.txt", "w")
# myfile.write("hello\n")
# myfile.write("second\n")

# myfile = open(r"/home/ayoub/ayoub.txt", "w")
# myfile.write("second \n"*100)

# mylist = ["oasma\n", "ayoub\n", "ouali\n"]
# myfile = open(r"/home/ayoub/ayoub.txt", "w")
# myfile.writelines(mylist)

# a save the old lines and complete


# mylist = ["oasma\n", "ayoub\n", "ouali\n"]
# myfile = open(r"/home/ayoub/ayoub.txt", "a")
# myfile.truncate(5)


# mylist = ["oasma\n", "ayoub\n", "ouali\n"]
# myfile = open(r"/home/ayoub/ayoub.txt", "a")
# print(myfile.tell())# place of cursure


# myfile = open(r"/home/ayoub/ayoub.txt", "r")
# myfile.seek(4)
# print(myfile.read())  # read from seek() position


##############################################################
# ///////////////////////////////////Built In Functions Part 1


# x = [1, 2, 3, "", 5, 6]

# if all(x):
#     print("all elements is ture")

# else:
#     print("at list one elements is false")

# b = [1, 2, 3, "", 5, 6]

# if any(b):
#     print("at list one elements is ture")

# else:
#     print("theres no any true elements")


# ########bin return binnary
# print(bin(100))

# id

# a = 1
# b = 3
# print(id(a))
# print(id(b))


# sum(iterable, start)
# a = [1, 10, 18, 16]
# print(sum(a))
# print(sum(a, 40))

# round(iterable, numofdigits)
# print(round(150.501))
# print(round(150.555, 2))

# ############## range(startt, end,step)
# a = [1, 10, 18, 16]
# print(list(range(0)))
# print(list(range(10)))
# print(list(range(10, 20, 2)))


# ##########################################print()

# print("sasa", "sasa", sep="#")

# print("firstline", end="\n")#by default

# print("firstline", end=" ")# doesn't return line


# ###################################abs()
#  ###################################pow(base,exp,mod) => Power

# print(pow(2,5))
# print(pow(2,5,10)) #2*2*2*2*2 %10

#  ###################################min(item,item,or iterator) =>

# print(min(2,5,4,8,2,7,5))#2


#  ###################################max(item,item,or iterator) =>
# print(max(2, 5, 4, 8, 2, 7, 5))  # 8
# # ################################### slice()
# a = ["a", "b", "c", "a", "b", "c"]
# print(a[:5])  #['a', 'b', 'c', 'a', 'b']
# print(a[slice(0, 5)])  #['a', 'b', 'c', 'a', 'b']

# # ################################### Map()


# def formatText(text):
#     return f"- {text.strip().capitalize()} -"


# myTexts = ["oussama ", " ay", "saber   "]
# myFormatedata = map(formatText, myTexts)

# for name in myFormatedata:
#     print(name)


# use map with lamda functions


# myTexts = ["oussama ", " ay", "saber   "]

# for name in list(map(lambda text: f"- {text.strip().capitalize()} -", myTexts)):
#     print(name)

# //////  Filter
# #case 1
# def checkNumber(num):
#     if num < 10:
#         return num


# myNumbers = [1, 2, 3, 4, 5, 6]
# myResult = filter(checkNumber, myNumbers)

# for number in myResult:

#     print(number)

# case 2

# def checkNumber(num):
#     if num == 0:
#         return True # must be true to return 0 because th filter fun does't return 0


# myNumbers = [1, 2, 3, 4, 5, 6, 0, 0, 0]
# myResult = filter(checkNumber, myNumbers)

# for number in myResult:

#     print(number)

# /////// case 3


# myString = ["abs", "abs", "ok", "okt", "sas", ]
# myResult = filter(lambda name: name.startswith("o"), myString)

# for nam in myResult:

#     print(nam)


##################################### #####################################
# Reduce()

# from functools import reduce


# def sumAll(sum1, sum2):

#     return sum1 + sum2


# numbers = [1, 2, 3, 4, 6, 8]
# myResult = reduce(sumAll, numbers)
# print(myResult)

##################################### #####################################
# enumerate()

# mySkills = ["html", "css", "javascript", "python"]

# myskillsWithCounter = enumerate(mySkills, 20)

# # print(type(myskillsWithCounter))

# for counter, skill in myskillsWithCounter:

#     print(f"{counter}- {skill}")

##########################################################################
###########################################################################
# help()
# print(help(print))


##########################################################################
# revers()

# name = "ayoub"
# # print(reversed(name))
# for letter in reversed(name):
#     print(letter)

##########################################################################
###################################################          date and time
import datetime
# print(dir(datetime))
# print(dir(datetime.datetime))

# print(datetime.datetime.now())
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)
# sec = datetime.datetime.now().second
# print(f"{sec}")


# # print current time HOUR
# print(datetime.datetime.now().time().hour)
# # print current time minute
# print(datetime.datetime.now().time().minute)
# # print current time second
# print(datetime.datetime.now().time().second)


# # print start end of time
# print(datetime.time.min)#00:00:00
# print(datetime.time.max)#23:59:59.999999


# # print a specific date
# print(datetime.datetime(2015, 2, 14))


# find my age
# myBirthDay = datetime.datetime()
# dateNow = datetime.datetime.now()

# print(f"your age is: {(dateNow - myBirthDay).days}")

##############################################
# format date
# https://strftime.org

# import datetime
# myBirthDay = datetime.datetime(1996, 2, 14)
# print(myBirthDay.strftime("%A %b %d %y"))#Wednesday Feb 14 96


#################################################
# iterable vs iterator
# iterable is the object contains data can be iterate upon
# exemple: (string, list,set, tuple, dictionary)
#
# iterator: thr objects used to iterate over ierable using next() method return 1 elements at the time

# myString = "saber"
# myIterator = iter(myString)
# print(next(myIterator))  # s
# print(next(myIterator))  # a
# print(next(myIterator))  # b

##############################################################
# //////////////////////////////////////////////////Generators

# generators is a functions with "yield" keywords insted of "return"
#

def myGenerator():
    yield 1
    yield 2
    yield 3


myGen = myGenerator()
print(next(myGen))
print(next(myGen))
print(next(myGen))
