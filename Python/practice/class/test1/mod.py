# encoding=utf-8
#########################################################################
#File Name: mod.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-23 19:55:14
#Last modified: 2017-10-23 19:57:22
#########################################################################
#!/usr/bin/env python



class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))
