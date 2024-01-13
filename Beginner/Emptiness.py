import requests
import re

def main(url):
	flag_re='grodno{.*?}'

	req=requests.get(url)
	flag=re.findall(flag_re,req.text)
	print(flag[0])





if __name__=='__main__':
	url='http://ctf.mf.grsu.by/tasks/023838760b034544becdb2d52f197ccd/'
	main(url)
