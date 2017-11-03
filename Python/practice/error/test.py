# encoding=utf-8
#########################################################################
#File Name: test.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-30 11:41:16
#Last modified: 2017-10-30 13:24:29
#########################################################################
#!/usr/bin/env python




if __name__ == '__main__':
	try:
		print('try...')
		r = 10 / int('1')
		print('result:', r)
	except ZeroDivisionError as e:
		print('ZeroDivisionError:', e)
	except ValueError as e:
		print('ValueError:', e)
	else:
		print('no error!')
	finally:
		print('finally...')

	print('END')
