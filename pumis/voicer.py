'''
Gives users voice after they idled for some time.
See also ../handlers/noticer.py
'''

import time

users = [];

class User:
	def __init__(self, username):
		self.username = username;
		self.now = time.time();

	def isGiveVoice(self):
		return time.time() - self.now > 5;

def scheduleUser(username):
	result = User(username)
	users.append(result);
	return result;

class Pumi:
	interval = 5;
	isInitialized = False;

	def __init__(self, brain):
		self.brain = brain;

	def isLithoku(self):
		return False;

	def init(self, resp):
		resp.sendCommand("MODE " + self.brain.channel + " +m");
		self.isInitialized = True;

	def talk(self, resp):
		
		if not self.isInitialized:
			self.init(resp);
		
		remove = []
		for item in users:
			if item.isGiveVoice():
				remove.append(users.index(item));
				resp.sendCommand("MODE " + self.brain.channel + " +v " + item.username);

		remove.reverse();
		for index in remove:
			users.pop(index);

