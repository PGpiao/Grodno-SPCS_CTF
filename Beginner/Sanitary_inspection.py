import re

flag_re = 'grodno{.*?}'
f=open('Our_rules.txt','r')
frw=f.read()
f.close()

req=re.findall(flag_re,frw)
print(req[1])