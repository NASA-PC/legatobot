# Introduction

Simple IRC bot for D&D and some various minor things.

# How to use

1. Configure the connection details etc. @ main.py according to your needs
2. Run the LegatoBot.py

# Dependencies

Python 2.7 or Python 3.0
BeautifulSoup (weather.py)

# Development
You probably only need to write handlers or pumis.

## Handlers
If you want to create a new handler, check out handlers/example.py
Best way to create a new handler is to copy example.py to "my_own_handler.py" and start from there.
* function canHandle(self, msg) must return True if handler can handle the response, in that case handling is dedicated to this handler and other handlers won't be executed.
* function handle(self, msg, resp) is where all fun part is stored. This function is dedicated to actually handling user input and outputing response using resp.send("your message here") or resp.sendCommand("your command here"), you can add msg.re() to parameters if you want the bot to respond to the correct channel, othervise it will respond to *'brain.chanel'*
If you want your handler to have higher priority, you can set higher priority property.

## Pumis
Pumis are regullary execurted tasks, executing each *'interval'* seconds until pumi dies (isLithoku() return true).  

*talk(self, resp)* is the only important function where all the handling should be implemented. Pumi is free to change it's interval or lithoku anytime it wishes, just be carefull ***not*** to spam server each 1 second with your boring bloging!  
Please check out pumis/example.py for fast dying pumi example. 

NOTE: talk() is executed before isLithoku() therefore each Pumi has a chance to say at least something before death.  
NOTE 2: talk() for the first time is called only after *'interval'* of seconds, so that pumis wouldn't spam the tread.

### Testing Pumis
Since testing pumis by simple running LegatoBot is time consuming, a helper file was created. How to use it:
1. open your python console
1. import pumiTest
1. import pumis.your_pumi_name
1. p = pumis.your_pumi_name.Pumi(pumiTest.brain)
1. p.talk(pumiTest.r)

p is your pumi, you can check variables of your pumi by typeing p.varable_name, i.e. *'p.interval'* or *'p.isLithoku()'*
in need you can execute p.talk(pumiTest.r) multiple times.


# Credits

* ArnieBoi[SWE]
* suukinni
* Thorndrop
* [J3remy](http://wiki.shellium.org/index.php?title=Writing_an_IRC_bot_in_Python&action=edit)
* kawaii anonkun
* [paulbarbu](https://github.com/paulbarbu/IRC-Bot/)

