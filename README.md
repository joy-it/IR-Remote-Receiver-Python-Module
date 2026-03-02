# JoyIT_IR_Remote_Receiver

>[!NOTE]
> This library was forked to make it installable and making it compatible with the Raspberry Pi 5. Therefore 'RPi.GPIO' is exchanged with 'gpiozero'.

## Installation
```shell-script
pip install JoyIT_IR_Remote_Receiver
```

Python 3 module for receiving IR remote control signals (NEC format) on a Raspberry Pi  using a TSOP382 IR Receiver

This module includes one example file. For my testing I used several remotes from around my 
house, the example file includes the codes for the Sparkfun 9 button remote.

## Connection
The TSOP382 IR receiver has 3 legs which are connected as follows:
- 1 - PI GPIO - Pin 16 is used in the example
- 2 - Pi Gnd
- 3 - Pi 3.3V

## Usage
To set up a IR object use:
```python
ir = IRModule.IRRemote(callback=yourfunctname)
```

To set up the Pi GPIO callback the following is required
```python
IR = DigitalInputDevice(pin = irPin, bounce_time = 0.000005)   # irPin = Pi pin connected to the output of the TSOP382 receiver
IR.when_activated =ir.pWidth
IR.when_deactivated =ir.pWidth 
```

To setup your program to provide the IR code being sent use the following
```python
ir.set_callback('DECODE')
```

To get a listing of the time spans of the IR pulse highs and lows use
```python
ir.set_verbose(True)
```

Current user functions include:
```python
set_callback(callback = yourfunctname)
remove_callback()
set_verbose(verbose = False)
set_repeat(repeat = True)
```
## Updates
**Apr 3, 2020 Update**
- added repeat code recognition functionality
- added the set_repeat() function to enable/disable the repeat code functionality

**Noc 25, 2025 Update**
- exchanged 'RPi.GPIO' with 'gpiozero' to ensure compatibility with Raspberry Pi 5
- made library installable

**Mar 2, 2026 Update**
- added repository to [PyPi](https://pypi.org/project/JoyIT-IR-Remote-Receiver/1.0.0/)