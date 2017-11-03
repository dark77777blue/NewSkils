# encoding=utf-8
#########################################################################
#File Name: test.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-23 18:08:55
#Last modified: 2017-10-23 19:58:58
#########################################################################
#!/usr/bin/env python

from mod import Student




if __name__ == '__main__':
	bart = Student('Bart Simpson', 59)
	lisa = Student('Lisa Simpson', 95)
	bart.print_score()
	lisa.print_score()
	print(bart)
	print(bart.__name)


