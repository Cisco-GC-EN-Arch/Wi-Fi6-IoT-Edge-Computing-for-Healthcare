import os
import time

os.popen('cd /home')
while True:
    os.popen('python /bin/lodestar27_scan.py >> mylog.txt')
    time.sleep(20)
    os.popen('curl -T mylog.txt --user username:password ftp://your.server.ip.address/mylog.txt')
    time.sleep(10)
    os.popen('rm -rf mylog.txt')
    time.sleep(26)
