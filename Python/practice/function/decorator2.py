# encoding=utf-8
#########################################################################
#File Name: decorator2.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-23 11:07:33
#Last modified: 2017-10-23 11:26:10
#########################################################################
#!/usr/bin/env python

import functools

def log(text):
	def decorator1(func):
		@functools.wraps(func)		#####################
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
		#wrapper.__name__ = func.__name__
	return decorator1


@log('execute')
def now():
	print('2015-3-25')


if __name__ == '__main__':
	now()
	print(now.__name__)

