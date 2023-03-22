# Programmer: 	Raza Bhatti
# Company:		Softgalaxy Technologies Inc.
# Website:		https://www.linkedin.com/in/softgalaxy
#
# Board this program is tested with: Raspberry Pi Pico
# REPL (R)ead,(E)valuate,(P)rogram,(L)oop is a term associated with this board or technology.
#
# Observation or Principle to proposed solutions: There are mostly or always multiple ways to achieve same objective.
#
# MicroPython 3.x using Raspberry Pi Pico Function: 
# 1. Blink LED on board using pyRTOS
#
#
# Reference Links
# 1. https://docs.micropython.org
# 2. https://www.electrosoftcloud.com/en/multithreaded-script-on-raspberry-pi-pico-and-micropython/
# 3. https://docs.python.org/3.7/library/_thread.html#module-_thread
# 4. https://bytesnbits.co.uk/multi-thread-coding-on-the-raspberry-pi-pico-in-micropython/
# 5. https://www.cytron.io/tutorial/real-time-multitasking-on-maker-pi-pico-using-pyrtos
#
# Notes:
# - Not using pyRTOS, instead the built in multithreading functionality offered by MicroPython.
# - 

'''
#
# Method #1, using semaphores
#
'''
"""
Basic multi thread example
"""
 
from time import sleep
import _thread
 
 
def core0_thread():
    counter = 0
    while True:
        print("Core 0 thread counter=") 
        print(counter)
        counter += 2
        sleep(3.25)
 
 
def core1_thread():
    counter = 1.0
    while True:
        print("Core 1 thread counter=") 
        print(counter)
        counter += 0.25
        sleep(3.35)
 
 
second_thread = _thread.start_new_thread(core1_thread, ())
 
core0_thread()
