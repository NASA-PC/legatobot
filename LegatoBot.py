import os
import main

brain = main.BrainsOfBot()

modules = os.listdir("handlers");
modules.sort();
for file in modules:
    if(file.endswith(".py")):
        file = file[:-3] # Remove .py
        module = __import__("handlers." + file).__getattribute__(file);
        if("Handler" in dir(module)):
            brain.registerHandler(module.Handler(brain));
            print ("module '{0}' registered".format(file));
        else:
            print ("Handler '{0}' does not have class Handler in it. Ignored.".format(file));


modules = os.listdir("pumis");
modules.sort();
for file in modules:
    if(file.endswith(".py")):
        file = file[:-3] # Remove .py
        module = __import__("pumis." + file).__getattribute__(file);
        if("Pumi" in dir(module)):
            brain.registerPumi(module.Pumi(brain));
            print ("Pumi module '{0}' registered".format(file));
        else:
            print ("Pumi '{0}' does not have class Pumi in it. Ignored.".format(file));


brain.start();
