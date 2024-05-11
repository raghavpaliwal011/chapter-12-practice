#map
def cube(x):
    return x*x*x
print (cube(2))
l = [1,2,3,4,5,6,7,8,9,10]
newl=list(map(cube,l))
print (newl)

#filter 
def filter_function(a):
    return a>4
newnewl = list(filter(filter_function,l))
print (newnewl)

#reduce
from functools import reduce
numbers = [3,5,4,7]
def mysum(x,y):
    return x+y
sum = reduce(mysum,numbers)
print (sum)