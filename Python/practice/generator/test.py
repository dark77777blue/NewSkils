# encoding=utf-8
#########################################################################
#File Name: test.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-21 11:45:47
#Last modified: 2017-10-21 16:51:23
#########################################################################
#!/usr/bin/env python


from collections import Iterable

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		#print(b)
		yield b
		a, b = b, a+b
		n = n + 1
	return 'done'

def odd(num):
	for i in range(num):
		print('step {}'.format(i))
		yield i




if __name__ == '__main__':
	L = [x * x for x in range(1, 11)]
	print(L)

	g = (x * x for x in range(1, 11))
	print(g)

	for node in g:
		print(node)

	'''
	print(next(L))
	print(next(L))
	print(next(L))
	print(next(L))
	print(next(L))
	print(next(L))
	'''

	print('=========================================================')

	g = fib(10)
	print(g)
	for node in g:
		print(node)

	print('=========================================================')

	g = odd(10)
	for i in g:
		print(i)
	
	g = fib(6)
	while True:
		try:
			x = next(g)
			print('g:', x)
		except StopIteration as e:
			print('Generator return value:{}'.format(e.value))
			break

	print(isinstance(g, Iterable))

