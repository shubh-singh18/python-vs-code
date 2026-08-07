#write a python program to create a .text file named "student.txt" and write the names of five student into it

with open("student.txt","w")as f:
    f.write("devansh\n")
    f.write("shivam\n")
    f.write ("shubh\n")
    f.write("shiva\n")
    f.write("Ram\n")

#question2
#write  a python program to read and display the entire contents of a text file

with open("student.txt","r")as f:
    data=f.read()
    print(data)

#question3
#write a python program to read and display the file line by line using a loop


with open ("student.txt","r")as f:
    for i in range(0,3):
     data=f.readline()
     if i>=0:
      print(data,end="")


#question4
#write a python program to append the text "python is fun!" to an existing text file and then display the updated contents.

with open("student.txt","a")as f:
   data=f.write("python is fun\n")
   print(data)

#question5
#write a python program to count the total number of lines in a text file.

with open("student.txt","r")as f:
   data=f.readlines()
   print(data)
   print(len(data))

#question6
#write a python program to count the total number of words in a text file 

with open("student.txt","r")as f:
   ch=f.read()
   print(len(ch))

#question7
#write a python program to count the total number of characters in a text

with open("student.txt","r")as f:
   words=f.readline()
   print(len(words))

#question9
#write a python program to search for a given word in a text file and display whether  it is found or not.

with open("student.txt","r")as f:
    words=f.read()
    d=str(input("enter "))
    if d  in words:
        print("yes")
    else:
        print("no")

#question10
#Write a python program to copy the contents of one text file (source.txt)into another  file(destination.)

with open("student.txt","r")as f:
   h=f.read()
   with open("destination.txt","w")as g:
      g.write(h)
      
      


