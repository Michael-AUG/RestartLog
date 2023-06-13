# RestartLog
A push button command to restart two systemctl services on a Raspberry Pi

This script utilises the GPIO pins on a Raspberry Pi to restart two running services (in this instance called 'log.service' and 'rigctld.service') at the push of a momentary button. I find this necessary because I use my Pi to syncronise rig information with CloudLog. However when I turn my radio off, often one or both of the services fail (because they're expecting a response from the rig), meaning they need restarting. In the past I had this script set to restart the Pi, but now I realise it is better all round to just restart the services instead of bouncing the whole Raspberry Pi.

In time I plan to add a command to sound a buzzer (attached to another GPIO Pin) which will serve as an audible confirmation that the services have been restarted.

To implement this script:
* Save the file (perhaps in `/home/pi/Scripts/`?)
* `$ sudo nano /etc/rc.local`
* Place this line **before the final `exit 0`** - `python /home/pi/Scripts/restartLog.py &`
* `$ sudo reboot`

As ever, I offer this simple script for other people's interest and, perhaps, assistance.

Best wishes. 73
Michael GM5AUG

https://gm5aug.topple.scot

