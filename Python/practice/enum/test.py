# encoding=utf-8
#########################################################################
#File Name: test.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-28 09:58:13
#Last modified: 2017-10-28 10:06:04
#########################################################################
#!/usr/bin/env python



from enum import Enum


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))





if __name__ == '__main__':

	for name, member in Month.__members__.items():
		print(name, '=>', member, ',', member.value)
		print(type(name), type(member))

	print(type('abc'), type(Month))




