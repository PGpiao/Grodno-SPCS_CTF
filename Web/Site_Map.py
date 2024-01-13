import requests
import re

def main(url):

	flag_re = 'grodno{.*?}'
	req = requests.get(url)
	flag = re.findall(flag_re, req.text)
	print(flag[0])

if __name__=='__main__':
	url='http://ctf.mf.grsu.by/tasks/0448a5c387935239c9fa6e7d20f0c50f/sitemap.xml'
	main(url)
