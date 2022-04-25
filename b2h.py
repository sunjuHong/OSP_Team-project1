#!/usr/bin/python3

import sys

def b2h():
	a = input("input bin number: ")
	b = int(a,2)
	print("hexa number: %s" % hex(b))
	print()

if __name__ == '__main__':
	b2h()
