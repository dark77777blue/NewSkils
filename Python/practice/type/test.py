# encoding=utf-8
#########################################################################
#File Name: test.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-25 15:15:33
#Last modified: 2017-10-25 20:05:45
#########################################################################
#!/usr/bin/env python

import types




def my_func():
	pass

class Animal(object):
	pass





if __name__ == '__main__':
	print(type('123'))
	print(int)
	print(type(int('123')))
	T = type(1)
	print(type(T('123')))
	T = type('123')
	print(T)
	print(type(T(123)))
	
	print(type(None))
	print(type(True))
	print(type(abs))

	print(type(my_func))

	an = Animal()
	print(type(Animal))
	print(type(an))

	print("#############################")

	print(type(123) == type(456))
	print(type(123) == int)
	print(type('abc') == str)
	print(type('abc') == type(123))

	print("#############################")

	print(type(my_func) == types.FunctionType)
	print(type(abs) == types.BuiltinFunctionType)
	print(type(lambda x: x) == types.LambdaType)
	print(type((x for x in range(10))) == types.GeneratorType)











