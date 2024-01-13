import requests
import jwt

def main(url):


	req=requests.get(url)
	data=req.headers['Authorization'].replace('Bearer ','')
	decoded_payload = jwt.decode(data, options={"verify_signature": False})
	print(decoded_payload)

if __name__=='__main__':
	url='http://ctf.mf.grsu.by/tasks/043db0a57ab0e71c37c90e784bed4517/'
	main(url)
