
# Reverse a String
# Write a function reverse_string(text) that reverses a string without using [::-1].
def reverse_string(text):
    rev=""
    for i in text:
        rev=i+rev
    return rev
print(reverse_string("shivam"))
