# -*- coding: UTF-8 -*-
'''
Searches from WIkipedia
'''

from bs4 import BeautifulSoup
import urllib2

def wiki(components): # #wiki <search term>
    # Returns a wiki link and the first paragraph of the page

    main_page = "https://en.wikipedia.org/wiki/Main_Page"

    wlink = components.split("#wiki ") # notice the trailing space
    if 1 == len(wlink): # no search term given, the Main_Page is "displayed"
        response = main_page
    else:
        search_term = wlink[1].lstrip().replace(" ", "_")

        if len(search_term) < 1:
            response = main_page
        else:
            response = "https://en.wikipedia.org/wiki/" + search_term

    response = response + "\r\n" #+ get_paragraph(response)

    return response.encode("utf-8")

    print(wiki)

'''def get_paragraph(response, wlink):
    # Gets the first paragraph from a wiki link

    msg = ""
    try:
        page_request = urllib2.Request(wlink)
        page_request.add_header("User-agent", "Mozilla/5.0")
        page = urllib2.urlopen(page_request)
    except IOError:
        msg = "Cannot acces link!"
    else:

        soup = BeautifulSoup(page)
        msg = "".join(soup.find("div", { "id" : "bodyContent"}).p.findAll(text=True))

        while 460 < len(msg): # the paragraph cannot be longer than 510
            # characters including the protocol command
            pos = msg.rfind(".")
            msg = msg[:pos]

    return msg'''

class Handler:
    priority = 10000; ''' It is used to determine which handler should be checked canHandle() first.
    Two handlers must not have the same priority (unless priority is 0)
    If priority is not defined, it is considered to be 0. '''

    def __init__(self, brain):
        self.brain = brain; # Brain is not used in this example, but it is useful if you want i.e the name of the bot

    def canHandle(self, msg):
        return msg.command == "PRIVMSG" and msg.msg.startswith("#wiki")

    def handle(self, msg, resp):
        responseText = wiki(msg.msg)
        resp.send(responseText, msg.re());
