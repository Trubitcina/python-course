import re
import sys


data = sys.stdin.read()
results = re.findall('(\d*(111|222|333|444|555|666|777|888|999|000)\d*)', data)
for i in results:
    print(i[0])
