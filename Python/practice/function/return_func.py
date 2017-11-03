# encoding=utf-8
#########################################################################
#File Name: return_func.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-23 08:12:27
#Last modified: 2017-10-23 08:21:04
#########################################################################
#!/usr/bin/env python



def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum




if __name__ == '__main__':

	print(calc_sum(*list(range(101))))


	f = lazy_sum(1, 3, 5, 7, 9)
	print(f)
	print(f())



