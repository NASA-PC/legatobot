# -*- coding: UTF-8 -*-
'''
Generates names on demand
'''
import random

def genMaleNames():
        male_name = [line.rstrip("\n") for line in open("library/male_names.txt")]
        surname = [line.rstrip("\n") for line in open("library/surnames.txt")]
        text = male_name[random.randint(0, len(male_name) -1)] + " " + surname[random.randint(0, len(surname) -1)]
        return text.encode("utf-8")
            
def genFemaleNames():
        female_name = [line.rstrip("\n") for line in open("library/female_names.txt")]
        surname = [line.rstrip("\n") for line in open("library/surnames.txt")]
        text = "Generated name: " + female_name[random.randint(0, len(female_name) -1)] + " " + surname[random.randint(0, len(surname) -1)]
        return text.encode("utf-8")

class Handler:
    priority = 17;

    def __init__(self, brain):
        self.brain = brain; # Brain is useful if you want i.e the name of the bot

    def canHandle(self, msg):
        return msg.command == "PRIVMSG" and msg.msg == "#name -m" or msg.msg == "#name -f";
            
    def handle(self, msg, resp):
        if(msg.msg == "#name -m"):
            msg.text = genMaleNames();
            resp.send(msg.text, msg.re());
            
        if(msg.msg == "#name -f"):
            msg.text = genFemaleNames();
            resp.send(msg.text, msg.re());
