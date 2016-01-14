import re
import math
import random

'''
Some geeks' game.
'''
userStats = {}

def rollDie(resp, numberOfDice, typeOfDie, usernick): # Dice rolling function
    if typeOfDie == "0":
        resp.send(":^)")
        return

    if numberOfDice == "":
        numberOfDice = "1"
    elif numberOfDice == "0":
        resp.send(":^)")
        return

    dieResults = []
    for i in range(int(numberOfDice)):
        dieResults.append(random.randint(1, int(typeOfDie)))

    resp.send(usernick + " rolls " + numberOfDice + "d" + typeOfDie + " = " + str(sum(dieResults)) + " (" + " + ".join(str(x) for x in dieResults) + ")")

def rollStats(resp, usernick): # Stat rolling function
    def modPipe(dieScore): # Stat modifier function
        # Minus 10, divide by 2 and floor it then make it into an integer
        modValue = int(math.floor((dieScore - 10) / 2 ))

        # Adds a + if the modifier is more than or equal to 0
        if modValue < 0:
            modValue = "" + str(modValue)
        elif modValue >= 0:
            modValue = "+" + str(modValue)

        return modValue

    if usernick in userStats:
        resp.send(usernick + " rolled:")
        for stat in userStats[usernick]:
            resp.send(stat + ": " + str(userStats[usernick].get(stat)) + " (" +modPipe(userStats[usernick].get(stat)) + ")")
        return

    stats = ["Str", "Dex", "Con", "Int", "Wis", "Cha"]
    statObj = {}

    resp.send(usernick + " rolled:")

    for stat in stats:
        dieScoreResults = []
        for i in range(0, 4):
            dieScoreResults.append(random.randint(1, 6))
        dieScoreResults.remove(min(dieScoreResults))

        statObj[stat] = sum(dieScoreResults)

        resp.send(stat + ": " + str(sum(dieScoreResults)) + " (" + modPipe(sum(dieScoreResults)) + ")")

    userStats[usernick] = statObj

def clearStats(resp, usernick): # Clears stored stats for user
    if usernick in userStats:
        del userStats[usernick]
        resp.send("Stats cleared for " + usernick + "\n")


class Handler:
    def __init__(self, brain):
        self.brain = brain; # Brain is not used in this example, but it is usefull if you want i.e the name of the bot


    def canHandle(self, msg):
        return msg.command == 'PRIVMSG' and (re.search(r'#\d[dD]\d', msg.msg) or msg.msg == '#stats' or msg.msg == '#clearstats');

    def handle(self, msg, resp):
        if(msg.msg == '#stats'):
            rollStats(resp, msg.user);
            return;

        if(msg.msg == '#clearstats'):
            clearStats(resp, msg.user);
            return;

        splitMessage = msg.msg.split(" ")

        # Gives all the words a number
        def indexOfRoll(the_list, substring):
            for i, s in enumerate(the_list):
                if re.search(r'#\d[dD]\d', s):
                    return i
            return -1

        # Creates dieRoll variables
        dieRoll = re.split(r'[dD]', splitMessage[indexOfRoll(splitMessage, "#")])

        # Rolls the die somehow???
        rollDie(resp, re.sub('[^0-9]','', dieRoll[0]), re.sub('[^0-9]','', dieRoll[1]), msg.user)

        pass;
