# encoding=utf-8
#########################################################################
#File Name: test.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-31 12:30:27
#Last modified: 2017-10-31 13:29:32
#########################################################################
#!/usr/bin/env python

import pickle


if __name__ == '__main__':
	d = dict(name='Bob', age=20, score=88)
	p = pickle.dumps(d)
	print(p)
	with open('dump.txt', 'wb') as f:
		pickle.dump(d, f)



