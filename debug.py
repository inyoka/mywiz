#!/usr/bin/env python3
# debug.py

def debug(func):
    # wraps function with a debugger.
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper


def make_adder(x, y):
    # Code executed when instance called.
    # Code Generator
    def add():
        return x + y
    return add


class Spam:
    a = 1 # Class variable

    def __init__(self, x, y):
        self.x = x # Instance variable
        self.y = y # Instance variable

    def foo(self):
        pass
'''
>>> s = Spam(2, 3)
>>> s.__dict__
{'y': 3, 'x': 2}
>>> Spam.__dist__['foo']
<function Spam.foo at 0x100>
'''

    def imethod(self): # Instance method
    # s = Spam()
    # s.imethod()
        pass

    @classmethod
    def cmethod(cls): # Class method
        pass

    @staticmethod
    def smethod(): # Function put in a class
        # Belongs to class but not instance.
        # Think : List of possible inputs
        pass

class Array:
    # Customise everything wth special methods
    def __getitem__(self, index):
        pass

    def __setitem__(self, index, value):
        pass

    def __delitem__(self, index):
        pass

    def __contains__(self, item):
        pass

#  Inheritance
class Base:
    def spam(self):
        pass

class Foo(Base):
    def spam(self):
        # Call method in base class
        r = super().spam()
