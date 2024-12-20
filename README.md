# IR-Remote-Receiver-Python-Module

*Making the library installable and using gpiozero instead of RPi.GPIO.*

Python (2 or 3) module for receiving IR remote control signals (NEC format) on a Raspberry Pi 
using a TSOP382 IR Receiver

To use this module requires the RPi.GPIO module and you need to run your program as the root
 user,  i.e. sudo...

This module includes one example file. For my testing I used several remotes from around my 
house, the example file includes the codes for the Sparkfun 9 button remote.

The TSOP382 IR receiver has 3 legs which are connected as follows:
- 1 - PI GPIO - I used Pin 16
- 2 - Pi Gnd
- 3 - Pi 3.3V

To set up a IR object use:
- ir = IRModule.IRRemote(callback=yourfunctname)

To set up the Pi GPIO callback the following is required
- IR = DigitalInputDevice(pin = irPin, bounce_time = 0.000005)   # irPin = Pi pin connected to the output of the TSOP382 receiver
- IR.when_activated =ir.pWidth & IR.when_deactivated =ir.pWidth 

To setup your program to provide the IR code being sent use the following
- ir.set_callback('DECODE')

To get a listing of the time spans of the IR pulse highs and lows use
- ir.set_verbose(True)

Current user functions include:
- set_callback(callback = yourfunctname)
- remove_callback()
- set_verbose(verbose = False)
- set_repeat(repeat = True)


Apr 3, 2020 Update
- added repeat code recognition functionality
- added the set_repeat() function to enable/disable the repeat code functionality


