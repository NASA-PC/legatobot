class Handler:
    def __init__(self, brain):
        self.brain = brain; # Brain is not used in this example, but it is usefull if you want i.e the name of the bot


    def canHandle(self, msg):
        if (msg.command == 'PRIVMSG'):
            if(msg.msg == '#4chan' or msg.msg == '4chan'):
                msg.text = 'Here you go, fam: https://www.4chan.org/int/balt';
                return True;
            if(msg.msg == '#8chan' or msg.msg == '8ch'):
                msg.text = 'Here you go, fam: https://8ch.net/balt';
                return True;
        return False;

    def handle(self, msg, resp):
        resp.send(msg.text, msg.re());
