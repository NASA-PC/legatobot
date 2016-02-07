# Introduction

Simple IRC bot for D&D and some various minor things.

# How to use

1. Configure the connection details etc. from main.py & git.py according to your needs
1. Run LegatoBot.py

# Dependencies

* Python 2.7/3.5.1
* BeautifulSoup (for weather.py)

# Development

You probably only need to write handlers or pumis.

## Handlers

If you want to create a new handler, check out handlers/example.py
The best way to create a new handler is to copy example.py to "my_own_handler.py" and start from there.
* function `canHandle(self, msg)` must return True if handler can handle the response, in that case handling is dedicated to this handler and other handlers won't be executed.
* function `handle(self, msg, resp)` is where the fun part is stored. This function is dedicated to actually handling user input and outputing response with `resp.send("your message here")` or `resp.sendCommand("your command here")`, you can add `sg.re()` to parameters if you want the bot to respond to the correct channel, othervise it will respond to `brain.channel`
If you want your handler to have higher priority, you can set it to have a higher priority property.

## Pumis

Pumis are regularly executed tasks, executing each `interval` seconds until the pumi dies (`isLithoku() return true`).  

`talk(self, resp)` is the only important function where all the handling should be implemented. A pumi is free to change it's interval or lithoku anytime it wishes, just be careful ***not*** to spam the server every second with your boring bloging!  
Please check out pumis/example.py for a fast dying pumi example. 

`talk()` is executed before `isLithoku()`, therefore each Pumi has a chance to say at least something before death.  
`talk()` for the first time is called only after `interval` of seconds, so that pumis wouldn't spam the tread.

### Testing Pumis

Since testing pumis by simply running LegatoBot is time consuming, a helper file was created. Here's how to use it:

1. open your python console
1. `import pumiTest`
1. `import pumis.your_pumi_name`
1. `p = pumis.your_pumi_name.Pumi(pumiTest.brain)`
1. `p.talk(pumiTest.r)`

`p` is your pumi, you can check variables of your pumi by typeing `p.variable_name`, i.e. `p.interval` or `p.isLithoku()`.
You can execute `p.talk(pumiTest.r)` multiple times if necessary.


# Credits

* ArnieBoi[SWE]
* suukinni
* Thorndrop
* [J3remy](http://wiki.shellium.org/index.php?title=Writing_an_IRC_bot_in_Python&action=edit)
* kawaii anonkun
* [paulbarbu](https://github.com/paulbarbu/IRC-Bot/)

