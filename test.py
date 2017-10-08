"""
test of decorator
"""

def deco1(func):
    print("In deco1")
    return func

def deco2(arg):
    def test(func):
        func()
    print("In deco2 {}".format(arg))
    return test

@deco2("Oops!")
@deco1
def foo():
    print("In Foo")

def counter(start_at=0):
    count = [start_at]
    def incr():
        count[0] += 1
        return count[0]
    return incr

class wrapme(object):
    def __init__(self, data):
        self.__data = data

    def get(self):
        return self.__data

    def __getattr__(self, item):
        return getattr(self.__data, item)