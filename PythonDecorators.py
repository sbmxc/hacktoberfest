#Decorators

#Decorators can be thought of as functions which modify the functionality of another function. They help to make your code shorter and more "Pythonic"


#creating decorator in python

def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")
