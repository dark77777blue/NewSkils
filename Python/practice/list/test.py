# encoding=utf-8
#########################################################################
#File Name: test.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-21 11:14:56
#Last modified: 2017-10-21 11:34:54
#########################################################################
#!/usr/bin/env python

import os








if __name__ == "__main__":
	print(list(range(1, 11)))

	l = [x * x for x in range(1, 11)]
	print(l)

	l = [x * x for x in range(1, 11) if x % 2 == 0]
	print(l)

	l = [m + n for m in 'ABC' for n in 'XYZ']
	print(l)

	print('===================================================')

	l = [d for d in os.listdir('/home/python')]
	print(l)

	print('===================================================')

	d = {'x':'A', 'y':'B', 'z':'C'}
	for k, v in d.items():
		print(k, '=', v)


	l = [k + '=' + v for k, v in d.items()]
	print(l)

	L = ['Hello', 'World', 'IBM', 'Apple']
	l = [s.lower() for s in L]
	print(l)




















