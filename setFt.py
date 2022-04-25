#!/usr/bin/python
import sys

#1. input integer list
print("input the 1st list: ",end='')
listA=input()
print("input the 2nd list: ",end='')
listB=input()

#2. convert list into set
setA=map(int,listA.split())
setB=map(int,listB.split())
setA=set(setA)
setB=set(setB)

#3. set union, intersection
setUnion=setA.union(setB)
setIntersection=setA.intersection(setB)

#4. convert set into list
setUnion=list(setUnion)
setIntersection=list(setIntersection)

if __name__=='__main__':
	print("union: ",setUnion)
	print("intersection: ",setIntersection)
