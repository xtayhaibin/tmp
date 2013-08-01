import os
import time

if __name__ == '__main__':
    while True:
	time.sleep(5)
    	os.system('cat /proc/loadavg > loadavg.html')

