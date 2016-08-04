'''
Displays commands for the bot.
'''

commands = {
    "d":"#XdY to roll Y-sided dice x times\n",
    "stats":"Generates strength, dexterity, constitution, intelligence, wisdom & charisma stats for your character.\n",
    "clearstats":"Clears your previously generated stats.",
    "4chan":"Provides a link to the current /balt/ general on 4chan's /int/ board.\n",
    "8chan":"Provides a link to the /balt/ on 8chan.\n",
    "insult":"Generates a funny insult. #insult name to insult a specific user.\n",
    "name":"Generates a name. Use -m or -f parameters for male/female names.\n",
    "shitpost":"Provides a link to channel statistics.\n",
    "todo":"Displays a To-Do list of LegatoBot. Please contribute!"
}

class Handler:
    priority = 100;

    def __init__(self, brain):
        self.brain = brain; # Brain is not used in this example, but it is useful if you want i.e the name of the bot

    def canHandle(self, msg):
        msg.text = ""
        if (msg.command == "PRIVMSG"):

            if (msg.contains("#help")):
                msgWords = msg.msg.split(" ")
                helpIndex = msgWords.index("#help")
                if (len(msgWords) >= helpIndex +2):
                    command = msgWords[helpIndex +1]

                    if (command in commands):
                        msg.text = commands[command]
                        return True;

                    else:
                        msg.text = "Invalid command. Use #help to display the list of commands."
                        return True;

                else:
                    msg.text = "Commands: d, stats, clearstats, 4chan, 8chan, todo, name, insult, shitpost\nUse #help <command> to learn more.\n"
                    return True;
                
    def handle(self, msg, resp):
        resp.send(msg.text, msg.re());
