# encoding=utf-8
#########################################################################
#File Name: test.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-23 15:33:50
#Last modified: 2017-10-23 17:38:30
#########################################################################
#!/usr/bin/env python



' a test mudule '

__author__ = 'Michael Liao'

import sys
import mod

def test():
	args = sys.argv
	if len(args) == 1:
		print('Hello, world!')
	elif len(args) == 2:
		print('Hello, %s!' % args[1])
	else:
		print('Too many arguments!')

if __name__ == '__main__':
	test()
	print(mod._private_1('Don'))
	print(mod.greeting('Don'))





