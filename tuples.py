#Tuples
"""
A tuple in Python is similar to list. The difference between the two is that we cannot change
the elelments of a tuple once it is assigned whereas we can change the elemens of a list.

In short tuple is an immutable list. A tuple can not be changes in any way once is created.

Characteristics 
.Ordered
.Unchangeable
.Allows duplicate
"""
#Creating tuple
#Empty
t1=()
print(t1)

#Create a tuple with single item
#it will print int 
t2=(2)
#it will print(str)
t2=("hello")
print(type(t2))

#For single item tuple(,) after char 
t1=(2,)
print(type(t1))
print(t1)

#Homogeneous tuple
t1=(1,2,3,4)
print(t1)
#Hetrogeneous tuple
t5=(1,2.5,True,[1,2,3])
print(t5)

#2D tuple
t5=(1,2,3,(4,5))
print(t5)

#Using type conversion
t6=tuple('hello')
print(t6)

#Acessing items
#indexing
#SLicing
print(t1)
print(t1[0])
print(t1[-1])


#Slicing
print(t1[0:4:2])
print(t1[-3:-1])
#reverse
print(t1[::-1])
print(t5)
print(t5[-1][0])

#Editing items
#throw error tuple object does not support item assignment
# t=[1,3,45]
# t[0]=100
# print(t)

#ADDING ITEMS
#not possible through error

#Deleting items
#delete whole tuple not its part
print(t1)
del t1

 #operations
#+ and *
t1=(1,2,3,4)
t2=(5,6,7,8)
print(t1+t2)
print(t1*3)
#membership
print(1 in t1)
print(1 not in t1)
#iteration
for i in t1:
    print(i)

#Tuple functions
#len/sum/min/max/sorted--list
t1=(1,2,3,4)
print(len(t1))
print(sum(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))
print(sorted(t1,reverse=True))

#count
t=(1,2,34,5)
print(t.count(5))
print(t)

#index
print(t.index(5))


#Difference between list and tuple
"""Syntax
Mutability
Speed
Memory
Built in functionality
Error prone
Usability"""

#Special syntax
#tuple unpacking
'''equal values will unpacking either error'''
a,b,c=(1,2,3)
print(a,b,c)

#if we want only 2 values use *others (print in[])
a,b,*others =(1,2,3,4)
print(a,b)
print(others)

#zipping tuple
# we have to convert it in list or tuple then it will print 1 element of a and first element of b
a=(1,2,3,4)
b=(5,6,7,8)
print(zip(a,b))
print(list(zip(a,b)))

