#importing module
import itertools

#collecting given input data
dic= {'hello': ['doc1'],'my': ['doc1'],'name': ['doc1'],'is': ['doc1', 'doc2'],
'james': ['doc1', 'doc2'],'a': ['doc2'],'developer': ['doc2']}
print(" Given input :",dic)
print()

#using sorted in-built function to sort the data 
#syntax of sorted(iterable,key=None)
def fun(ele):
    return len(ele[1])
sorted_keys= sorted(dic.items(),key=fun)

# above code sorted only keys
def fun2(ele):
    return len(ele[1])
final=[]
#groupby function will take two inputs list or dict and key=None
s=itertools.groupby(sorted_keys,fun2)
for keyss,values in s:
    final.append(sorted(values))

print(" Generated output :  ",final)



