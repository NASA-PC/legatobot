'''
---
Example pumi.
This pumi says hello and then dies.

---
resp = {
    send(msg) - sends PRIVMSG
    sendCommand(command) - sends any command
}
'''

class Pumi:
    interval = 1; #Intervl in seconds, how often Pumi should be executed, or in this particular example how long Pumi will wait before saying Hello.

    def __init__(self, brain):
        self.brain = brain; # Brain is not used in this example, but it is useful if you want i.e the name of the bot

    def isLithoku(self): #If this function returns False, pumi will not talk again :( Ever. Unless Legatobot is restarted.
        return True; #Die as soon as possible

    def talk(self, resp): #Do all the bloging
        resp.send("Hello everyone! :3"); # Send hello world message
