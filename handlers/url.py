'''
HTTP html title reader
'''
import sys
import re

if sys.version_info < (3, 0):
    import urllib2
    def getUrlData(url):
        return urllib2.urlopen(url).read();
    
    def getContentType(url):
        try:
            result = urllib2.urlopen(url).info();
            return result.gettype()
        except:
            return None;
            
else:
    import requests
    def getUrlData(url):
        return requests.get(url = url).text;

    def getContentType(url):
        try:
            return requests.head(url = url).headers.get('Content-Type');
        except:
            return None;

LINK_REGEX = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

class Handler:
    
    def __init__(self, brain):
        self.brain = brain;
    
    def canHandle(self, msg):
        
        if(msg.command == 'PRIVMSG' and msg.contains("http")):
            link = re.findall(LINK_REGEX, msg.msg)
            return len(link) > 0;
        
    def handle(self, msg, resp):
        link = re.findall(LINK_REGEX, msg.msg)[0];
        
        contentType = getContentType(link);
        if(contentType and contentType.find('text/html') != -1):
            html = getUrlData(link);
            title = re.search('<title>([^<]+)', html);
            if(title):
                title = title.group(1);
                if(link.startswith('http://youtu') or link.startswith('https://youtu')):
                    title = 'Only on my channel: ' + title;

                resp.send(title, msg.re());

