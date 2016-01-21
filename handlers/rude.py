'''
Some silly and innocent bullyi... jokes. :)
'''
import random

class Handler:
    priority = -1;

    # Array for funny naughty words
    curses = ["homo", "dildo", "scrub", "penishole", "fag",
    "madman", "refugee", "immigrant", "nigger", "shitskin",
    "scrotum", "banaan", "equine vaginal cavity", "vagina",
    "punk", "bag", "furry", "error", "fig", "noob", "busta"]

    def __init__(self, brain):
        self.brain = brain; # Brain is not used in this example, but it is useful if you want i.e the name of the bot

    def canHandle(self, msg):
        msg.text = ""

        if(msg.command == "PRIVMSG"):
            # Shut up if
            if(msg.contains("shut up") and msg.contains(self.brain.botnick)):
                msg.text = "fuck off";
                return True;

            # Channel if
            if(msg.contains("http") and msg.contains("youtu")):
                msg.text = "only on my channel";
                return True;

            # Finns if
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
            for curse in self.curses:
                if (msg.contains(curse) and msg.contains("you")):
                    if msg.contains("fuck"): # If it has fuck, add some fucking
                        msg.text = "yeah you fucking " + curse;
                        return True;
                    else:
                        msg.text = "yeah you " + curse;
                        return True;

        return False;

    def handle(self, msg, resp):
        resp.send(msg.text, msg.re());
