# Binary file handling
# A binary file stores data in the form of bytes .include image,(.jpg,.png),audio(.mp3),video(.mp4),PDFS,and executables files

#File handling with binary mode

# write mode

with open("binary.txt","wb")as f:
    print(f.write(b"Hello world\n"))
    print(f.write(b"python is a simple language\n"))

# Append mode

with open("binary.txt","ab")as f:
    print(f.write(b"devansh"))

#Read mode

with open("binary.txt","rb")as f:
  print(f.read())

# The seek() and tell() method
#Tell () method

# we can use tell() method to return current position of the cursor from begining of the file.
#The position(index) of first character in files is zero just like string index
#example

with open("binary.txt","r")as f:
   print(f.tell())

#Seek() method
# we can use seek() method to move cursor to specified location can you please seek the cursor to a particular location.
#example

with open("binary.txt","r")as f:
    print(f.seek(3))
    print(f.tell())