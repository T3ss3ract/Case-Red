from gpiozero import LED, Button
import yaml
import io 

with open("config.yaml" , 'r') as stream:
	config = yaml.load(stream)

if config == None:
	print("ERROR: no config file loaded")







