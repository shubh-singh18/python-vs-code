# question1-> Write code to open a file named reading.txt in read mode.

file=open("reading.txt","r")
data=file.read()
print(data)

# question2-> Write a program to read a text from a given file reading.txt and find whether it contains the word live.

file=open("reading.txt","r")
data=file.read()
if "Live" in data:
    print("Live word present in a file")
else:
    print("Live word not present in a file")

# question3->What happens if you open a non -existing file in "r" mode?

file=open("hello.txt","r")
data=file.read()
print(data)

#question4-> open a file called report.txt in write mode.

file=open("reading.txt","w")
data=file.write("thanks you,hello ")
print(data)

#question5->Write code to open a file named reading.txt in append mode

file=open("reading.txt","a")
data=file.write("Shubhsinghchauhan\n hello shubh")
print(data)

#question6-> create a file names shubh_info.txt using "x" mode.
file=open("shubh.txt","x")
data=file.write("hello world all is good")
print(data)

#question7->Read a file named notes.txt and print the full content

with open("notes.txt","r")as f:
 data=f.read()
print(data)

#question8->Read only the first line of notes.txt.
with open("notes.txt","r")as f:
    line1=f.readline()
print(line1)

#question9->Print how many lines are present in notes.txt
with open("notes.txt","r")as f:
    list=f.readline()
    print("output of readlines function",list)
    print(len(list))