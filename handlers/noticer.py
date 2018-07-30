'''
Notices when a new user joins. Schedules user to enable voice.
See also ../pumis/voicer.py
'''

from pumis import voicer as v


class Handler:
    priority = 0;

    def __init__(self, brain):
        self.brain = brain; # Brain is not used in this example, but it is useful if you want i.e the name of the bot

    def canHandle(self, msg):
        return msg.command == 'JOIN';

    def handle(self, msg, resp):
        v.scheduleUser(msg.user);
