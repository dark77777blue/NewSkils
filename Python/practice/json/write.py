# encoding=utf-8
#########################################################################
#File Name: test.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-31 13:42:11
#Last modified: 2017-10-31 13:49:37
#########################################################################
#!/usr/bin/env python

import json




if __name__ == '__main__':
	d = dict(name = 'Bob', age = 20, score = 88)
	with open('./dump.txt', 'w') as f:
		#p = json.dumps(d)
		json.dump(d, f)
		#print(p)


