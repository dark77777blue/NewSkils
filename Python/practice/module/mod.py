# encoding=utf-8
#########################################################################
#File Name: mod.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-23 17:23:43
#Last modified: 2017-10-23 17:29:15
#########################################################################
#!/usr/bin/env python

def _private_1(name):
	return 'Hi, %s' % name

def _private_2(name):
	return 'Hi, %s' % name

def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)
