import wiringpi2
import rtmidi

from defines import *


from config import *
#import config
# config.TIMEOUT

def Setup(outPin, inPin, ledPin):
	# set Send Pin Register
	wiringpi2.pinMode(outPin, OUTPUT)

	# set receivePin Register low to make sure pullups are off
	wiringpi2.pinMode(inPin, OUTPUT)
	wiringpi2.digitalWrite(inPin, LOW)
	wiringpi2.pinMode(inPin, INPUT)
	
	# set ledPin
	wiringpi2.pinMode(ledPin, OUTPUT)
	wiringpi2.digitalWrite(ledPin, LOW)

def CapRead(outPin, inPin, total=0, cycles=CYCLES):
	# set Send Pin Register low
	wiringpi2.digitalWrite(outPin, LOW)

	# set send Pin High
	wiringpi2.digitalWrite(outPin, HIGH)   
 
	# while receive pin is LOW AND total is positive value
	while( wiringpi2.digitalRead(inPin) == LOW and total < TIMEOUT ):
		total+=1
    
	if ( total > TIMEOUT ):
		return -2 # total variable over TIMEOUT
        
	# set receive pin HIGH briefly to charge up fully - because the while loop above will exit when pin is ~ 2.5V 
	wiringpi2.digitalWrite(inPin, HIGH)
 
	# set send Pin LOW
	wiringpi2.digitalWrite(outPin, LOW)

	# while receive pin is HIGH  AND total is less than TIMEOUT
	while( wiringpi2.digitalRead(inPin) == HIGH and total < TIMEOUT) :
		total+=1
    
	if ( total >= TIMEOUT ):
		return -2

	# decrement cycles counting
	cycles-=1

	# if we reach the end of cycles, then...
	if (cycles == 0):
		if DEBUG:
			print("total unit count: %d" % total)
		# get the average of values over the cycles
		total = round(total/CYCLES)
		# if the average total is greater of equal to TRIGGER value
		if ( total >= TRIGGER ):
			return 1
		else:
			return 0

	return CapRead(outPin, inPin, total, cycles)

def ChangeBank():
	global BANK

	# increment bank number
	BANK += 1

	# check for bank boundaries
	if ( BANK > BANK_MAX ):
		BANK = 1

	print("BANK: %d selected" % BANK)

	# blink the led x times followed by BANK number
	#i = 0
	#while ( i < BANK ):
	#	wiringpi2.delay(500)
	#	wiringpi2.digitalWrite(SENSORS[7]['led'], HIGH)
	#	wiringpi2.delay(500)
	#	wiringpi2.digitalWrite(SENSORS[7]['led'], LOW)
	#	i += 1

# Initial definitions
note = 0;

# setup sensor input and output pins
for sensor in SENSORS:
	Setup(sensor['output'], sensor['input'], sensor['led'])

# Init virtual midi port
midi_out = rtmidi.MidiOut()
midi_out.open_virtual_port()

# loop
while True:
	
	for sensor in SENSORS:

		if (DEBUG):
			print("############ %s" % sensor['name'])

		value = CapRead(sensor['output'], sensor['input'])
		
		if ( value and ( value != sensor['last_value'] ) ):
			
			print("############ %s" % sensor['name'])
			#if (sensor['note'][BANK-1] == 0):
			if (sensor['type'] == BANK_CHANGE):
				# change bank request
				ChangeBank()
				note = 0
			elif (sensor['type'] == BANK_SELECT):
				note = sensor['note'][BANK-1]
			elif (sensor['type'] == RANDOM):
				# stuff for ramdom type
				note = note
			elif (sensor['type'] == SEQUENTIAL):
				# stuff for sequential sensor type
				sensor['seq_next'] += 1
				if ( sensor['seq_next'] >= len(sensor['note']) ):
					sensor['seq_next'] = 0
				note = sensor['note'][sensor['seq_next']]
			print ('Send Note ON: %d' % note)
			midi_out.send_message([0x90, note, 100]) # Note on

			# set sensor led ON
			wiringpi2.digitalWrite(sensor['led'], HIGH)


		elif ( value != sensor['last_value']  ):
			#if (sensor['note'][BANK-1] != 0):
			print("############ %s" % sensor['name'])

			if (sensor['type'] == BANK_SELECT):
				note = sensor['note'][BANK-1]
			elif (sensor['type'] == RANDOM):
				# stuff for ramdom type
				note = note
			elif (sensor['type'] == SEQUENTIAL):
				# stuff for sequential sensor type
				note = sensor['note'][sensor['seq_next']]

			print ('Send Note OFF: %d' % note)
			midi_out.send_message([0x80, note, 100]) # Note off
			# set sensor led Off
			wiringpi2.digitalWrite(sensor['led'], LOW)
			

		sensor['last_value'] = value

