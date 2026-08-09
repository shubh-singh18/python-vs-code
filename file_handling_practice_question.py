# question 1->Create a file named data.txt and write "python file handling"into it.

with open("data.txt","w")as f:
 print(f.write("Python file handing\n")) 

#question 2->Read the data.txt file and print its  complete content.

with open("data.txt","r")as f:
    print(f.read())

#question 3->Add "I am learning python" to data.txt without deleting the existing content.

with open("data.txt","a")as f:
   print(f.write("I am learning python"))

#question 4->Read a file and count the total number of lines present in it.

with open("destination.txt","r")as f:
 print(len(f.readlines()))

#question 5->Read a file and count the total number of words present in it.

with open("data.txt","r")as f:
    a=f.read()
    words=a.split()
    print(len(words))

#question 6->Read a file and count the total number of characters,excluding spaces.

with open("data.txt","r")as f:
    data=f.read()
    print(len(data))

#question 7->Take a word from the user and check whether that word exists in a file or not.

with open("data.txt","r")as f:
    a=f.read()
if "python" in a:
    print("word is present in file")
else:
    print("word is not present")

#question 8->Read the contents of source.txt and copy them into destination1.txt

with open("source.txt","r")as f:
    a=f.read()
with open("destination1.txt","w")as f:
    print(f.write(a))




















   