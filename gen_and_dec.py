def generator():
    yield 1
    yield 2
x=generator()
print(next(x))
print(next(x))

def decorator(fun):
    def wrapper():
        print("before function")
        fun()
        print("after function")
    return wrapper
@decorator
def hello():
    print("hello")
hello()



def a():
    return ("this  is frist function")
x=a()
def b(x):
    return x
print(b(x))

def a(x):
    def b():
        print("before changing")
        x()
        print("after changing")

    return b
@a
def c():
    print("this is decorator function")
c()
