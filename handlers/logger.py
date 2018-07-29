''' Logs everything to console '''
import logging

ignored_commands = ['001', '002', '003', '004', '005', '251', '252',
                    '254', '255', '265', '266', '250', '375', '372',
                    '396', '332', '333', '366', '376'];

class Handler:
    
    def __init__(self, brain):
        self.brain = brain;
    
    def canHandle(self, msg):
        
        if(msg.command == 'PRIVMSG'):
            logging.info('{0:12}: {1}'.format(msg.user, msg.msg));
        elif (not msg.command in ignored_commands):
            logging.info('--- {0}/{1} --- {2}'.format(msg.command, msg.user, msg.msg));

        return False;
        
    def handle(self, msg, resp):
        pass;
