'''
Greets anonkun and anybody who greets bot.
'''
class Handler:
    priority = 10;

    def __init__(self, brain):
        self.brain = brain;


    def canHandle(self, msg):
        msg.isAnonkun = False;
        msg.type = '';

        if(msg.command == 'JOIN' and msg.user == 'anonkun[lt]'):
            msg.isAnonkun = True;
            return True;

        if(msg.command == 'PRIVMSG'):
            if(msg.contains('tere ' + self.brain.botnick)):
                msg.type = 'Tere';
                return True;

            if(msg.contains('hello ' + self.brain.botnick)):
                msg.type = 'Hello';
                return True;

            if(msg.contains('bye')):
                msg.type = 'bye';
                return True;

        return False;


    def handle(self, msg, resp):
        if(msg.isAnonkun):
            resp.send('hello {0} :3'.format(msg.user), msg.re());
            return;

        if(msg.type == 'bye'):
            exclamation = '';
            if(msg.msg.find('!') != -1):
                exclamation = '!';

            resp.send('bye {0}{1}'.format(msg.user, exclamation), msg.re());
            return;

        resp.send('{0} {1}!'.format(msg.type, msg.user), msg.re());
