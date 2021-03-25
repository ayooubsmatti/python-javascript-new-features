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

# class Member:

#     def __init__(self, first_name, middle_name, last_name, gender):
#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender

#     def full_name(self):
#         return f"{self.fname} {self.mname} {self.lname}"

#     def name_with_title(self):
#         if self.gender == "male":
#             return f"Hello Mr :{self.fname}"
#         else:
#             return f"Hello Ms :{self.fname}"


# member_one = Member("Ayoub", "Mohamed", "Smatti", "male")
# member_two = Member("Ahmed", "Ali", "Islem", "male")
# member_three = Member("Mona", "Mohamed", "Smatti", "female")

# print(member_one.full_name())
# print(member_one.name_with_title())
# print(member_three.name_with_title())


# ----------------------------------------------
# --------- OOP  - Class Attributes  -----------
# ----------------------------------------------
# Self: point to instance creates from class
# Instance Attributes: Instance Attributes defined inside the constructor
# -----------------------------------------------
# class attributes: attributes defined outside the constructor
# -----------------------------------------------


# class Member:
#     not_allowed_attribute = ["hell", "shit", "baloot"]
#     users_num = 0

#     def __init__(self, first_name, middle_name, last_name, gender):
#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender
#         Member.users_num += 1

#     def full_name(self):
#         if self.fname in Member.not_allowed_attribute:
#             raise ValueError("Name Not Allowed")
#         else:
#             return f"{self.fname} {self.mname} {self.lname}"

#     def name_with_title(self):
#         if self.gender == "male":
#             return f"Hello Mr :{self.fname}"
#         else:
#             return f"Hello Ms :{self.fname}"

#     def delete_user(self):
#         Member.users_num -= 1
#         return f"User {self.fname} Deleted."


# print(Member.users_num)
# member_one = Member("Ayoub", "Mohamed", "Smatti", "male")

# member_two = Member("Ahmed", "Ali", "Islem", "male")

# member_three = Member("shit", "Mohamed", "Smatti", "female")

# print(Member.users_num)
# print(Member.delete_user(member_one))
# print(Member.users_num)


# ----------------------------------------------
# --------- OOP  - Class Methods And Static-----
# ----------------------------------------------
# Class Method:
# --marked with @classmethod-decorator-to-flag-it-as-class-method
# --it take cls parameter not self to point to the class not the instance
# --used when yo want to do somthing with the class itself
# -static method:
# --it takes no parameters
# --its bound to the class not instance
# --used when doing something doesn't have access to object or class but related to class
# -----------------------------------------------


# class Member:
#     not_allowed_attribute = ["hell", "shit", "baloot"]
#     users_num = 0

#     @classmethod
#     def show_users_count(cls):
#         print(f"we have {cls.users_num} User in our system")

#     @staticmethod
#     def say_hello():
#         print("Hello from static method")

#     def __init__(self, first_name, middle_name, last_name, gender):
#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender
#         Member.users_num += 1

#     def full_name(self):
#         if self.fname in Member.not_allowed_attribute:
#             raise ValueError("Name Not Allowed")
#         else:
#             return f"{self.fname} {self.mname} {self.lname}"

#     def name_with_title(self):
#         if self.gender == "male":
#             return f"Hello Mr :{self.fname}"
#         else:
#             return f"Hello Ms :{self.fname}"

#     def delete_user(self):
#         Member.users_num -= 1
#         return f"User {self.fname} Deleted."


# member_one = Member("Ayoub", "Mohamed", "Smatti", "male")

# member_two = Member("Ahmed", "Ali", "Islem", "male")

# member_three = Member("shit", "Mohamed", "Smatti", "female")
# -----------------------------------------------
# this two ways is equal bu prefer one
# print(member_one.full_name())
# print(Member.full_name(member_one))
# -----------------------------------------------
# Member.show_users_count()
# Member.say_hello()
# -----------------------------------------------


# ----------------------------------------------
# --------- OOP  - Magic Methods ---------------
# ----------------------------------------------
# Everything in python is an object
# __init__ called automatically when instantiation class
# self.__class__ the class to which a class instance belongs
# __str__ gives a human readable output of the object
# __len__ returns the length of the container
# --------called when we use the built in len() function on the object
# -----------------------------------------------

# class Skill:
#     def __init__(self):
#         self.skills = ["html", "css", "js"]

#     def __str__(self):
#         return f"THis is my skills => {self.skills}"

#     def __len__(self):
#         return len(self.skills)


# profile = Skill()
# print(profile)
# print(profile.__class__)
# print(len(profile))

# profile.skills.append("php")
# profile.skills.append("MySQL")

# print(len(profile))


# ----------------------------------------------
# --------- OOP  - Inheritance -----------------
# ----------------------------------------------

# class Food:  # base class
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         print(f"{self.name} Is created From base class")

#     def eat(self):
#         print("eat method from base class")


# class Apple(Food):  # derived class
#     def __init__(self, name, price, amount):
#         # Food.__init__(self, name) #create Instance from base class
#         super().__init__(name, price)
#         self.amount = amount
#         print(f"{self.name} Is created From derived class and price is {self.price} and amount is {self.amount}")

#     def get_from_tree(self):
#         print("get from tree from derived class")


# food_two = Apple("Pizza", 15, 20)
# food_two.eat()
# food_two.get_from_tree()


# --------------------------------------------------
# ------------- OOP  - Method Overriding -----------
# --------------------------------------------------
# class Food:  # base class
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         print(f"{self.name} Is created From base class")

#     def eat(self):
#         print("eat method from base class")


# class Apple(Food):  # derived class
#     def __init__(self, name, price, amount):
#         # Food.__init__(self, name) #create Instance from base class
#         super().__init__(name, price)
#         self.amount = amount
#         print(f"{self.name} Is created From derived class and price is {self.price} and amount is {self.amount}")

#     def get_from_tree(self):
#         print("get from tree from derived class")

#     def eat(self):#overidd method
#         print("Eeat Method From Drived Class")


# food_two = Apple("Pizza", 15, 20)
# food_two.eat()
# food_two.get_from_tree()
# food_two.eat()


# --------------------------------------------------
# ----- OOP  - Multiple Inheritance ----------------
# --------------------------------------------------

# class BaseOne:
#     def __init__(self):
#         print("Base One")

#     def fun_One(self):
#         print("One")


# class BaseTwo:
#     def __init__(self):
#         print("Base Two")

#     def fun_Two(self):
#         print("Two")


# class Derived(BaseOne, BaseTwo):
#     pass


# my_var = Derived()
# # print(Derived.mro())

# my_var.fun_One()
# my_var.fun_Two()

# class Base:
#     pass
# class DerivedOne(Base):
#     pass
# class DerivedTwo(DerivedOne):
#     pass


# --------------------------------------------------
# ----- OOP  -  Polymorphism -----------------------
# --------------------------------------------------

# class A:
#     def do_somthing(self):
#         print("From Class A")
#         raise NotImplementedError("Derived class must implement this methods")


# class B(A):
#     pass


# class C(A):
#     def do_somthing(self):
#         print("from class C")


# my_instance = C()
# my_instance.do_somthing()


# --------------------------------------------------
# ----- OOP  -   Encapsulation ---------------------
# --------------------------------------------------

# Encapsulation
# --restrict Access to the data stored in attributes and methods
# -Public
# --every Attribute and method that we used so far is public
# --Attributes and methods can be modified and run from everywere
# --inside our outside the class
# -Protected
# --Attributes and methods can be accessed from within the class and sub classes
# --Attributes and Methods Prefixed with One Underscore _
# -Private
# --Attributes and methods can be Accessed from within the class or project only
# --Attributes cannot be modified from outside the class
# --Attributes and methods prefixed with two Underscores __
# ---------------------------------------------------
# --Attributes = Variables = Properties
# ---------------------------------------------------

# class Member:
#     def __init__(self, name):
#         self.name = name #Public


# one = Member("Ayoub")
# print(one.name)
# one.name = "ayoub"
# print(one.name)
# ---------------------------------------------------

# class Member:
#     def __init__(self, name):
#         self._name = name  # Protected


# one = Member("Ayoub")
# print(one._name)
# one.name = "ayoub"
# print(one._name)
# ---------------------------------------------------

# class Member:
#     def __init__(self, name):
#         self.__name = name  # Private

#     def say_hello(self):
#         return f"Hello {self.__name}"


# one = Member("Ayoub")
# # print(one.__name) #error
# print(one.say_hello())
# print(one._Member__name)

# ---------------------------------------------------

# --------------------------------------------------
# ----- OOP  -  Getters And Setters ----------------
# --------------------------------------------------
# class Member:
#     def __init__(self, name):
#         self.__name = name  # Private

#     def say_hello(self):
#         return f"Hello {self.__name}"

#     def get_name(self):  # Getter
#         return self.__name

#     def set_name(self, new_name):
#         self.__name = new_name


# one = Member("Ayoub")
# print(one.get_name())
# one.set_name("saber")
# print(one.get_name())

# --------------------------------------------------
# ----- OOP  -  @Property Decorator ----------------
# --------------------------------------------------
# class Member:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say_hello(self):
#         return f"Hello {self.name}"

#     @property
#     def age_in_days(self):
#         return self.age * 365


# one = Member("Ayoub", 25)
# print(one.name)
# print(one.age)
# print(one.say_hello())
# print(one.age_in_days)


# --------------------------------------------------
# ----- OOP  -  ABCs Abstract Base Class -----------
# --------------------------------------------------
# --class called abstract class if it has one or more abstract methods
# --abc module in python provides Infrastructure for defining custom abstract base classes
# --by adding @abdstractmethod Decorator on the methods
# --ABCMeta class is a Metaclass used for defining abstract base class
# ---------------------------------------------------
# from abc import ABCMeta, abstractclassmethod


# class Programming(metaclass=ABCMeta):
#     @abstractclassmethod
#     def has_oop(self):
#         pass

#     def has_name(self):
#         pass


# class Python(Programming):
#     def has_oop(self):
#         return "Yes"


# class Passcal(Programming):
#     def has_oop(self):
#         return "No "


# one = Passcal()
# print(one.has_oop())
# ---------------------------------------------------
