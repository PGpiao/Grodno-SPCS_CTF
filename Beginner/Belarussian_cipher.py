import re

f=open('bel_cipher.txt','r')
a=f.read().replace("працяжнiк","0").replace("кропка","1").replace(" ","")
f.close()
flag_re='grodno{.*?}'
characters = [chr(int(a[i:i+8], 2)) for i in range(0, len(a), 8)]
result = ''.join(characters)
flag=re.findall(flag_re,result)
print(flag[0])

