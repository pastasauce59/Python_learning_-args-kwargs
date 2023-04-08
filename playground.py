##ARGUMENTS WITH DEFAULT VALUES
def my_function(a=1, b=2, c=3):
    #Do this with a
    #Then do this with b
    #Finally do this with c
    pass


##FUNCTIONS WITH UNLIMITED ARGUMENTS
# def add(n1, n2):
#     return n1 + n2

def add(*args):
    #args will be in the form of a tuple
    for n in args:
        print(n)


##UNLIMITED (POSITIONAL) ARGUMENTS

def add(*args):
    #You can access args by index as well
    print(args)
    print(args[2])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,4,7))


##UNLIMITED KEYOWRD ARGUMENTS
def calculate(n, **kwargs):
    # print(type(kwargs))
    print(kwargs)
#    for (key, value) in kwargs.items():
#     print(key)
#     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=5)


class Car:
    #**kw represents all of the optional arguments that can be passed in when initializing car class
    def __init__(self, **kw):
        # self.make = kw['make']
        # self.model = kw['model']
        #IF you fail to put in an argument for 'make' or 'model', it will throw an error.
        #USE kw.get() instead because it will generate 'none' if no argument is given.
        self.make = kw.get('make')
        self.model = kw.get('model')

# my_car = Car(make='Nissan', model='GT-R')
my_car = Car(make='Nissan')

print(my_car.make, my_car.model)