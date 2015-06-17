#!/usr/bin/python
import random
import string
import sys


if len(sys.argv) > 1:
    N = int(sys.argv[1])
else:
    N = 10

c = ''.join(random.SystemRandom().choice(string.ascii_uppercase))
ostr = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N-1))
ostr = c+ostr
print(ostr)
