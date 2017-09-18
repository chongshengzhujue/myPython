import urllib2
import re
import urlparse

# def download(url):
# 	print "downloading:", url
# 	try:
# 		return urllib2.urlopen(url).read()
# 	except urllib2.URLError as e:
# 		print "download error:", e.reason
# 		html = None
# 		return html

# def download(url, numRetrys):
# 	print "downloading:", url
# 	try:
# 		return urllib2.urlopen(url).read()
# 	except urllib2.URLError as e:
# 		print "download error:", e.reason
# 		html = None
# 		if numRetrys > 0:
# 			if hasattr(e, "code") and 500 <= e.code < 600:
# 				print "=========="
# 				return download(url. numRetrys-1)
# 		return html

def download(url, user_agent="wswpssa", numRetrys=2):
	print "downloading:", url
	headers = {"User-agent" : user_agent}
	request = urllib2.Request(url, headers = headers)
	try:
		return urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print "download error:", e.reason
		html = None
		if numRetrys > 0:
			if hasattr(e, "code") and 500 <= e.code < 600:
				print "=========="
				return download(url. numRetrys-1)
		return html

def link_crawler(seed_url, link_regex):
	crawl_queue = [seed_url]
	while crawl_queue:
		url = crawl_queue.pop()
		html = download(url)
		seen = set(crawl_queue)
		for link in get_links(html):
			if re.match(link_regex, link):
				link = urlparse.urljoin(seed_url, link)
				if link not in seen:
					seen.add(link)
					crawl_queue.append(link)

def get_links(html):
	weboage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.I)
	return weboage_regex.findall(html)

link_crawler("http://example.webscraping.com/", "/(index|view)")























