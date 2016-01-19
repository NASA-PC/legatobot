'''
Displays commands for the bot.
'''

class Handler:
    priority = -100;

    def __init__(self, brain):
        self.brain = brain; # Brain is not used in this example, but it is useful if you want i.e the name of the bot

    def canHandle(self, msg):
        return msg.command == "PRIVMSG" and msg.msg == "#help";

    def handle(self, msg, resp):
        resp.send("#XdY to roll Y-sided dice x times, #stats to generate stats #clearstats to clear stats, #4chan for latest /balt/ thread, #8chan for the /balt/ board, #todo to see the To-Do list.', msg.re());
