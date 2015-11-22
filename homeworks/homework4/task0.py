__author__ = 'Nina'


f = open('/home/nina/Bio_Py/yazkora.txt', 'r')
contents = f.read()
unit_text = contents.split('.')
f2 = open('/home/nina/Bio_Py/answer.txt', 'w')
for words in unit_text:
    word = words.split(' ')
    for adjective in word:
        if adjective[-2::] == 'yo':
            f2.write(adjective + ' ')
        else:
            f2.write('\n')
f.close()
f2.close()
