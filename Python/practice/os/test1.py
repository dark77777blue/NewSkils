# encoding=utf-8
#########################################################################
#File Name: test1.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-31 11:59:27
#Last modified: 2017-10-31 12:06:05
#########################################################################
#!/usr/bin/env python


import os


if __name__ == '__main__':
	#l = [x for x in os.listdir('/home/python') if os.path.isdir(x)]
	l = [x for x in os.listdir('./') if os.path.isfile(x)]
	print(l)
	if os.path.isdir('./test1.py'):
		print('is path')

