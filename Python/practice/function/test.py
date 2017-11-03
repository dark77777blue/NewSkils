# encoding=utf-8
#########################################################################
#File Name: test.py
#Author: Don Hu
#Mail: hudeng@staff.sina.com.cn
#Create Time: 2017-10-18 16:56:44
#Last modified: 2017-10-21 18:42:56
#########################################################################
#!/usr/bin/env python

from functools import reduce

def add(x, y):
	return x + y

def fn(x, y):
	return x * 10 + y



if __name__ == '__main__':
	#r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
	#print(list(r))
	#print(tuple(r))
	#print(set(r))


	print(reduce(add, [1, 3, 5, 7, 9]))
	print(reduce(fn, [1, 3, 5, 7, 9]))









