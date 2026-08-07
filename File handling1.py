#file=open("reading.txt","r")
#data=file.read()
#print(data)



#write a progeram to read a text from a given file reading.txt and find whether it contains the world my

#file=open("reading.txt","r")
#data=file.read()
#data=data.lower()
#if "my" in data:
 #   print("my world present in reading file")
#else:
 #   print("my world no present in reading file")

#file=open("reading.txt","w")
#data=file.write("hello,my name is shubh singh chauhan\n hello world")
#print(data)

#with open("reading.txt","r") as f:
 #   for i in range(1,2):
  #      data=f.readline()
   #     if i>=1:
    #       print(data,end="")

#with open("reading.txt","r") as f:
#    data=f.readlines()
 #   print("output of readlines function",data)
  #  print("number of lines in file",len,data)

#file=open("reading.txt","r")
#data=file.read(12)
#print(data)

#with open("reading.txt","r") as f:
#    data=f.read(10)
#    print(data)

#Read entire file
#with open("reading.txt","r") as f:
 #   data=f.read()
  #  print(data)

# Read line by line

#with open("reading.txt","r") as f:
#    line1=f.readline()
 #   line2=f.readline()
  #  line3=f.readline()
   # print(line1)
   # print(line2)
   # print(line3)

#Read all lines

with open("reading.txt","r")as f:
    line=f.readlines()
    print(line)