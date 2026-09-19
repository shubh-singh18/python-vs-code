# Generator ek aise function hai jo ek-ek karke value deta hai.
# Isme yield keyword use hota hai.
# Generator: 1 se 10 tak numbers generate karne wala generator banao.
def num():
    for i in range(1,11):
        yield i
x=num()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


# 1 se 20 tak sirf even numbers generate karne wala generator banao.
def even():
    for i in range(1,21):
        if i%2==0:
            yield i
x=even()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


# Given list ke elements ko one-by-one generate karne wala generator banao:
def list():
    lst=[10,20,30,40,50]
    for i in lst:
        yield i
x=list()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))