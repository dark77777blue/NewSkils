# encoding=utf-8
#########################################################################
#File Name: test.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-30 16:19:23
#Last modified: 2017-10-31 11:54:43
#########################################################################
#!/usr/bin/env python

import os

if __name__ == '__main__':

	'''
	print(os.name)
	print(os.uname())
	print(os.environ.get('SHELL'))
	print(os.environ.get('PATH'))
	'''

	print(os.path.abspath('.'))
	try:
		pass
		#os.mkdir('./testdir')
	except FileExistsError as e:
		print('except:', e)
	finally:
		print('finally...')



	try:
		os.rmdir('./testdir')
	except FileNotFoundError as e:
		print('except:', e)
	finally:
		print('finally...')

	print('END')



