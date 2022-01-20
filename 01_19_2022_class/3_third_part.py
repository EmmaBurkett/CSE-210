class Person:

    # this: ="" initializes full_name as an empty string
    # init is a 'constructor.'
    def __init__(self, full_name=""):

        # Store parameter in an attribute self.full_name for any
        # given instance. 
        self.full_name = full_name
    

# An instance of Person stored in 'emma'
emma = Person("Emma Burkett")
print(emma)

# Manipulate the variable that is declared in the _init_ of this
# instance of Person.
print(emma.full_name)
# For this instance of Person, emma = self
# emma.full_name = self.full_name


# An instance of the class Person stored in 'heather'
heather = Person("Heather Purser")
print(heather)

# A variable owned by a class is arbitrarily called an 'attribute' 
# because objects in real life have attributes. 
# Manipulate the attribute owned by the instance of Person 
# called 'heather.'
print(heather.full_name)
# For this instance of Person, heather = self
# heather.full_name = self.full_name




