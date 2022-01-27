"""
CSV note - Flash card that you write your class on what your class calls what your class does.
also your methods. Can also create your attributes but some people don't like that
top: Director
Left: Behavior 
Right: Called Class
bottom: 
"""
def hello_word(message):
    hello = "Hello"
    return "Hello " + message

def array():
    message_array = []
    for i in range(2):
        message_array.append(hello_word("World"))
    return message_array

print(array())