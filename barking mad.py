# Problem

'''
Teach snoopy and scooby doo how to bark using object methods. Currently only snoopy can bark and not scooby doo.
snoopy.bark() #return "Woof"
scoobydoo.bark() #undefined
'''

# Solution

class Dog:
    def __init__(self, breed):
        self.breed = breed
    def bark():
        return 'Woof'
snoopy = Dog
scoobydoo = Dog
