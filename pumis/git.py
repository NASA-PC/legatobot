import json
import sys

if sys.version_info < (3, 0):
    import urllib2
    def getUrlData(url):
        return urllib2.urlopen(url).read();
else:
    import requests
    def getUrlData(url):
        return requests.get(url = url).text;

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
    interval = 10;

    def __init__(self, brain):
        self.brain = brain; # Brain is not used in this example, but it is useful if you want i.e the name of the bot
        self.checkUpdate = True;
        self.isLithoku = False;
        self.mySha = '';

        try:
            with open('.git/refs/remotes/origin/master', 'r') as file:
                self.mySha = file.read().strip();
        except:
            self.isLithoku = True;

        self.latestSha = '';

    def isLithoku(self):
        return self.isLithoku;

    def talk(self, resp):
        self.interval = 5 * 60;

        data = json.loads(getUrlData('https://api.github.com/repos/Thorndrop/legatobot/commits'))

        if(self.checkUpdate):
            self.checkUpdate = False;
            behind = 0;
            for commit in data:
                if (commit['sha'] == self.mySha):
                    break;
                behind += 1;
            if(behind == 0):
                resp.send("I am up to date, yay!")
            if(behind == 1):
                resp.send("I am out of date, there is a new commit in the github repository.")
            if(behind >= 2):
                resp.send("I am out of date, there are {0} new commits in the github repository.".format(behind))

        if(not self.latestSha):
            self.latestSha = data[0]['sha'];
        else:
            for commit in data:
                if (commit['sha'] != self.latestSha):
                    resp.send('A new commit in github "{0}" by "{1}"'.format(commit['commit']['message'], commit['commit']['author']['name']).replace('\r', '').replace('\n', ' '));
                else:
                    break;
            self.latestSha = data[0]['sha'];
