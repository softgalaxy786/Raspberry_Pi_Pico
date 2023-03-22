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
"""
Using Flag class for inter thread communication
multi thread example
"""
 
from time import sleep
import _thread
 
class Flag:
    run_core_1 = False
 
    @classmethod
    def set_run_flag(cls):
        cls.run_core_1 = True
 
    @classmethod
    def clear_run_flag(cls):
        cls.run_core_1 = False
 
    @classmethod
    def get_run_flag(cls):
        return cls.run_core_1
 
 
def core0_thread():
    counter = 0
    while True:
        # print next 5 even numbers
        for loop in range(5):
            print(counter)
            counter += 2
            sleep(1)
 
        # signal core 1 to run
        Flag.set_run_flag()
 
        # wait for core 1 to finish
        print("core 0 waiting")
        while Flag.get_run_flag():
            pass
 
 
def core1_thread():
    global run_core_1
    counter = 1
 
    while True:
 
        # wait for core 0 to signal start
        print("core 1 waiting")
        while not Flag.get_run_flag():
            pass
 
        # print next 3 odd numbers
        for loop in range(3):
            print(counter)
            counter += 2
            sleep(0.5)
 
        # signal core 0 code finished
        Flag.clear_run_flag()
 
 
Flag.clear_run_flag()
second_thread = _thread.start_new_thread(core1_thread, ())
core0_thread()