'''
TODO: get all brain.handlers and they should format their own helps.
'''

class Handler:
    priority = -100;

    def __init__(self, brain):
        self.brain = brain; #brain is not used in this example, but it is usefull if you want i.e the name of the bot

    def canHandle(self, msg):
        return msg.command == 'PRIVMSG' and msg.msg == '#help';

    def handle(self, msg, resp):
        resp.send('#XdY to roll Y-sided dice x times, #stats to generate stats #clearstats to clear stats, #4chan for latest /balt/ thread, #todo to see the To-Do list.', msg.re());
