#!/usr/bin/python3

import sys    

def fib():
    n=int(input('fibonacci number:'))

    previous=0
    current=1
    i=1
    v=0

    while i<=n:
        if i==n:
            v=current
        print(current,end=" ")
        temp=previous
        previous=current
        current+=temp
        i+=1
    print("")
    print('F',n,'=',v,sep="")





if __name__=='__main__':
    fib()
<<<<<<< HEAD
    


=======
>>>>>>> 0a7e65baf6667f38bd521b511bb95c12065dcf04
