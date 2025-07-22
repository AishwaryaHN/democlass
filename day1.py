# print('hello')
# landing page


# print("welcome to python cls")





# python introduction
# variables -naming given to the memory location of the computer. used to store same or different kinds of data/values.

# a=10
# Rules for naming variable 
# we can use alphabets ,numbers,$. 
# it cannot starts with number bt it can starts with aplha /$.StopIteration
# white space not allowed.
# reserved keyword or special characters are not allowed.
# its a  casesensitive.
# Name="aishwarya"
# name="sathvik"
# print(name)
# name="siri"
# a=10
# b=20
# c=30
# a,b,c=10,20,30
# print(a,b,c)

# a=50
# print(a)
# add_numbers=10

#  data types -5
# 1.numbers 
# a.integers-its contain whole number also it may be + or -

# a=0
# b.floating points- real numbers  decimal number

# b=0.002
# c.complex -real and imaginary part

# a=10+2j 
# j contains -1
# print(a.imag)


# 2.boolean -returns only either True or False
# is_eligible=False
# print(is_eligible)
# 3.sequence-its a oredered collection of same or different kind of data .
# a.string its a sequence of character enclose within "" or ''
# property-immutable (not changeble)


# operations
# indexing-[] its starts with 0
# place="chamarajanagara"
age="18"
# place[1]="a"
# print(place)
# slicing-dividing a part 
# syntax:-
# [start:end:skip]
# print(place[0:9:3])
# print(type(float(age)))
# print(f'my age is {age}')
# print(place+"  "+int(age))

# typecasting-converting one variable value to another variable value type.



# lower()
# count()
# remove()



# age='23'
# age="13"
# print(age)
# b="0.03"
# name="python"
# b.list-
# c.tuple
# 4.dictionary
# 5.sets


# operators
# conditional statements
# looping
# function



# advanced 
# oops
# module 
# file handling

# numbers=["student","teacher"]
# numbersinTuple=(1,2,3,4)

# UpperCasewords=list(map(lambda x:x.upper(),numbers))
# print(UpperCasewords)

# 4 features in oops 
# 1.inheritance-child class inherits the propertis and methods from parents class. 
# class Animal:
#     # name="darshika"
#     def __init__(self,color,wieght):
#         self.color=color
#         self.wieght=wieght
#     def eat(self):
#         return "eating"
# class dog(Animal):
#     def __init__(self, color, wieght,breed):
#         super().__init__(color, wieght)
#         self.breed=breed
#     def bark(self):
#         return "barking"
# class cat(dog):
#     def meow(self):
#         return"meow meow"
# d=cat("white",100,"golden")

# print(d.color)
# print(d.eat())
# print(d.breed)
# print(d.meow())





# 2.Encapsulation-use to secure the data (private and public attributes)

# class account:
#     def __init__(self,balance):
#         self.__balance=balance  #private
#     def get_balance(self):
#         return "my balance is",self.__balance
# a1=account(10000)
# print(a1.get_balance())
        # pass

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age #private attribute
#     def getAge(self,age2):
#         self.__age=age2
#         return self.__age
#     def get_name(self,name2):
#         self.name=name2
#         return self.name
    

# s1=Student("hitha",18)
# print(s1.name)

# print(s1.getAge(25))
# print(s1.get_name("darshika"))


# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def make_sound(self):
#         pass 

# class Dog(Animal):
#     def make_sound(self):
#         return "bark"

# # A1=Animal()
# D1=Dog()

# print(A1.make_sound())
# print(D1.make_sound())






# 3.Polymorphism-poly means many morphism means forms/ways. methodoverriding.
# the same function name behaves differenty based on the object that calls it.
# class vehicle:
#     def start(self):
#         return "vehicle"
# class bike(vehicle):
#     def start(self):
#         return "i have two weels"
# class car(bike):
#     def start(self):
#         return "i have  four wheels"
# c1=vehicle()
# print(c1.start())

# class parent:
#     def __init__(self,year):
#         self.year=year

#     def calc_age(self):
#         ageVar=2025-self.year
#         return ageVar
    

# class age(parent):
    
#     def __init__(self,year):
#         self.year=year

#     def say(self):
#         return self.year
#     def display(self):
#         return f'you born in {self.year} and your age is{ageVar}'

# c1=age(2002)
# print(c1.year)
# class student:
#     def __init__(self,name,age):
#          self.name=name
#          self.__age=age
#     def __get_age(self):
#          return self.__age
#     def set_age(self,new_age):
#          self.__age=new_age
#          print("new_age is updated")
#         #  return self.__age
#     def display(self):
#          return self.__get_age()

# s1=student("s1",18)
# print(s1.name)
# print(s1.set_age(40))
# print(s1.display())

# class chm:
#     def welcome(self):
#         return "ba daey"
# class mandya(chm):
#     def welcome(self):
#         return "baarlaa"
# class mysore(mandya):
#     def welcome(self):
#         return "ba broo"
# class mangalore(mysore):
#     def welcome(self):
#         return "banni"
    
# mg=mangalore()
# print(mg.welcome())
# 4.Abstraction

# from abc import ABC, abstractmethod
# class user(ABC):
    
#     @abstractmethod
#     def login(self):
#         pass
    
#     def display(self):
#         return self.login()
    

# class AdminUser:
#     def login(self):
#         print("u logged in as admin")
    

# U=AdminUser()
# U.login()

    
# module is nothing but python file. it consist of functions and variables(array,object and dictionries )
