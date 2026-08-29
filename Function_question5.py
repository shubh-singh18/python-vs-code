# Count Vowels
# Write a function count_vowels(text) that counts the number of vowels in a given string. 
# The function should handle both uppercase and lowercase letters.
def count_vowels(text):
    count=0
    for ch in text:
        if ch.lower() in "aieou":
            count+=1
    return count
text=input("enter a text")
print(count_vowels(text))
