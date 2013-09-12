xbmc-idleubsubscribe
====================

XBMC script add-on that will auto unsubscribe from current tv channel if no activity detected

Currently the time for sleep is hardcoded into the default.py
in the variable: IDLE_TIME_MIN = 60

The system will prompt before the expiry of the timer and if no action taken
it will unsubscribe/stop the current activity on xbmc

INSTALLATION:
=============

Create a folder for the addon in your .xbmc folder.
e.g. mkdir /storage/.xbmc/addons/script.service.idleunsubscribe

Copy the default.py and addon.xml into this folder

Edit default.py and set the idle time you want. it's set to 1hr by default

Reload XBMC, go into addons and enable the idleunsubscribe addon. This will then
trigger and start the countdown timer when a playback is taking place.

