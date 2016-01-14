'''
Displays the To-Do list.
'''
class Handler:
    def __init__(self, brain):
        self.brain = brain; # Vrain is not used in this example, but it is usefull if you want i.e the name of the bot

    def canHandle(self, msg):
        return msg.command == 'PRIVMSG' and msg.msg == '#todo';

    def handle(self, msg, resp):
        resp.send('Just do it, fam!', msg.re())
        #for line in urllib.urlopen("https://raw.githubusercontent.com/Thorndrop/legatobot/master/todo.txt"): # Alternative way
        for line in open("todo.txt"):
            resp.send(line, msg.re())
