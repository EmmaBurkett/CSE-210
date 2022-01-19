"""
Recall that in past classes you used functions, and sometimes you used
a function multipul times for different purposes. It's the same with
classes; you will use a class multipul times for different purposes. In 
this file you will use a class to represent multipul persons. 

instantiate = to create an instance, or a single occurrence, of an object.
"""

class Person:

    # Class functions are called methods - arbitrary terminology.
    # __init__ instantiates your class
    # every method has a parameter 'self' in the leftmost position.
    def __init__(self):
        pass

# instantiate a person
# instantiate = to create an instance of an object. So 'emma' stores 
# an instance of the class Person
emma = Person()
print(emma)

# instantiate another person: (line 27)
# 'heather' stores another instance of the class Person, different than
# the instance of Person stored in 'emma.' 
heather = Person()
print(heather)