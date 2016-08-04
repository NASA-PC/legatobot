'''
Quirky adventure game for us nerds, amirite? ;)
'''
import re
import math
import random

userStats = {}

def rollDice(resp, numberOfDice, typeOfDice, usernick): # Dice rolling function
    if typeOfDice == "0":
        resp.send(":^)")
        return
    
    if numberOfDice == "":
        numberOfDice = "1"
        
    if numberOfDice == "0":
        resp.send(":^)")
        return

    diceResults = []
    for i in range(int(numberOfDice)):
        diceResults.append(random.randint(1, int(typeOfDice)))

    if numberOfDice == "1":
        resp.send(usernick + " rolls " + numberOfDice + "d" + typeOfDice + " = " + str(sum(diceResults)))
    else:
        resp.send(usernick + " rolls " + numberOfDice + "d" + typeOfDice + " = " + str(sum(diceResults)) + " (" + " + ".join(str(x) for x in diceResults) + ")")

def rollStats(resp, usernick): # Stat rolling function
    def modPipe(diceScore): # Stat modifier function
        # Minus 10, divide by 2 and floor it then make it into an integer
        modValue = int(math.floor((diceScore - 10) / 2 ))

        # Adds a + if the modifier is more than or equal to 0
        if modValue < 0:
            modValue = "" + str(modValue)
        elif modValue >= 0:
            modValue = "+" + str(modValue)

        return modValue

    stats = ["Str", "Dex", "Con", "Int", "Wis", "Cha"]
    
    if usernick in userStats:
        resp.send(usernick + " rolled:")
        for stat in stats:
            resp.send(stat + ": " + str(userStats[usernick].get(stat)) + " (" +modPipe(userStats[usernick].get(stat)) + ")")
        return

    statObj = {}

    resp.send(usernick + " rolled:")

    for stat in stats:
        diceScoreResults = []
        for i in range(0, 4):
            diceScoreResults.append(random.randint(1, 6))
        diceScoreResults.remove(min(diceScoreResults))

        statObj[stat] = sum(diceScoreResults)

        resp.send(stat + ": " + str(sum(diceScoreResults)) + " (" + modPipe(sum(diceScoreResults)) + ")")

    userStats[usernick] = statObj

def clearStats(resp, usernick): # Clears stored stats for user
    if usernick in userStats:
        del userStats[usernick]
        resp.send("Stats cleared for " + usernick + "\n")

class Handler:
    def __init__(self, brain):
        self.brain = brain; # Brain is not used in this example, but it is useful if you want i.e the name of the bot

    def canHandle(self, msg):
        return msg.command == "PRIVMSG" and (re.search(r"#\d[dD]\d|#[dD]\d", msg.msg) or msg.msg == "#stats" or msg.msg == "#clearstats");

    def handle(self, msg, resp):
        if msg.msg == "#stats":
            rollStats(resp, msg.user);
            return;

        if msg.msg == "#clearstats":
            clearStats(resp, msg.user);
            return;

        splitMessage = msg.msg.split(" ")

        # Gives all the words a number
        def indexOfRoll(the_list, substring):
            for i, s in enumerate(the_list):
                if re.search(r"#\d[dD]\d|#[dD]\d", s):
                    return i
            return -1

        # Creates diceRoll variables
        diceRoll = re.split(r"[dD]", splitMessage[indexOfRoll(splitMessage, "#")])

        # Rolls the dice somehow???
        rollDice(resp, re.sub("[^0-9]","", diceRoll[0]), re.sub("[^0-9]","", diceRoll[1]), msg.user)

        pass;
