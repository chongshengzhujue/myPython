# -*- coding:utf-8 -*-  

import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

try:
	request = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(request)
	content = response.read().decode('utf-8')
	#print content
	pattern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?<h2>(.*?)</h2>.*?<div.*?'+
                         'content">(.*?)</span>',re.S)
	items = re.findall(pattern,content)
	print "ssssss"
	for item in items:
		print item[0],item[1]
except urllib2.URLError as e:
	if hasattr(e, "code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason
