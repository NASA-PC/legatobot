'''
https://en.wikipedia.org/wiki/Magic_8-Ball
'''

import random

def mball(components): # Return a random entry from the shuffled list

    answers = ["It is certain.", "It is decidedly so.", "Without a doubt.", \
        "Yes - definitely.", "You may rely on it.", "As I see it, yes.",\
        "Most likely.", "Outlook good.", "Signs point to yes.", "Yes.", \
        "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", \
        "Cannot predict now.", "Concentrate and ask again.", "Don\'t count on it.", \
        "My reply is no.", "My sources say no.", "Outlook not so good.", \
        "Very doubtful."]
        
    response = ""

    if components.split("#ball"):
        # the user sent just the command, no garbage
        random.shuffle(answers)
        response = random.choice(answers)

    return response
    
class Handler:
    priority = 1000; ''' It is used to determine which handler should be checked canHandle() first.
    Two handlers must not have the same priority (unless priority is 0)
    If priority is not defined, it is considered to be 0. '''

    def __init__(self, brain):
        self.brain = brain; # Brain is not used in this example, but it is useful if you want i.e the name of the bot

    def canHandle(self, msg):
        return msg.command == "PRIVMSG" and msg.msg.startswith("#8ball")

    def handle(self, msg, resp):
        responseText = mball(msg.msg)
        resp.send(responseText, msg.re());
