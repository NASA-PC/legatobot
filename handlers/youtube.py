'''
Youtube title reader
'''
import sys
import re

if sys.version_info < (3, 0):
    import urllib2
    def getUrlData(url):
        return urllib2.urlopen(url).read();
else:
    import requests
    def getUrlData(url):
        return requests.get(url = url).text;

LINK_REGEX = 'https?://(?:www\.)?youtu(?:be\.com/watch\?v=|\.be/)([\w\-]+)(&(amp;)?[\w\?=]*)?'

class Handler:
    
    def __init__(self, brain):
        self.brain = brain;
    
    def canHandle(self, msg):
        
        if(msg.contains("http") and msg.contains("youtu")):
            link = re.search(LINK_REGEX, msg.msg)
            return hasattr(link, 'group');
        
    def handle(self, msg, resp):
        link = re.search(LINK_REGEX, msg.msg).group(0);
        
        html = getUrlData(link);
        title = re.search('<title>([^<]+)', html).group(1);
        
        resp.send("Only on my channel: " + title, msg.re());