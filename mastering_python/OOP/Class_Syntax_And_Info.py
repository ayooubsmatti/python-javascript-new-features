# ----------------------------------------------
# --------- OOP  - Class Syntax And Info   -----
# ----------------------------------------------
# [01] class is the blusprint or constructor of th object
# [02] class Instantiate Means Create Instance of A class
# [03] Instance => object created from class and have their methods
# [04] class Defined with keyword class
# [05] class Name written with pascalCase [UpperCamelCase] Style
# [06] class may contains methods and attributes
# [07] when creating object python look for built in __init__ method
# [08] __init__ method called every time you create object from class
# [09] __init__ method is initialize the data for the object
# [10] Any method with two Underscore in the start and end called Dunder or magic method
# [11] self refer to the current instance created from the class and must be firs param
# [11] self refer to the current instance created from the class and must be firs param
# [12] self can be Named anything
# [13] In pyhton you dont need to call new() keyword to create object
# ----------------------------------------------

# syntax
# class Name:
#   constructor => Do instantiation [Create instance from a class ]
#   each instance is separate object
#   def__init_(self,other_data)
#       body of function

# class Member:
#     def __init__(self):
#         print("A new Member Has Been Added")


# member_one = Member()
# member_two = Member()
# member_three = Member()

# print(member_one.__class__)

# ----------------------------------------------

# my_dictionary = {
#     'name':"Osama",
#     'age':36,
#     'monthly_salary':5000,
#     'yearly_salary':, #Something
# }


# ----------------------------------------------
# -- OOP  - Instance Attributes And Methods-----
# ---------------------------------------------
# Self: point to instance creates from class
# Instance Attributes: Instance Attributes defined inside the constructor
# -----------------------------------------------
# Instance Methods: take self parameter wich point to instance created from class
# Instance Methods can have more than one parameter like my function
# Instance Methods can freely Access attributes and methods on teh same Object
# Instance Methods can access the class itself
# -----------------------------------------------

class Member:

    def __init__(self, first_name, middle_name, last_name, gender):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender

    def full_name(self):
        return f"{self.fname} {self.mname} {self.lname}"

    def name_with_title(self):
        if self.gender == "male":
            return f"Hello Mr :{self.fname}"
        else:
            return f"Hello Ms :{self.fname}"


member_one = Member("Ayoub", "Mohamed", "Smatti", "male")
member_two = Member("Ahmed", "Ali", "Islem", "male")
member_three = Member("Mona", "Mohamed", "Smatti", "female")

print(member_one.full_name())
print(member_one.name_with_title())
print(member_three.name_with_title())
