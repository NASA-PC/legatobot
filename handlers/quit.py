
class Handler:
    def __init__(self, brain):
        self.brain = brain; #brain is not used in this example, but it is usefull if you want i.e the name of the bot


    def canHandle(self, msg):
        return msg.command == 'PRIVMSG' and msg.msg.lower() == ('gtfo ' + self.brain.botnick).lower();


    def handle(self, msg, resp):
        resp.sendCommand('QUIT :rude tbh')

