# encoding=utf-8
#########################################################################
#File Name: decorator3.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-23 14:16:07
#Last modified: 2017-10-23 14:34:07
#########################################################################
#!/usr/bin/env python

import functools


def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('begin call %s' % (func.__name__))
		func(*args, **kw)
		print('after call %s' % (func.__name__))
		#return
	return wrapper


@log
def f():
	print('f doing...')

###############################################################################
if __name__ == '__main__':
	f()

