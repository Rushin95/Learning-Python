# get total difference in seconds

#!/bin/python
import time
import datetime
import sys

def get_seconds(t1,t2):
    zone_diff = (get_zone_seconds(t1)-get_zone_seconds(t2))
    t1 = t1.split(' ')
    t2 = t2.split(' ')
    dt1= datetime.datetime.strptime(' '.join(t1[1:-1]), "%d %b %Y %H:%M:%S")
    dt2= datetime.datetime.strptime(' '.join(t2[1:-1]), "%d %b %Y %H:%M:%S")
    td = dt1-dt2
    return int(td.total_seconds())-int(zone_diff)

def get_zone_seconds(t):
    t = t.split(' ')
    zone = "%.2f" % (float(t[-1])/100)
    zone_hour,zone_min = map(int,zone.split('.'))
    zone_seconds = abs(zone_hour)*3600 + zone_min*60
    if zone_hour>=0.00:
        return  zone_seconds
    else:
        return  -zone_seconds

def time_delta(t1, t2):
    # Complete this function
    return get_seconds(t1,t2)

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        t1 = raw_input().strip()
        t2 = raw_input().strip()
        delta = time_delta(t1, t2)
        print abs(delta)

# Sample Input:
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000
