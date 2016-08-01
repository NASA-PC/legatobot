# -*- coding: UTF-8 -*-
'''
Searches from Google
'''
import json
import urllib
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def google(components): # #google <search term>

    main_page = "https://www.google.com/#q="

    wlink = components.split("#google ") # notice the trailing space
    if 1 == len(wlink): # no search term given, the Main_Page is "displayed"
        response = main_page
    else:
        search_term = wlink[1].lstrip()
        search_term = urllib.quote_plus(search_term)

        if len(search_term) < 1:
            response = main_page
        else:
            response = "https://www.google.com/#q=" + search_term

    response = response + "\r\n"

    return response.encode("utf-8")

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
