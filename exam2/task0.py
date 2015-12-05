import re
import sys

text_in = open('/home/nina/Загрузки/hp5.txt', 'r')
HarryPotter = text_in.read()
SayWisp = re.findall('whispered ', HarryPotter)
#for word in SayWisp:
print(len(SayWisp))
