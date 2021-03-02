#generator is as same as iterator the differences are

    #1.since they are not special methods they dont need class sprcial method in the sence __method__()
    #2.generator creates a iterator
    #3.a generator is better tahn iterator

def cube():

    n=20

    for i in range(1,n):
        cu=i*i*i
        yield cu            #yeild is a keyword used in generators which creates a iterator

    return cu       #cu is retuned n times one by one since we use yeild

gen=cube()
for i in gen:
    print(i)