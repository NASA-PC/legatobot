'''
Some silly and innocent bullyi... jokes & Warnings to nervous individuals.
'''
import random

class Handler:
    priority = -1;

    def __init__(self, brain):
        self.brain = brain; # Brain is not used in this example, but it is useful if you want i.e the name of the bot
        self.lastNick = '';
        self.spamCount = 1;

    def canHandle(self, msg):
        msg.text = ""

        if(msg.command == "PRIVMSG"):

            # Shut up function including funny naughty arrays
            if(msg.contains("shut up") and msg.contains(self.brain.botnick)):
                with open("curses_adj.txt") and open("curses_nou.txt") as f:
                    curse_adj = [line.rstrip("\n") for line in open("curses_adj.txt")]
                    curse_nou = [line.rstrip("\n") for line in open("curses_nou.txt")]
                    msg.text = "fuck off you " + curse_adj[random.randint(0, len(curse_adj) -1)] + " " + curse_nou[random.randint(0, len(curse_nou) -1)];
                    return True
                
            # Insults on demand
            '''if(msg.contains("#insult") and msg.contains()):
                with open("curses_adj.txt") and open("curses_nou.txt") as f:
                    curse_adj = [line.rstrip("\n") for line in open("curses_adj.txt")]
                    curse_nou = [line.rstrip("\n") for line in open("curses_nou.txt")]
                    msg.text = "you're a " + curse_adj[random.randint(0, len(curse_adj) -1)] + " " + curse_nou[random.randint(0, len(curse_nou) -1)];
                    return True'''

            # Channel function
            if(msg.contains("http") and msg.contains("youtu")):
                msg.text = "only on my channel";
                return True;

            # PSA function
            if(msg.contains("finn")):
                psa = ["Respect our environment, put a finn in the bin!",
                       "Have you put a Finn in the bin today?",
                       "Get back in that bin, Finn!",
                       "Once I knew a friendly Finn\nhe lived inside a dingy bin",
                       "If I perchance was born a Finn\nI'd spend my days inside a bin",
                       "Little Finn, don't run from the bin\nEvery Finn must go in the bin"]
                
                msg.text = psa[random.randint(0, len(psa) - 1)]
                return True;

            # Funny reply
            with open("curses_nou.txt") as curses:
                msgWords = msg.msg.split(" ")
                for curse in curses:
                    curse = curse.rstrip("\n")
                    if (curse in msgWords and msg.contains("you")):
                        if (msg.contains("fuck")): # If it has fuck, add some fucking
                            msg.text = "yeah you fucking " + curse;
                            return True;
                        else:
                            msg.text = "yeah you " + curse;
                            return True;
                        
        return msg.command == "PRIVMSG";

    def handle(self, msg, resp):
        if(msg.user != self.lastNick):
            self.spamCount = 1;
        else:
            self.spamCount += 1;

        self.lastNick = msg.user;

        if(self.spamCount == 5):
            resp.send("Shh, {0}, calm down.".format(msg.user), msg.re());

        if(self.spamCount == 10):
            resp.send("oh wow", msg.re());

        if(self.spamCount == 20):
            resp.send("SHUT THE FUCK UP {0}".format(msg.user), msg.re());

        resp.send(msg.text, msg.re());
