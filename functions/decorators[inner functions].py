#a simple division function
def div(a,b):
    print(a/b)

#a function which checks is divident is greater than the divisor if not swapping is done
def smart_div(func):#since smart div have inner function parameter func
                    #can have parameter[giving value for func inside the same function]
    def inner(a,b):
        if a < b:
            a,b=b,a     #swapping

        return func(a,b)#func is the parameter passed in smart_div and now func is having parameter
                        #since value passed in actual argument is a function so parameter func = function div
                        #[this gives swapped values] if doubts occurs in types of argument do check [types of arguments.py]

    return inner    #it returns func(a,b) which is swapped values

div1=smart_div(div) #now function div = parameter func
div1(4,8)

#this linkink is known as decorators