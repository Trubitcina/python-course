import re
import sys

data = sys.stdin.read()
result = re.sub('([\W]+)', ' ', data)
print(result)
