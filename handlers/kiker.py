'''
Kicks spammers out of this idle heaven
'''

class Handler:
	whitelist = [
		'anonkun[lt]',
		'bomf',
		'enon'
	];
	
	outsiders = [];

	def __init__(self, brain):
		self.brain = brain;

	def canHandle(self, msg):
		if msg.command != "PRIVMSG" or not msg.user:
			return False;
		
		if msg.msg.startswith("Hey, I thought you guys might be interested"):
			return True;
		
		user = msg.user;
		if user:
			user = user.lower();

		if user in self.whitelist:
			return False;

		if ("https://" in  msg.msg or "http://" in msg.msg) and user not in self.outsiders:
			return True;
		
		if len(self.outsiders) > 10:
			del self.outsiders[0];
		
		if(user not in self.outsiders):
			self.outsiders.append(user);

		return False;


	def handle(self, msg, resp):
		resp.sendCommand("KICK " + self.brain.channel + " " + msg.user + " :we don't like spam"); 
