# -*- coding: UTF-8 -*-
'''
Searches from Google
'''
import json
import sys


if sys.version_info < (3, 0):
    import urllib
    import urllib2
    
    def quote(url):
        return urllib.quote_plus(url.encode("utf-8"));
    
    def getUrlData(url):
        return urllib2.urlopen(url).read();
else:
    import urllib.parse
    import requests
    def quote(url):
        return urllib.parse.quote_plus(url.encode("utf-8"));

    def getUrlData(url):
        return requests.get(url = url).text;


#What this is for?
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

def getSearchTerm(components):
    return  components[len("#google"):].strip();

def google(components): # #google <search term>

    response = "https://www.google.com/#q=" # if no search term given, the Main_Page is "displayed"
    query =  getSearchTerm(components);
    if len(query) > 0: 
        response += quote(query)

    return response

def getOneItem(data, index):
    return str(index) + ". " + data["items"][index]["title"] +" " + data["items"][index]["link"];

def googleResults(msg, resp):
    query =  getSearchTerm(msg.msg);
    if len(query) > 0:
        url = "https://www.googleapis.com/customsearch/v1?cx=005983647730461686104:qfayqkczxfg&key=AIzaSyCy6tveUHlfNQDUtH0TJrF6PtU0h894S2I&q=" + query
        data = json.loads(getUrlData(url));
        if data and "items" in data and len(data["items"]) > 3:
            for i in range(0, 3):
                text = getOneItem(data, i);
                if len(text) > 2:
                    resp.send(text, msg.re());
        
    pass

class Handler:
    priority = 10500; ''' It is used to determine which handler should be checked canHandle() first.
    Two handlers must not have the same priority (unless priority is 0)
    If priority is not defined, it is considered to be 0. '''

    def __init__(self, brain):
        self.brain = brain; # Brain is not used in this example, but it is useful if you want i.e the name of the bot

    def canHandle(self, msg):
        return msg.command == "PRIVMSG" and msg.msg.startswith("#google")

    def handle(self, msg, resp):
        responseText = google(msg.msg)
        resp.send(responseText, msg.re());
        googleResults(msg, resp);
