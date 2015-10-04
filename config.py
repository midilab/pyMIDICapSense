from defines import *

DEBUG = 0

TRIGGER = 20 # the average of last values for n CYCLES readed from sensor will triguer the MIDI note at value?
CYCLES = 6 # more cycles checks means more signal stability and sensitivity

#TRIGGER = 30 # the average of last n CYCLES
#CYCLES = 6 # more cycles checks means more signal stability and sensitivity

#TRIGGER = 90 # the average of last n CYCLES
#CYCLES = 6 # more cycles checks means more signal stability and sensitivity

#TRIGGER = 40
#CYCLES = 4

# Here we use a global output for the signal, individual output could be less noisly just in case...
MAIN_OUTPUT_CTR = 1

#RANDOM: each touch triggers a random note inside note list
#SEQUENTIAL: each touch triggers the next note on the note list sequence controlled by 'seq_next' param
#BANK_SELECT: each touch triggers the corespondent note inside note list that are indexed by BANK/SCENE number selected
#BANK_CHANGE: For sensor to change the program banks

# Definition of max number of banks to use
BANK_MAX = 12 # or 13?

SENSORS = [
	{
		'type': SEQUENTIAL,
		'name': 'Sensor 1 (Oracle main voices)',
		'output': MAIN_OUTPUT_CTR,
		'input': 4,
		'led': 3,
		'note': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], # MIDI notes 1 to 26 
		'seq_next': 0,
		'last_value': 0
	},
	{
		'type': SEQUENTIAL,
		'name': 'Sensor 2 (Vocalize)',
		'output': MAIN_OUTPUT_CTR,
		'input': 8,
		'led': 7,
		'note': [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], # MIDI notes 27 to 51
		'seq_next': 0,
		'last_value': 0
	},
	{
		'type': SEQUENTIAL,
		'name': 'Sensor 3 (Pads/FXs/Water)',
		'output': MAIN_OUTPUT_CTR,
		'input': 12,
		'led': 11,
		'note': [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], # MIDI notes 52 to 76
		'seq_next': 0,
		'last_value': 0
	},
	{
		'type': BANK_SELECT, # SCENE sounds better
		'name': 'Sensor 4 (A Serie)',
		'output': MAIN_OUTPUT_CTR,
		'input': 14,
		'led': 13,
		'note': [77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], # MIDI notes 77 to 89
		'last_value': 0
	},			
	{
		'type': BANK_SELECT,
		'name': 'Sensor 5 (B Serie)',
		'output': MAIN_OUTPUT_CTR,
		'input': 18,
		'led': 17,
		'note': [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102], # MIDI notes 90 to 102
		'last_value': 0
	},			
	{
		'type': BANK_SELECT,
		'name': 'Sensor 6 (B Serie)',
		'output': MAIN_OUTPUT_CTR,
		'input': 22,
		'led': 21,
		'note': [103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115], # MIDI notes 103 to 115
		'last_value': 0
	},					
	{
		'type': BANK_SELECT,
		'name': 'Sensor 7 (A Serie)',
		'output': MAIN_OUTPUT_CTR,
		'input': 24,
		'led': 23, # better name? not just for led usage but other things mitgh be cool
		'note': [116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127], # MIDI notes 116 to 127
		'last_value': 0
	},
	{
		'type': BANK_CHANGE,
		'name': 'Bank Select',
		'output': MAIN_OUTPUT_CTR,
		'input': 28,
		'led': 27,
		'note': [0, 0, 0],
		'last_value': 0
  }
]
