# encoding=utf-8
#########################################################################
#File Name: test.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-26 14:39:01
#Last modified: 2017-10-26 15:48:25
#########################################################################
#!/usr/bin/env python

class Student(object):
	def __init__(self):
		self._score = 70
		self._birth = 2014

	@property
	def score(self):
		return self._score
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value

	@property
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self, value):
		self._birth = value

	@property
	def age(self):
		return 2017 - self._birth

	def __getattr__(self, attr):
		return lambda :None




if __name__ == '__main__':
	s = Student()
	'''
	s.score = 60
	print(s.score)
	s.score = 101
	'''
	print(s.score)
	print(s.birth)
	print(s.age)
	s.birth = 2015
	print(s.age)
	#s.age = 10

	print('######################')
	print(s.abc)








