# #fizz Buzz
# print numbers from 1 to 100 .for multiple of:
#     3,print "fizzz"
#     5,print "bizz"
# both 3 and 5 print "fizzbu", otherwise the number itself
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("Fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("bizz")
    else:
        print(i) 
        