import os 

def positive_increase(data):
	count = 0
	for i in range(1, len(data)):
		if data[i] > data[i-1]:
			count += 1
	return count

def positive_increase_window(data):
	count = 0
	for i in range(3, len(data)):
		if data[i] > data[i-3]:
			count += 1
	return count

cwd = os.path.dirname(os.path.abspath(__file__)) + "\\"
data = []

with open(cwd + "input.txt") as f:
	data = f.read().split('\n')
	data = [int(x) for x in data]

print("\nPart 1:\n-----------------------------")
print("Result:")
print(positive_increase(data))
print("-----------------------------")
print("\nPart 2:\n-----------------------------")
print("Result:")
print(positive_increase_window(data))
print("-----------------------------")

