#!/usr/bin/env python3
import os
from gpiozero import DigitalInputDevice
import IRModule
import time


# method to decode the IR signal
def remote_callback(code):
    # buttons of remote control
    if code == 0xffa25d:
        print("KEY_CH-")
    elif code == 0xff629d:
        print('KEY_CH')
    elif code == 0xffe21d:
        print('KEY_CH+')
    elif code == 0xff22dd:
        print('KEY_PREV')
    elif code == 0xff02fd:
        print('KEY_NEXT')
    elif code == 0xffc23d:
        print('KEY_PLAY/PAUSE')
    elif code == 0xffe01f:
        print('KEY_VOL-')
    elif code == 0xffa857:
        print('KEY_VOL+')
    elif code == 0xff906f:
        print('KEY_EQ')
    elif code == 0xff6897:
        print('KEY_0')
    elif code == 0xff9867:
        print('KEY_100+')
    elif code == 0xffb04f:
        print('KEY_200+')
    elif code == 0xff30cf:
        print('KEY_1')
    elif code == 0xff18e7:
        print('KEY_2')
    elif code == 0xff7a85:
        print('KEY_3')
    elif code == 0xff10ef:
        print('KEY_4')
    elif code == 0xff38c7:
        print('KEY_5')
    elif code == 0xff5aa5:
        print('KEY_6')
    elif code == 0xff42bd:
        print('KEY_7')
    elif code == 0xff4ab5:
        print('KEY_8')
    elif code == 0xff52ad:
        print('KEY_9')
    return

# set up IR pi pin and IR remote object with our method to decode
irPin = 15
ir = IRModule.IRRemote(callback='DECODE')
# using 'DECODE' option for callback will print out
# the IR code received in hexadecimal
# this can used to get the codes for whichever NEC
# compatable remote you are using

# set pin as input
IR = DigitalInputDevice(pin = irPin, bounce_time = 0.000005)

# Add event at pin when a signla is received
# callback to calculate signal into hex
IR.when_activated =ir.pWidth
IR.when_deactivated =ir.pWidth

ir.set_verbose() # verbose option prints outs high and low width durations (ms)

# print at the start
print('Starting IR remote sensing using DECODE function and verbose setting equal True ')
print('Use ctrl-c to exit program')


try:
    time.sleep(5)

    # turn off verbose option and change callback function
    # to the function created above - remote_callback()
    print('Turning off verbose setting and setting up callback')
    ir.set_verbose(False)
    ir.set_callback(remote_callback)

    # while to keep progrm running
    # through event detection signal is received and printed
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    # clean GPIOs up and remove callback from object
    print('Removing callback and cleaning up GPIO')
    ir.remove_callback()