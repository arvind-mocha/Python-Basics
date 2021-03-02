#this is second file

#double underscore name double underscore (__name__) is the special variable

#if this file is executed print(__name__) gives __main__
#if this file is imported print(__name__) gives imported file name

import special_variable_1       #check this file for complete understanding

if __name__=="__main__":
    print("i am executed and i am second file so")
    print(__name__,"is printed")  # it acts as first file since we are running this file