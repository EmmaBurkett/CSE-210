"""
In this file we create an array attribute in Person which will hold
a list of instances, 'Restaurant.' The list represents the Person's 
favorite places to eat.
""" #Hello

class Person:

    # ="" initializes full_name as an empty string
    def __init__(self, full_name=""):

        # Store parameter in an attribute self.full_name for hello
        # this instance. 
        self.full_name = full_name

        # This array will hold multiple instances of Restaurant.
        self.restaurants = []
    

    def add_restaurant(self, restaurant):
        """This is a very simple method (Recall: Method = Function)"""

        # Add a new restaurant to our self.restaurants array.
        self.restaurants.append(restaurant)
    

    def get_restaurants(self):

        # return the our list of favorite restaurants (each item in the
        # array being an instance of Restaurant, which array is stored 
        # in an instance of person)
        # Each 'Person' will have their own list of favorite restaurants.
        return self.restaurants
    

    def get_favorite_restaurant(self):
        # Put something in best to initialize it.
        best = -1

        # put an instance of restaurant into favorite to initialize it.
        favorite = Restaurant("","","5", -1)

        # Loop through the array self.restaurants, let r represent each
        # element in the array.
        for r in self.restaurants:

            # set 'best' equal to an element's rating.
            best = r.rating

            # Set favorite equal to an element's instance of Restaurant.
            favorite = r

            # Repeat for each element.

        # (favorite will return the last element in the array)

        # This returns the last element in the array. 
        return favorite


# New class called restaurant.
class Restaurant:

    # You will pass in four variables, 'self' should not be 
    # passed in when an instance of Restaurant is declared.
    def __init__(self, name, cuisine, price, rating):

        # Attributes of a restaurant.
        self.name = name
        self.cuisine = cuisine
        self.price = price
        self.rating = rating
    
    def __str__(self):
        return self.name

emma = Person("Emma Burkett")
print(emma)
print(emma.full_name)

# An instance of Restaurant; it holds everything you need to know about
# big judds
big_judds = Restaurant("Big Judd's", "American", "5", 4)

# Add the instance of Restaurant, big_judds to my instance of 
# Person's 'restaurant' list attribute.
emma.add_restaurant(big_judds)

# A new instance of Restaurant.
pizza_hut = Restaurant("Pizza Hut", "Pizza", "5", 3)

# Add this restaurant to Emma's favorite restaurant list.
emma.add_restaurant(pizza_hut)

# Prints the location in memory for each restaurant in the array.
print(emma.get_restaurants())

# Prints emma's favorite restaurant.
print(f"{emma.full_name}'s favorite restaurant is",
      f"{emma.get_favorite_restaurant()}")
    
# An instance of Person.
heather = Person("Heather Purser")
# Prints the location in memory for the object heather.
print(heather)
# Prints heather's name.
print(heather.full_name)
