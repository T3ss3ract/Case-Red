from gpiozero import LED, Button
import yaml
import io
import time

with open("config.yaml" , 'r') as stream:
	config = yaml.load(stream)

if config == None:
	print("ERROR: no config file loaded")

#   check_plant_time
#   params: none
#   returns: an integer operation code for the status of each plant 
#   status code -1: plant is inactive due to time constraints
#                0: plant is active and receiving nutrients
#                2: general error code (add more later)
def check_plant_time():
    for plant in config[plants]:
        start_time = config[plant][start_time]
        end_time = config[plant][end_time]
        #current_time = time.asmtime
        if(#current time is past end time):
            plant_id = config[plant][plant_id]
    return 0




def fan_test():
    return 0

def water_pump_test():
    return 0:


def led_test():
    return 0


def run_fans():
    return 0


def run_water_pumps():
    return 0

def run_leds():
    return 0





