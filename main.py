#!/usr/bin/python3
import os
import sys
import aiml
from sl4awrapper import Sl4aWrapper


BRAIN_FILE = os.path.dirname(sys.argv[0])+"/brain.dump"
bot = Sl4aWrapper()
k = aiml.Kernel()


# To increase the startup speed of the bot it is
# possible to save the parsed aiml files as a
# dump. This code checks if a dump exists and
# otherwise loads the aiml from the xml files
# and saves the brain dump.
if os.path.exists(BRAIN_FILE):
    bot.sprogress_start(
        "Please wait", "Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
    bot.sprogress_end()
else:
    print(BRAIN_FILE+" not found!")
    quit()

# Endless loop which passes the input to the bot and prints
# its response
while True:
    input_text = bot.listen()
    if input_text == "bye":
        bot.speak("have a nice day!")
        break
    response = k.respond(input_text)
    print("> "+response)
    bot.speak(response)
