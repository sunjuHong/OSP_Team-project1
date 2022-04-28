#!/usr/bin/python3
from our_pkg.b2h import *
from our_pkg.setFt import *
#from our_pkg.fibo import *

def print_menu():
	menu = input("Select menu: 1)b2h 2)set 3)fibo 4)exit ?")
	return int(menu)



if __name__=='__main__':
	while 1:
		n = print_menu()
		if n == 4:
			break
		elif n == 1:
			our_pkg.b2h()
		elif n == 2:
			our_pkg.setFt()
#elif n == 3:
#our_pkg.fib()
		else:
			print("worng number! select 1~4")
		
	


