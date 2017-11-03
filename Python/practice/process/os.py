# encoding=utf-8
#########################################################################
#File Name: os.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-31 14:16:19
#Last modified: 2017-10-31 14:26:29
#########################################################################
#!/usr/bin/env python


import os

if __name__ == '__main__':

	print('Process (%s) start...' % os.getpid())

	pid = os.fork()
	if pid == 0:	#子
		print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
	else:	#父
		print('I (%s) just created a child process (%s).' % (os.getpid(), pid))



