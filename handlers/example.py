'''
---
Example handler.
This handler sends back parsed message to user who posted private
message "echo" to the bot.
---
msg = {
    command = PRIVMSG|QUIT|JOIN
    source = username!id
    user = username
    target = room|target user(in private messages, usually bot name)
    msg = message|reason

    isTargetRoom() - true if target strarts with #
    re() - can be used in send(), returns either room name either username
}

resp = {
    send(msg) - sends PRIVMSG
    sendCommand(command) - sends any command
}
'''

class Handler:
    priority = 0; ''' We don't care about priority.
    It is used to determine which handler should be checked canHandle() first.
    Two handlers must not have the same priority (unless priority is 0)
    If priority is not defined, it is considered to be 0. '''

    def __init__(self, brain):
        self.brain = brain; # Brain is not used in this example, but it is useful if you want i.e the name of the bot

    def canHandle(self, msg):
        return msg.command == "PRIVMSG" and not msg.isTargetRoom() and msg.msg == "echo";

    def handle(self, msg, resp):
        responseText = msg.toString();
        print ("Sending response: " + responseText);
        resp.send(responseText, msg.re()); # Send private message to sender user
