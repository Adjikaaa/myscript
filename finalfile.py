import argparse, subprocess, sys
#sys.stdout = open('result.txt', 'w')

def perebor():
	while True:
		for num in file:
			for line in range(int(num)):
				line = line[1, -1]
			    lst = list((line.strip()).split(", "))
			    print(lst)
		temp = file.tell()
		file.seek(temp+2)

file = open("somefile.txt", "r")
arr = []

file.close()