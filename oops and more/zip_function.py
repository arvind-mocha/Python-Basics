name=["arvind","ashok","chandru","mani"]
jobs=["apple","google","micro soft","intel",'u']

zipped=list(zip(name,jobs))#zip combines two variable like list,set ect 

zipped1=zip(name,jobs)#it gives only address

zipped2=dict(zip(name,jobs))

print(zipped)
print(zipped1)
print(zipped2.values())
