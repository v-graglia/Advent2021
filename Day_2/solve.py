import os

cwd = os.path.dirname(os.path.abspath(__file__)) + "\\"
data = []

with open(cwd +  "input.txt") as f:
	data = f.read().split('\n')
	
	data = [x.split(" ") for x in data]
	data = [[x, int(y)] for x,y  in data]

print("\n\nPart 1:\n---------------------------------------------")

hor = 0
depth = 0

for direction, units in data:
	if direction == "forward":
  		hor += units		
	elif direction == "up":
  		depth -= units
	else:
  		depth += units

print("Horizontal position: " + str(hor) + "\nDepth: " + str(depth))
print("Horizontal position * Depth = " + str(hor * depth))
print("---------------------------------------------")

print("\nPart 2:\n---------------------------------------------")

aim = 0
hor = 0
depth = 0

for direction, units in data:
	if direction == "forward":
		hor += units
		depth += aim * units
	elif direction == "up":
  		aim -= units
	else:
		aim += units

print("Horizontal position: " + str(hor) + "\nDepth: " + str(depth))
print("Horizontal position * Depth = " + str(hor * depth))
print("---------------------------------------------")

