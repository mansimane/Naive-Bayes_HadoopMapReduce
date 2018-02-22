#!/usr/bin/env python
import math
import sys
import re
def tokenizeDoc(cur_doc):
    return re.findall('\\w+',cur_doc)

dictlist = {}
Y = {}
Y_wstar = {}
Y_star = 0
event_prev = ""
cnt_prev = 0

for line in sys.stdin:
    m = line.split("\t")
    event = m[0]
    cnt = int(m[1].replace("\n",""))
    #print "event_prev", event_prev
    #print "event", event
    if event == event_prev:
        cnt_prev += cnt
    else:
        if event_prev != "":
            sys.stdout.write(event_prev)
            sys.stdout.write("\t")
            sys.stdout.write(str(cnt_prev))
            sys.stdout.write("\n")
            cnt_prev = cnt
            event_prev = event
        else:
            event_prev = event
            cnt_prev = cnt

#To print last event becuase it won't go in the if as there won't be any event after that
sys.stdout.write(event_prev)
sys.stdout.write("\t")
sys.stdout.write(str(cnt_prev))
sys.stdout.write("\n")
