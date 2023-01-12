##################################################################################
#-------------------------------    WORKMUTER    -------------------------------#
##################################################################################

### Intro
##################################################################################
### This is WorkMuter. The idea is that you get to listen to music when you spend 
### time in the apps that you need to work in. To discourage distractions, 
### it will mute your music player when you aren't in the apps you want to work in.
### To encourage you to work, it will unmute your music player when you are back in the right apps. 
##################################################################################

### Check out README.md for more info.

from enum import Enum
from win32gui import GetForegroundWindow
import wmi
import time
import win32process
import os
import configparser

class Mode(Enum):
    WHITELIST = 1,
    BLACKLIST = 2

###################################
### --- USER SETTINGS BELOW --- ### 
###################################
### (Remnant from before there was a config file)


# Tip: To find out the names of programs, you can run the program 
# and check the console after you open a program, or check the detailed view of task manager

#If you're not using spotify, you can change the target app here
target_app = "Spotify.exe"

# Working in apps that are not in the whitelist will mute the target app
whitelist = [
    "explorer.exe",
    "msedge.exe",
    "Code.exe",
    "Notion.exe",
    "Spotify.exe",
]

# In blacklist mode, by default apps will not mute target app, 
# but blacklisted apps will, 
# target app unmutes when you leave the blacklisted app
blacklist = [
    "Discord.exe",
    "chrome.exe"
]


#Pick a mode
mode = Mode.BLACKLIST
# mode = Mode.WHITELIST

###################################
### --- LOADING CONFIG FILE --- ###
###################################

config = configparser.ConfigParser()
read_file = config.read('config.ini')

if(len(read_file) > 0): # succesfully read file
    target_app = config['target']['target_app']
    whitelist = config['whitelist']['whitelist'].splitlines()
    blacklist = config['blacklist']['blacklist'].splitlines()
    if(config['mode']['mode'] == 'whitelist'):
        mode = Mode.WHITELIST
    else:
        mode = Mode.BLACKLIST
    print("Config file succesfully loaded")
else:
    print("Could not load config file: using hardcoded settings. Are you sure there is a config.ini in my folder?")


###################################
### --- END OF CONFIG FILE  --- ###
###################################

### PROGRAM STARTS HERE ###

POLLING_INTERVAL = 0.5

c = wmi.WMI()

def get_app_path(hwnd):
    """Get applicatin path given hwnd."""
    exe = None
    try:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        for p in c.query('SELECT ExecutablePath FROM Win32_Process WHERE ProcessId = %s' % str(pid)):
            exe = p.ExecutablePath
            break
    except:
        return None
    else:
        return exe


def get_app_name(hwnd):
    """Get applicatin filename given hwnd."""
    exe = None
    try:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        for p in c.query('SELECT Name FROM Win32_Process WHERE ProcessId = %s' % str(pid)):
            exe = p.Name
            break
    except:
        return None
    else:
        return exe

def log(app_name, msg):
    """Log the app name."""
    print(str(app_name) + " " + str(msg))

def mute_program(program):
    """Mute the program."""
    os.system(os.getcwd() + "\\" + "nircmdc.exe muteappvolume " + program + " 1") # 0 unmutes the program
    log(program, "muted.")

def unmute_program(program):
    """Unmute the program."""
    os.system(os.getcwd() + "\\" + "nircmdc.exe muteappvolume " + program + " 0") # 1 mutes the program
    log(program, "unmuted.")

#Main loop
while(True):
    time.sleep(POLLING_INTERVAL)

    app_name = get_app_name(GetForegroundWindow())

    #we don't keep state nor check if the program is already muted, so we just mute/unmute it every time

    if mode == Mode.WHITELIST:
        if app_name in whitelist or app_name == None:
            log(app_name, "in whitelist.")
            unmute_program(target_app)
        else:
            log(app_name, "not in whitelist.")
            mute_program(target_app)
        continue
    
    if mode == Mode.BLACKLIST: 
        if app_name in blacklist:
            log(app_name, "in blacklist.")
            mute_program(target_app)
        else:
            log(app_name, "not in blacklist.")
            unmute_program(target_app)
        continue