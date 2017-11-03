# encoding=utf-8
#########################################################################
#File Name: thread.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-11-02 16:57:33
#Last modified: 2017-11-02 17:06:51
#########################################################################
#!/usr/bin/env python

import time, threading

def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('thread %s >>> %s' % (threading.current_thread().name, n))
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)



if __name__ == '__main__':
	print('thread %s is running...' % threading.current_thread().name)
	t = threading.Thread(target=loop, name = 'LoopThread')
	t.start()
	t.join()
	print('thread %s ended.' % threading.current_thread().name)
