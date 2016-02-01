
class FakeResponse:
    def send (self, msg, xx = ''):
        print(">>>>>SENDING: {0}".format(msg));

    def sendCommand(self, msg):
        print(">>>>SENDING COMMAND: {0}".format(msg));

class FakeBrain:
    botnick = 'FakeLegato'
    server = "fake.irc.ircworld.org" # Server
    port = 69
    channel = "#balt" # Channel
    handlers = []
    pumis = []
    debug = False

brain = FakeBrain()
r = brain.resp = FakeResponse();

print("Write:")
print("'import pumis.your_pumi_name'")
print("'p = pumis.your_pumi_name.Pumi(pumiTest.brain)'")
print("'p.talk(pumiTest.r)'")
