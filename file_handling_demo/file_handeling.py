#file handeling

#open is a function which takes two parameters like file name and operations to be performed

#if your file is a which is of any type but not a sound,image,vedio the you can use these operatins which is passed as second parameter

#operations
    #read------r    used only to read
    #write-----w    used only to write and if a new word is written old word is deleted
    #append----a    used to write and when a nw word is written old word is not deleted

#if you have a img file then it is of binary type sowe must use binary operations

    #binary read-----br
    #binary write----bw

#reading
f=open('files_demo.txt','r') #if you open a file you need to store it in a variable

print(f.read())    #there are many function to read a file like readlines(),read()

#writing
f1=open('myfile','w')   #if you dont have a existing file then pyhton creates you a new file while using write function

print(f1.write("my name is arvind"))    #the old sentence gets removed when you write a new sentence

#append 'a'
f2=open("append.txt",'a')

print(f2.write(" i play games"))

#reading image

m=open('710789.jpg','br')

m1=open('death image.jpg','ba')

for i in m:
    m1.write(i)

