# encoding=utf-8
#########################################################################
#File Name: test2.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-30 13:40:39
#Last modified: 2017-10-30 13:43:31
#########################################################################
#!/usr/bin/env python

class FooError(ValueError):
	pass

def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' % s)
	return 10 / n




if __name__ == '__main__':
	print(foo(2))
	print(foo(0))

	print('END')



