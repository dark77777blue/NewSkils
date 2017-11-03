# encoding=utf-8
#########################################################################
#File Name: subprocess.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-31 14:58:01
#Last modified: 2017-11-02 15:42:44
#########################################################################
#!/usr/bin/env python

import subprocess

if __name__ == '__main__':
	print('$ nslookup www.python.org')
	r = subprocess.call(['nslookup', 'www.python.org'])
	print('Exit code:', r)




