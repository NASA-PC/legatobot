'''
Kicks spammers out of this idle heaven
'''

class Handler:

    def __init__(self, brain):
        self.brain = brain;

    def canHandle(self, msg):
        return msg.command == "PRIVMSG" and msg.user and msg.msg.startswith("Hey, I thought you guys might be interested")

    def handle(self, msg, resp):
        resp.sendCommand("KICK " + self.brain.channel + " " + msg.user + " :we don't like spam"); 
