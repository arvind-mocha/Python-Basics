#this is first file

#double underscore name double underscore (__name__) is the special variable

#if this file is executed print(__name__) gives __main__
#if this file is imported print(__name__) gives imported file name

#if this file is the first file and not a module it prints __main__
#module in the sense import file


print("hi")

if __name__!="__main__":
    print("i am not executed")
    print("i am from file 1 and i am imported")
    print("from", __name__)  # if you run this file it acts as first file and prints __main__
    # if you import this file then it acts as second file in that file and
    # __name__ is printed there as this (file name) which is special_variable_1

if __name__=="__main__":
    print("i am first file and i am executed")

print()



