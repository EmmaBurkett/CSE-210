"""Abstraction - we want a little piece of information to store; not all
of it.  Like when your math teacher gives you useless info and wants                                          Hello
you to only acknowledge the info that is relevant to the given problem.

A Class is: another way to write code. We often use classes for
organization or convenience. It can store functions and can store 
variables. 

Instance: a single occurrence of something. So, when you have an
'instance of a class' you have a single occurrence of that class.
"""


# This is a class; it is also an object. 
class Person:
    pass


# Create a 'Person.' 
# This creates an instance of the class Person and stores that class 
# in 'emma'
emma = Person()

# You can create a different person, 
# which creates a new instance of the class. 
# 'heather' stores an instance of person which has no relation to the
# instance of 'emma'
heather = Person()

print(emma)
# prints out something like this: 
# <__main__.Person object at 0x0000023C2101FCA0>
# '__main__' is a reference for this file. 
# 'Person' is our class
# '0x0000023C2101FCA0' is the location in memory for the object 'emma'
# So this says:
# 'In the current file 'emma' is an object, 'Person,' which is stored 
# in memory location 0x0000023C2101FCA0'



# This declares a variable which we store in the class.
# This variable is arbitrarily called an 'attribute' because 
# it is a variable owned by the class.
emma.full_name = "Emma Burkett" 

# print the variable.
print(emma.full_name)


# Note: OOP = Object Oriented Programming 
