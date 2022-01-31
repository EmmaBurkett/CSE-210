class Base:
    def __init__(self):
        self._helper()

    def _helper(self):
        print("Helper Function")
    
    def __helper2(self):
        print("Helper 2 function")
    
x = Base()

print("Trying to call subfunction")

x._helper() # will let you access this private function because python
            # lets you be an adult and call whatever you want
            # this is called protected

print("Trying to call private function")
#x.__helper2()  # double underscore means private - see init
                # Python will return an error class ovject has no attribute

x._Base__helper2()  # You can access protect and private methods but as a rule
                    # You should not.