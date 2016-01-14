'''
Calms down users.
'''

class Handler:
    priority = -9000; # Execute only if nobody else handled

    def __init__(self, brain):
        self.brain = brain; # Brain is not used in this example, but it is usefull if you want i.e the name of the bot
        self.lastNick = '';
        self.spamCount = 1;

    def canHandle(self, msg):
        return msg.command == 'PRIVMSG';


    def handle(self, msg, resp):
        if(msg.user != self.lastNick):
            self.spamCount = 1;
        else:
            self.spamCount += 1;

        self.lastNick = msg.user;

        if(self.spamCount == 5):
            resp.send('Shh, {0}, calm down.'.format(msg.user), msg.re());

        if(self.spamCount == 10):
            resp.send('oh wow', msg.re());

        if(self.spamCount == 20):
            resp.send("YOU'RE ON FIRE, FAM!!!", msg.re());
