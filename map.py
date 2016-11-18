#!/usr/bin/env python

import sys
from decimal import *

# input comes from STDIN (standard input)
for data in sys.stdin:
        col = data.split(",")
        if len(col)==23 and col[4]!="":
                mag = Decimal(col[4])
				# Fetch only those records that match the criteria i. region vs count
                if(mag >= 3.0 and mag <= 6.0):
                        print '%s\t%s' % (col[21], 1)
                        #print '%s\t%s' % (col[4], 1)  ii. magnitude vs count