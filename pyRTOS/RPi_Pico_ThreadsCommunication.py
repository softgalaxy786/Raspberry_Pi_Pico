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
Using global variable for inter thread communication
multi thread example
"""
 
from time import sleep
import _thread
 
 
def first_Thread_Core0():
    global run_first_thread

    counter = 0
    while True:
        print("\nFirst Thread Waiting")
        while run_first_thread:					# wait for core 1 to finish
            pass
        print("First Thread In Execution")

        # print next 5 even numbers
        for loop in range(5):
            print(counter)
            counter += 2
            sleep(1)

        run_second_thread = False			     # signal core 0
  
def second_thread():
    global run_second_thread

    counter = 1
 
    while True:
 
        # wait for core 0 to signal start
        print("\nSecond Thread Waiting")
        while not run_second_thread:
            pass
        print("Second Thread In Execution")
 
        # print next 3 odd numbers
        for loop in range(3):
            print(counter)
            counter += 2
            sleep(0.5)
        sleep(1)					# A delay for smooth execution of the program.
        run_first_thread = True         # Global variable to send signals between threads

second_Thread_Core1 = _thread.start_new_thread(second_thread, ())

run_second_thread = True         # Global variable to send signals between threads
bFirstTimeRunControl=True

#The following infinite loop to synchronize (like semaphores) proper code execution.
while(True):
  if(bFirstTimeRunControl):  
    run_first_thread=False	# Stops first thread from executing
  first_Thread_Core0()		# Start first thread on core 0.
  
