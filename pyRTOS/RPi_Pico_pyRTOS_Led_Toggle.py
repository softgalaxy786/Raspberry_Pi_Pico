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
#Import relevant dependencies

import machine
import utime
import _thread

# We configure the pin of the internal led as an output and
# we assign to internal_led
internal_led = machine.Pin(25, machine.Pin.OUT)

# We create a semaphore (also called a "lock" )
semaphore_Gate = _thread.allocate_lock()

# Function that will block the thread with a while loop
# which will simply display a message every second
def second_thread():
    while True:
        # We acquire the traffic light lock
        semaphore_Gate.acquire()			# Close the gate (lock) for other tasks to access CPU time.
        print("Greetings from second thread")
        utime.sleep(1)						# Delay as required.
        # We release the traffic light lock
        semaphore_Gate.release()			# Release the gate (unlock) for other tasks to access CPU time.
# Function that initializes execution in the second core
# The second argument is a list or dictionary with the arguments
# that will be passed to the function.
_thread.start_new_thread(second_thread, ())

# Third Function, which will simply display a message.
def third_thread():
    while True:
        # We acquire the traffic light lock
        semaphore_Gate.acquire()			# Close the gate (lock) for other tasks to access CPU time.
        print("Greetings from third thread")
        utime.sleep(0.25)						# Delay as required.
        # We release the traffic light lock
        semaphore_Gate.release()			# Release the gate (unlock) for other tasks to access CPU time.


# Second loop that will block the main thread, and what it will do
# that the internal led blinks every half second
while True:
    # We acquire the semaphore lock
    semaphore_Gate.acquire()			# Close the gate (lock) for other tasks to access CPU time.
    print("LED blinking, main while loop")
    internal_led.toggle()
    utime.sleep(1)
    semaphore_Gate.release()			# Release the gate (unlock) for other tasks to access CPU time.
#    third_thread()
#    utime.sleep(3)

'''
#
# Method #2, without semaphores
#
#Import pyRTOS and relevant dependencies

import machine
import utime
import _thread

# We configure the pin of the internal led as an output and
# we assign to internal_led
internal_led = machine.Pin(25, machine.Pin.OUT)

# Function that will block the thread with a while loop
# which will simply display a message every second
def second_thread():
    while True:
        print("Hello, I'm here in the second thread writting every second")
        utime.sleep(1)

# Function that initializes execution in the second core
# The second argument is a list or dictionary with the arguments
# that will be passed to the function.
_thread.start_new_thread(second_thread, ())

# Second loop that will block the main thread, and what it will do
# that the internal led blinks every n second
while True:
    internal_led.toggle()
    utime.sleep(2)					# n=2 seconds

'''