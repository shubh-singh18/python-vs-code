#Given a string use a for loop to count how many vowels (a,i,e,o,u) it contains.
text=input("enter a string")
count=0
for ch in text:
    if ch.lower() in "aieou":
        count+=1
        print(count)