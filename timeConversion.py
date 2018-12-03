#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):

    hh = s[0:2]
    am_pm = s[8:10]
    if am_pm == 'PM':
        if hh == '12':
            pass
        else:
            hh = int(hh)
            hh += 12
            hh = str(hh)
    elif am_pm == 'AM':
        if hh == '12':
            hh = '00'
    new_s = hh+s[2:8]
    # print(new_s)
    return new_s
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    f.write(result + '\n')

    f.close()
