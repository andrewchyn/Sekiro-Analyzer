# Variables to change

-COM3 may not be the port your arduino is connected to

-TASE_TIME is set to a low time, increase for longer shock

-TOLERANCE is set so a white screen does not trigger the output, may need adjustment if you change ingame settings

-LED is optional, not having one plugged in will not be an issue

-TASER_PIN is the pin the relay is plugged into - Does not need to be used.


If you want something else to happen when you die, you want to edit the "taser()" function. You can also comment out the printing out of values. Script essentially looks at a screenshot and spits out a value of "how similar" the screenshot is to the original using the structural similarity index, this is probably overkill as we are only screenshotting a homogenous region of pixels, but can be repurposed for other projects. 

# Notes

This was my first time using python and it sucks in a lot of ways that I am too lazy to fix 
