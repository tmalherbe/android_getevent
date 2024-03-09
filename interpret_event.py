#!/usr/bin/python

from enum import Enum
import sys
#import file

Event_type = Enum('Event_type', ['EV_ABS', 'EV_SYN'])
Event_name = Enum('Event_name', ['ABS_MT_TRACKING_ID', 'ABS_MT_POSITION_X', 'ABS_MT_POSITION_Y', 'ABS_MT_PRESSURE', 'SYN_REPORT'])

def parse_event_line(event_line):
	#print(event_line)
	
	event_line = event_line.strip()

	parsed_event_line = ()

	x1 = event_line.find("EV_ABS")
	x2 = event_line.find("EV_SYN")

	#print(f"x1 {x1}")

	if x1 != -1:
		#print(f"x {x}")
		y = event_line[x1:].find("ABS_MT_TRACKING_ID")
		z = event_line[x1:].find("ABS_MT_POSITION_X")
		t = event_line[x1:].find("ABS_MT_POSITION_Y")
		u = event_line[x1:].find("ABS_MT_PRESSURE")
		#print(f"x {x}")print(f"y {y}")

		if y != -1:
			parsed_event_line = Event_type['EV_ABS'], Event_name['ABS_MT_TRACKING_ID'], event_line[-8 : ]
		elif z != -1:
			parsed_event_line = Event_type['EV_ABS'], Event_name['ABS_MT_POSITION_X'], event_line[-8 : ]

		elif t != -1:
			parsed_event_line = Event_type['EV_ABS'], Event_name['ABS_MT_POSITION_Y'], event_line[-8 : ]

		elif u != -1:
			parsed_event_line = Event_type['EV_ABS'], Event_name['ABS_MT_PRESSURE'], event_line[-8 : ]

		else:
			return parsed_event_line

	elif x2 != -1:
		y = event_line[x2:].find("SYN_REPORT")

		if y != -1:
			parsed_event_line = Event_type['EV_SYN'], Event_name['SYN_REPORT'], event_line[-8 : ]

	else:
		return parsed_event_line

	#parsed_event_line.append

	return parsed_event_line

def parse_raw_events_list(raw_events_list):

	events_list = []

	for line in raw_events_list:
		parsed_line = parse_event_line(line)
		#print(f"{parsed_line}")

		events_list.append(parsed_line)

	return events_list

print(sys.argv[0])

def usage():
	print("usage")

def extract_events_sequence(events_list):
	#print(events_list)
	#print(len(events_list))

	coordinate_list = []

	a = 0
	b = 0
	c = 0
	d = 0
	e = 0
	
	coord_x = ""
	coord_y = ""

	i = 0
	while i < len(events_list):

		#print("debut boucle")
		#print(len(event))
		
		#if len(event) == 0:
		#	print("nulle")
		#	i+=1
		#	continue
		
		#else:

		event = events_list[i]
		#print(f"{i+1} {event}")

		ev_type = event[0]
		ev_name = event[1]	

		if ev_type == Event_type['EV_ABS'] and ev_name == Event_name['ABS_MT_TRACKING_ID']:
			#print("a")
			a = 1
			b = 0 ; c = 0 ; d = 0 ; e = 0
			coord_x = ""
			coord_y = ""
	
		if ev_type == Event_type['EV_ABS'] and ev_name == Event_name['ABS_MT_POSITION_X']:
			#print("b")
			b = 1		
			coord_x = event[2]

		if ev_type == Event_type['EV_ABS'] and ev_name == Event_name['ABS_MT_POSITION_Y']:
			#print("c")
			c = 1
			coord_y = event[2]

		if ev_type == Event_type['EV_ABS'] and ev_name == Event_name['ABS_MT_PRESSURE']:
			#print("d")
			d = 1

		if ev_type == Event_type['EV_SYN'] and ev_name == Event_name['SYN_REPORT']:
			#print("e")
			e = 1	
		#i += 1

		if a * b * c * d * e == 1:
			#print(f"Found coord ({coord_x}, {coord_y})")
			a = 0 ; b = 0 ; c = 0 ; d = 0 ; e = 0
			
			coordinate_list.append((int(coord_x, 16), int(coord_y, 16)))		
		i+=1

	return coordinate_list

def coordinate_to_char(coordinate):
	x = coordinate[0]
	y = coordinate[1]
	#print(f"({x}, {y})")
	
	if (x > 0x00f0 and x < 0x0b00 and y < 0x5828 and y > 0x5e65):
		print("q")
		return

	if (x > 0x0f2b and x < 0x180e and y <  0x5e65 and y > 0x5887):
		print("w")
		return

	if (x > 0x1bd9 and x < 0x2518 and y <  0x5ddd and y > 0x5887):
		print("e")
		return

	if (x > 0x295c and x < 0x329b and y < 0x5e3c and y > 0x58d9):
		print("r")
		return

	if (x > 0x34e9 and x < 0x3fff and y < 0x5e13 and y > 0x57ff):
		print("t")
		return

	if (x > 0x4332 and x < 0x4b41 and y < 0x5e3c and y > 0x58b0):
		print("y")
		return

	if (x > 0x4f2a and x < 0x573a and y < 0x5db4 and y > 0x5887):
		print("u")
		return

	if (x > 0x5c52 and x < 0x6517 and y < 0x5e8e and y > 0x58d9):
		print("i")
		return

	if (x > 0x6901 and x < 0x7110 and y < 0x5ddd and y > 0x5851):
		print("o")
		return

	if (x > 0x749e and x < 0x7d63 and y < 0x5e13 and y > 0x5851):
		print("p")
		return

	if (x > 0x095c and x < 0x1240 and y < 0x6665 and y > 0x60d9):
		print("a")
		return

	if (x > 0x15b0 and x < 0x1f68 and y < 0x6665 and y > 0x60b0):
		print("s")
		return

	if (x > 0x2203 and x < 0x2bbb and y < 0x668e and y > 0x60d9):
		print("d")
		return

	if (x > 0x2f2b and x < 0x3869 and y < 0x66b7 and y > 0x6102):
		print("f")
		return

	if (x > 0x3bd9 and x < 0x4407 and y < 0x66ee and y > 0x60d9):
		print("g")
		return

	if (x > 0x482c and x < 0x51e4 and y < 0x66ee and y > 0x612b):
		print("h")
		return

	if (x > 0x54f9 and x < 0x5ddd and y < 0x663c and y > 0x60b0):
		print("j")
		return

	if (x > 0x614c and x < 0x6a8b and y < 0x6606 and y > 0x60d9):
		print("k")
		return

	if (x > 0x6f2a and x < 0x7739 and y < 0x65dd and y > 0x6102):
		print("l")
		return

	if (x > 0x15b0 and x < 0x1e38 and y < 0x6e8e and y > 0x697d):
		print("z")
		return

	if (x > 0x22d7 and x < 0x2b42 and y < 0x6e8e and y > 0x692b):
		print("x")
		return

	if (x > 0x2f2b and x < 0x38c4 and y < 0x6eb7 and y > 0x692b):
		print("c")
		return

	if (x > 0x3c52 and x < 0x44bd and y < 0x6f09 and y > 0x6902):
		print("v")
		return

	if (x > 0x48a6 and x < 0x5189 and y < 0x6e8e and y > 0x68cb):
		print("b")
		return

	if (x > 0x55af and x < 0x5ddd and y < 0x6eb7 and y > 0x692b):
		print("n")
		return

	if (x > 0x6203 and x < 0x6b41 and y < 0x6eb7 and y > 0x6954):
		print("m")
		return

def coordinate_list_to_string(coordinate_list):
	for coordinate in coordinate_list:
		coordinate_to_char(coordinate)

def main():

	if len(sys.argv) < 2:
		usage()
		exit()

	fd = open(sys.argv[1], 'r')

	raw_events_list = fd.readlines()
	fd.close()

	events_list = parse_raw_events_list(raw_events_list)
	coordinate_list = extract_events_sequence(events_list)
	coordinate_list_to_string(coordinate_list)

if __name__ == "__main__":
	main()
