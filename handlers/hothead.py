'''
Some silly and innocent bullyi... jokes & warnings to nervous individuals.
'''
import random

class Handler:
    priority = -1;

    # Array for usernames, needs to be re-done to use /names, possibly imported to one of the main files
    names = ["ArnieBoi[SWE]", "arnie[se]", "pasta", "mr_soup",
             "MikeW", "zmpg", "NASA", "trikkyslikky", "LegatoBot",
             "anonkun[lt]"]

    def __init__(self, brain):
        self.brain = brain; # Brain  is useful if you want i.e the name of the bot
        self.lastNick = '';
        self.spamCount = 1;

    def canHandle(self, msg):
        msg.text = ""

        if(msg.command == "PRIVMSG"):

            # Shut up function including funny naughty arrays
            if(msg.contains("shut up") and msg.contains(self.brain.botnick)):
                with open('library\curses_adj.txt') and open('library\curses_nou.txt') as f:
                    curse_adj = [line.rstrip("\n") for line in open('library\curses_adj.txt')]
                    curse_nou = [line.rstrip("\n") for line in open('library\curses_nou.txt')]
                    msg.text = "fuck off you " + curse_adj[random.randint(0, len(curse_adj) -1)] + " " + curse_nou[random.randint(0, len(curse_nou) -1)];
                    return True
                
            # Insults on demand
            if (msg.contains("#insult")):
              msgWords = msg.msg.split(" ")
              insultIndex = msgWords.index("#insult")
              if (len(msgWords) >= insultIndex +2):
                  name = msgWords[insultIndex +1]
                  
                  if(name in self.names):
                      with open('library\curses_adj.txt') and open('library\curses_nou.txt') as f:
                          curse_adj = [line.rstrip("\n") for line in open('library\curses_adj.txt')]
                          curse_nou = [line.rstrip("\n") for line in open('library\curses_nou.txt')]
                          msg.text = "Hey" + " " + name +  " you're a " + curse_adj[random.randint(0, len(curse_adj) -1)] + " " + curse_nou[random.randint(0, len(curse_nou) -1)];
                          return True

              with open('library\curses_adj.txt') and open('library\curses_nou.txt') as f:
                  curse_adj = [line.rstrip("\n") for line in open('library\curses_adj.txt')]
                  curse_nou = [line.rstrip("\n") for line in open('library\curses_nou.txt')]
                  msg.text = curse_adj[random.randint(0, len(curse_adj) -1)] + " " + curse_nou[random.randint(0, len(curse_nou) -1)];
                  return True
                      
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
            with open('library\curses_nou.txt') as curses:
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
            
        if(self.spamCount == 15):
            resp.send("Sir, please stop this.", msg.re());

        if(self.spamCount == 20):
            resp.send("SHUT THE FUCK UP {0}".format(msg.user), msg.re());

        resp.send(msg.text, msg.re());
