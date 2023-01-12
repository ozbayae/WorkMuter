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

### Installation and running
##################################################################################
### IF YOU ARE NOT USING THE EXECUTABLE
### Make sure you have Python 3 installed.
### Move WorkMuterPython to the desired location. Inside that folder, run install.bat
### to install the necessary packages (installs to default environment).
### 	To run WorkMuter, launch run.bat (or launch WorkMuter.py from the command line).
### ---------------------------------------------------
### IF YOU ARE USING THE EXECUTABLE
### You don't need to have Python installed, and you don't need to use install.bat
### Simply move or copy the folder WorkMuterProgram to the desired location (like C:\Program Files\)
###	To run WorkMuter, run WorkMuter.exe.
### ----------------------------------------------------
### If you want to run the program at startup, make a shortcut to run.py or to WorkMuter.exe
### place it in your startup folder. Windows + R and then shell::startup to find the folder
##################################################################################

### Functionality:
##################################################################################
### This program will mute the target program, by default Spotify,
### when the user spends time in apps that aren't in the whitelist
### It mutes the target program when the user is in apps that are in the blacklist
### Mode 1: Mute the target program when the user is in apps that are not in the whitelist
### Mode 2: Mute the target program when the user is in apps that are in the blacklist
##################################################################################

### Tweaking the program
##################################################################################
### To tweak settings, edit the config file (config.ini) found in WorkMuterProgram 
### if you are using executable, or in WorkMuterPython if you are using WorkMuter.py.
##################################################################################

### Building the executable
##################################################################################
### A new executable can be built using the python package "pyinstaller" from inside 
### WorkMuterPython, for example with the following command. > pyinstaller --onefile WorkMuter.py
##################################################################################

### nircmd
##################################################################################
### To mute Windows applications, this program relies on nircmd, found here:
### https://www.nirsoft.net/utils/nircmd.html. I have included a zip to their full
### distribution package as per their licence agreement.
##################################################################################