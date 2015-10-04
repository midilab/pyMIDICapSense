DEBUG = 0

INPUT = 0
OUTPUT = 1
HIGH = 1 
LOW = 0 

# Sensor types
RANDOM 			= 0 # each trigger a random note will be fired
SEQUENTIAL 	= 1 # each trigger the next not will be fired
BANK_SELECT = 2 # Sensor acts in conformation with BANK number selected
BANK_CHANGE = 3 # For sensor to change the program banks

TIMEOUT = 5000 # timeframe unit, each receiver check consume 1 timeframe unit
TRIGGER = 90 # the average of last n CYCLES
CYCLES = 6 # more cycles checks means more signal stability and sensitivity

# Initial bank
BANK = 1

# Definition of max number of banks to use
BANK_MAX = 1
#BANK_MAX = 12
