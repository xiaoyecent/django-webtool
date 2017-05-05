#coding: utf-8
import json
import requests

def ipapi(ip):
	url = 'http://api.map.baidu.com/location/ip?ak=xxxxxxxxx&coor=bd09ll&ip=' + ip
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	r = requests.get(url, headers=headers, timeout=6)
	jsdic = json.loads(r.content)
	if jsdic.has_key('content'):
		city = jsdic['content']['address']
		pointx = jsdic['content']['point']['x']
		pointy = jsdic['content']['point']['y']
	return city, pointx, pointy
	
def getmap(x, y):
	im = 'http://api.map.baidu.com/staticimage/v2?ak=xxxxxxxxx&mcode=666666&center=' + x + ',' + y + '&width=500&height=300&zoom=11'
	return im
'''if __name__ == '__main__':
	ipapi(ip)'''
