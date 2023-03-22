# Programmer: 	Raza Bhatti
# Company:	Softgalaxy Technologies Inc.
# Website:	https://www.linkedin.com/in/softgalaxy
#
# Board this program is tested with: Raspberry Pi Pico
# REPL (R)ead,(E)valuate,(P)rogram,(L)oop is a term associated with this board or technology.
#
# Observation or Principle to proposed solutions: There are mostly or always multiple ways to achieve same objective.
#
# MicroPython 3.x using Raspberry Pi Pico Function: 
# 1. Blink LED on board
#
#
# Reference Links
# 1. https://docs.micropython.org
#
# Notes:
# 1. How to auto execute this program on powering up Rasperrby Pi Pico
#    - Rename this file to main.py, if using Thonny, use File->Save a Copy option to upload to Raspeberry Pi Pico
#
#


'''
#------------------------------------------------------------------------------------------------------
#Currently supported features using Micro Python includes:
#------------------------------------------------------------------------------------------------------
#• REPL over USB and UART (on GP0/GP1).
#• 1600kB filesystem using littlefs2 on the on-board flash. (Default size for Raspberry Pi Pico)
#• utime module with sleep and ticks functions.
#• ubinascii module.
#• machine module with some basic functions.
#  machine.Pin class
#  machine.Timer class
#  machine.ADC class
#  machine.I2C and machine.SoftI2C classes
#  machine.SPI and machine.SoftSPI classes
#  machine.WDT class
#  machine.PWM class
#  machine.UART class
#• rp2 platform-specific module
#  PIO hardware access library
#  PIO program assembler
#  Raw flash read/write access
#• Multicore support exposed via the standard _thread module
#• Accelerated floating point arithmetic using the RP2040 ROM library and hardware divider (used automatically)
#'''

'''
# Implementation Method #1
#
from machine import Pin		# A requirement for configuring pins.
import utime				# A requirement for delay functions.

ledpin = Pin(25, Pin.OUT)


while(1):
  utime.sleep(1)			# Delay of 1 sec for see the blink.
  ledpin.value(0)			# Turn Rasperry Pi Pico LED connected with pin 25 OFF
  print("LED is ON")		# Send a text message to serial port
  utime.sleep(1)			# Now turn the Raspberry Pi Pico LED OFF connected with pin 25.
  ledpin.value(1)			# A delay for us to see the blink.
  print("LED is OFF")		# Send a text message to serial port


'''
# Implementation Method #2
#

from machine import Pin, Timer

i_RPi_Pico_LED=25
bBlinkLED=True

led_RPi = Pin(i_RPi_Pico_LED, Pin.OUT)
def fnToggleLED():
  global bBlinkLED
  if bBlinkLED:
    print("Toggling LED ON")
    led_RPi.value(1)
    bBlinkLED=False
  else:
    print("Toggling LED OFF")
    led_RPi.value(0)
    bBlinkLED=True
  

def tick(timer):
  fnToggleLED()

timer_Inst1 = Timer()											   # Initiate a timer instance
timer_Inst1.init(mode=Timer.PERIODIC, freq=1, callback=tick)       # Enable this line for periodic at 1Hz blink

#timer_Inst1.init(period=5000, callback=tick)					     # Enable this line for periodic at 1Hz blink

#timer_Inst1.init(mode=Timer.ONE_SHOT, period=1000, callback=tick) # one shot firing after 1000ms

