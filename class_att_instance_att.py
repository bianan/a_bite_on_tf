"""
https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
"""


class MyClass(object):
    class_var = 1

    def __init__(self, i_var):
        self.i_var = i_var
        
        
foo = MyClass(2)