# encoding=utf-8
#########################################################################
#File Name: process.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-31 14:31:49
#Last modified: 2017-10-31 14:40:33
#########################################################################
#!/usr/bin/env python

from multiprocessing import Process
import os



def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target=run_proc, args=('test',))
	print('Child process will start.')
	p.start()
	p.join()
	print('Child process end.')


