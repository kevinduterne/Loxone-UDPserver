Loxone-UDPserver
================

Python UDP server to trigger scripts on external machine with simple UDP commands from Loxone

(This explanations will work without any modifications on Mac/Linux, haven't tested it on Windows as of yet.. )

Edit the server IP and respective port in UDPserver.py
Edit the commands.xml with the scripts/commands you would like to trigger on your machine

syntax
<tag function="Functionname" name="Commandname" command="Executable"/>
example command "reboot computer"
<tag function="Shell" name="Reboot" command="reboot now"/>
example run script "run applescript to change source of music and the speaker"
<tag function="Source" name="iTunes" command="osascript AirfoilSource.scpt iTunes"/>
  <tag function="Speaker" name="Kitchen" command="osascript AirfoilSpeaker.scpt Kitchen"/>


You can then start the server on your local machine or server, make sure all the files/scripts are in the same folder
sudo python UDPserver.py &

To test the server you can use netcat 
sudo nc -u "server_IP" "port"(without the quotes)
--> if running the server on port 5005 and testing on the local machine itself that would be 
sudo nc -u localhost 5005

You can then enter a command with the following syntax:
function name (extra option)

The extra option is added for extra parameters without entering them in the xml, like "on" or "off". They will be passed at the end of the command.

For the example of reboot that would be 
Shell Reboot

More real life example, change source to the itunes library on my computer and enable the speaker in the kitchen
Source iTunes
Speaker Kitchen On

Adding this in Loxone is easy 

Make a new virtual output with properties
adres = udp://Server_IP:PORT
enable end connection after sending command
divider = ;

From there on you can make virtual output commands
All you have to enter is the command in the "command for on" field 
If you have different commands for "on" or "off" you can enter then in the respective fields..

Enjoy! 
