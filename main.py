if __name__ == "__main__":
    print ("You are running the wrong file! You should run LegatoBot.py!")

import socket
import threading
import time
import logging

class ParsedLine:

    def __init__(self):
         self.command = ""
         self.source = ""
         self.user = ""
         self.target = ""
         self.msg = ""

    def contains(self, txt):
        return self.msg.lower().find(txt.lower()) != -1;

    def startswith(self, txt):
        return self.msg.lower().startswith(txt.lower());

    def isTargetRoom(self):
        return self.target.startswith("#");

    def re(self):
        if (self.isTargetRoom()):
            return self.target;
        return self.user;

    def toString(self):
        result = "{\n";

        properties = vars(self);
        for prop in properties:
            if (properties[prop] != ""):
                result += "{0}: {1}\n".format(prop, properties[prop]);
        result += '}';
        return result;




class Response:
    def __init__(self, brain):
        self.send = brain._send;
        self.sendCommand = brain._sendCommand;



class PumiWrapper:
    def __init__(self, pumi, resp):
        self.pumi = pumi;
        self.resp = resp;

    def start (self):
        self.timer = threading.Timer(self.pumi.interval, self.execute);
        self.timer.start();

    def cancel(self):
        if hasattr(self, 'timer'):
            self.timer.cancel();

    def execute(self):
        self.pumi.talk(self.resp)

        if(not self.pumi.isLithoku()):
            self.start();

'''
Examples:
:anonnkun[lt]!~bzz@sdedxu-268-70-64-59.inturbo.lt PRIVMSG LegatoBot2 :asdf
:anonnkun[lt]!~bzz@sdedxu-268-70-64-59.inturbo.lt PRIVMSG #balt :test1
:NASA!~NASA@79-30-444-51.dyn.estpak.ee PRIVMSG #balt :#stats
:anonnkun[lt]!~bzz@sdedxu-268-70-64-59.inturbo.lt QUIT :Quit: anonnkun[lt]
:anonnkun[lt]!~bzz@sdedxu-268-70-64-59.inturbo.lt JOIN #balt
:pasta!uid71692@bqeguxm.irccloud.com PRIVMSG #balt :sherlock theories
PING :ee.ircworld.org
'''
def parseIRCLine(line):
    result = ParsedLine();

    line = line.split(":", 2); # Converts to ['', command, msg] or ['', command] or [command]
    if(len(line) > 0 and line[0] == ""):
        del line[0]; # Removes empty string

    if(len(line) == 2):
        result.msg = line[1].strip();
        del line[1];

    if(len(line) == 1):
        command = line[0].strip().split(" "); # Converts to [source, COMMAND, user/room]

        if(len(command) >= 2):
            result.source = command[0];
            result.user = result.source.split("!")[0];
            result.command = command[1];

        if(len(command) == 3):
            result.target = command[2];

        if(len(command) == 1):
            result.command = command[0];

    return result;

class BrainsOfBot:
    def __init__(self):
        # Some basic variables used to configure the bot
        self.server = "irc.ircworld.org" # Server
        self.port = 6667
        self.channel = "#balt" # Channel
        self.botnick = "LegatoBot" # Your bot's nick
        self.handlers = []
        self.pumis = []
        self.isPumisAlreadyInitialized = False;
        self.debug = True
        self.resp = Response(self);
        self.legatoLock = threading.Lock();
        self.wasLastMsgHandled = False; # Not sure if anybody will ever need it. Can be used to check if user is responding to the bot

    def registerHandler(self, handler):
        if(hasattr(self, "ircsock")):
            logging.error ("Bot is started. Handlers must be registered before start. Ignoring.");
            return;

        if(not hasattr(handler, "priority")):
            handler.priority = 0;

        if(handler.priority != 0):
            for item in self.handlers:
                if(item.priority == handler.priority):
                    raise Exception("Handlers {0} and {1} have the same priority {2}.".format(item.__name__, handler.__name__, item.priority))

        self.handlers.append(handler)

    def registerPumi(self, pumi):
        if(hasattr(self, "ircsock")):
            logging.error ("Bot is started. Pumis must be registered before start. Ignoring.");
            return;

        self.pumis.append(PumiWrapper(pumi, self.resp));

    def _sendCommand(self, msg):
        if(not hasattr(self, "ircsock")):
            logging.error ("Bot was not yet started. Ignoring.");
            return;
        msg = msg.strip().replace("\r", "").replace("\n", " "); # Newlines are forbiden

        self.legatoLock.acquire(True); #lock thread so, that only one command could be sent at the time
        self.ircsock.send((msg + "\n").encode(encoding="utf-8"))
        self.legatoLock.release();

    def _send(self, msg, target = ""): # This is the send message function, it simply sends messages to the channel.
        if(target == ''):
            target = self.channel;

        msg = msg.splitlines();
        for item in msg:
                self._sendCommand("PRIVMSG " + target + " :" + item)

    def _prepareHandlers(self):
        self.handlers.sort(key=lambda handler: handler.priority, reverse=True) # Sort by priority

    def ping(self, msg): # Bot will respond to server pings
        self._sendCommand("PONG :" + msg.msg)

    def tryInitializePumis(self):
        if(self.isPumisAlreadyInitialized): # Only execute once
            return;

        time.sleep(3);
        for pumi in self.pumis:
            pumi.start();

        self.isPumisAlreadyInitialized = True;
        
    def cleanupPumis(self):
        for pumi in self.pumis:
            pumi.cancel();

    def start(self):
        self.isStarted = True;
        self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ircsock.connect((self.server, self.port)) # Here we connect to the server

        self._sendCommand("USER " + self.botnick + " " + self.botnick + " " + self.botnick + " :http://4chan.org/int/balt") # User authentication
        self._sendCommand("NICK " + self.botnick) # Here we actually assign the nick to the bot
        self._sendCommand("JOIN " + self.channel) # Joins the channel using the functions we previously defined

        self._prepareHandlers();
        # Start event loop
        while 1: # Be careful with these! It might send you into an infinite loop
            ircmsg = self.ircsock.recv(2048).decode(encoding="utf-8") # Receive data from the server
            ircmsg = ircmsg.strip("\n\r") # Removing any unnecessary linebreaks

            if(len(ircmsg) <= 0): # Disconnected
                break;

            lines = ircmsg.splitlines();
            for line in lines:

                line = line.strip();
                if not line:
                    continue; # Skip empty lines

                if(self.debug):
                    # Here we print what's coming from the server
                    logging.info(line)

                msg = parseIRCLine(line)

                if(msg.command == "PING"): # Ping is special. Brain can handle it by itself
                    self.ping(msg);
                    continue;

                if(msg.command == "NOTICE" and msg.startswith("Welcome to IRCWorld, ")):
                    self.tryInitializePumis();
                    continue;

                wasLastMsgHandled = False;

                for handler in self.handlers:
                    if(handler.canHandle(msg)):
                        if(self.debug):
                            logging.debug ("handler {0} can handle".format(handler.__class__.__module__));
                        handler.handle(msg, self.resp);
                        wasLastMsgHandled = True;
                        break;
                    elif(self.debug):
                        logging.debug ("NOT {0}".format(handler.__class__.__module__));

                self.wasLastMsgHandled = wasLastMsgHandled;
        
        self.cleanupPumis();
        print ("TIME TO DIE")
