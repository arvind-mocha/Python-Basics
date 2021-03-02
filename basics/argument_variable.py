#argv is argument variable which is allows user to pass input in as command line
#[python filename.py] this is the command line
#argv is used to pass input as cmd line  argument like this python filename.py 1 2 here 1 and 2 is the input and they are passed as cmd arguments
import sys
#no arvg[0] because argv[0] is the heading
x=sys.argv[1]#argv[1] is the first input
y=sys.argv[2]#argv[2] is the second input
print(x+y)

