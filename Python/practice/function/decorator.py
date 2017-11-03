# encoding=utf-8
#########################################################################
#File Name: decorator.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-23 10:09:01
#Last modified: 2017-10-23 11:30:14
#########################################################################
#!/usr/bin/env python

import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper


@log
def now():
	print('2015-3-25')




if __name__ == '__main__':

	now()
	print(now.__name__)



