#!/usr/bin/env python

import urllib2, urllib, sys, json
from optparse import OptionParser

url = "http://domains.yougetsignal.com/domains.php"

contenttype = "application/x-www-form-urlencoded; charset=UTF-8"
domain1 = []

def banner():
    
                                      
    print "\n\n"                                  
    print " ,---.  ,---. ,--,--,  ,---.  ,--,--." 
    print "(  .-' | .-. :|      \(  .-' ' ,-.  | "
    print ".-'  `)\   --.|  ||  |.-'  `)\ '-'  | "
    print "`----'  `----'`--''--'`----'  `--`--' "
    print "\n\n"
                                      

def request(target, httpsproxy=None, useragent=None):
	global contenttype

	if not useragent:
		useragent = "Mozilla/5.0 (X11; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0 Iceweasel/22.0"
	else:
		print "["+ bc.G + "+" + bc.ENDC + "] User-Agent: " + useragent

	if httpsproxy:
		print "["+ bc.G + "+" + bc.ENDC + "] Proxy: " + httpsproxy + "\n"
		opener = urllib2.build_opener(
                urllib2.HTTPHandler(),
                urllib2.HTTPSHandler(),
                urllib2.ProxyHandler({'http': 'http://' + httpsproxy}))
		urllib2.install_opener(opener)

	postdata = [('remoteAddress',target),('key','')]
	postdata = urllib.urlencode(postdata)

	request = urllib2.Request(url, postdata)

	request.add_header("Content-type", contenttype)
	request.add_header("User-Agent", useragent)
	try:
		result = urllib2.urlopen(request).read()
	except urllib2.HTTPError, e:
		print "Error: " + e.code
	except urllib2.URLError, e:
		print "Error: " + e.args

	obj = json.loads(result)
	return obj


def output(obj):
	print   "Status:" + obj["status"]
	if obj["status"] == "Fail":
		message = obj["message"].split(". ")
		print   "Error:     " + message[0] + "."
		sys.exit(1)

	print "Domains:   " +obj["domainCount"]
	print "Target:    " + obj["remoteAddress"]
	print "Target IP: " + obj["remoteIpAddress"]

	print "\nResults:"

	for domain, hl in obj["domainArray"]:
		print  domain
		domain1.append(domain)
def wordpress_checker():
    print "\n WEBSITES WHICH ARE RUNNING ON WORDPRESS"
    print "=========================================="
    for i in domain1:
        i = "http://"+i
        try:
            raw = urllib2.urlopen(i).read()
            if "wp-content" in raw:
                print i + " is using wordpress"
        except:
            pass
def main():
        banner()
	target = raw_input("Enter the domain name or ip: ")
	obj = request(target)
	output(obj)


if __name__ == "__main__":
	try:
		main()
		wordpress_checker()
	except KeyboardInterrupt:
		print "["+ bc.R + "!" + bc.ENDC + "] KeyboardInterrupt detected!\nGoodbye..."
		sys.exit()
