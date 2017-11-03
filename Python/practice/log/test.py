# encoding=utf-8
#########################################################################
#File Name: test.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-30 13:33:16
#Last modified: 2017-10-30 13:37:00
#########################################################################
#!/usr/bin/env python

import logging

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)




if __name__ == '__main__':
	main()
	print('END')


