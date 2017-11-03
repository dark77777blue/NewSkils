# encoding=utf-8
#########################################################################
#File Name: test.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-28 10:16:12
#Last modified: 2017-10-28 10:19:31
#########################################################################
#!/usr/bin/env python


class Hello(object):
	def hello(self, name = 'world'):
		print('Hello, %s.' % name)



if __name__ == '__main__':
	pass
	h = Hello()
	print(h.hello())
	print(type(h))
	print(type(Hello))



