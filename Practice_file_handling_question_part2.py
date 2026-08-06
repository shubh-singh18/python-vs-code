#write a data in file

file=open("notes.txt","w")
data=file.write("Hello everyone")
print(data)

#read a data in file

with open("notes.txt","r") as f:
    data=f.read()
    print(data)


#append a new data in file

with open("notes.txt","a")as f:
    data=f.write("devansh")
    print(data)

#all lines are read

with open("notes.txt","r")as f:
    data=f.readlines()
    print(data)

#read lines 1 to 4 only

with open("notes.txt","r")as f:
    for i in range(1,5):
        data=f.readline()
        if i>=1:
            print(data)


#how many words are present in file count

with open("notes.txt","r")as f:
    data=f.readline()
    print(len(data))


#name=input("enter your name")
#file=open("notes.txt","w")
#file.write(name)
#file.close()
#print("data saved successfully")

#create a file and write student detail.
with open("fill.txt","w")as f:
    data=f.write("student-> shubhsingh"   \
                   " marks->78" \
                 " good performance")
    print(data)
 

#Read all data from a file.
with open("fill.txt","r")as f:
    data=f.read()
    print(data)

#append new data to an existing file.
with open("fill.txt","a")as f:
    data=f.write("  python")
    print(data)

#Search for a word in a file
with open("fill.txt","r")as f:
    data=f.read()
if "python" in data:
    print("word are present")
else:
    print("word not present")

#Display only even-numberes lines from a file

with open("fill.txt","r")as f:
    data=f.readlines()
    for i in range(1,20):
        if i%2==1:
            print(data[i])





