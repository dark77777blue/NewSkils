# encoding=utf-8
#########################################################################
#File Name: closure.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-23 08:25:08
#Last modified: 2017-10-23 08:32:56
#########################################################################
#!/usr/bin/env python


def count():
	def f(j):
		return lambda :j*j

	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs


if __name__ == '__main__':
	f1, f2, f3 = count()
	print(f1())
	print(f2())
	print(f3())

