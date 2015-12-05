import re
import requests

mails_in = open('/home/nina/Загрузки/links.txt', 'r')
mails = mails_in.readlines()

addresses = ''
for i in mails:
    link = requests.get(mails)
    addresses += link.text

address = re.findall('(\w+([._]\w+)*@\w+([._]\w+)*)', addresses)
emails = []
for email in address:
    if email[0] not in emails:
        emails.append(email[0])

mails_out = open('/home/nina/Bio_Py/email_addresses.txt', 'w')
mails_out.write("\n".join(emails))