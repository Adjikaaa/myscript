import argparse, subprocess, sys, pathlib, os
from collections import defaultdict


def func(N):
	dirname = pathlib.Path(N)
	os.chdir(dirname)
	f = open(N + '.txt', "r")
	result = open(N + 'res.txt', 'a')
	forparsing = []
	for line in f:
		forparsing.append(line[:-1])
	print(*forparsing, sep = '\n')

	d = defaultdict(list)
	print(len(forparsing))
	for i in range(len(forparsing)):
		if 'for' in forparsing[i]:
			l = int(forparsing[i][0:2])
			cnf = '(' + forparsing[i][(forparsing[i].index('n') - 6):(forparsing[i].index('n') + 2)] + ')'
			val = set()
			for j in range(l):
				line = forparsing[i + 1 + j][1:-1]
				val.add(line)
			val = set(sorted(val))
			if val not in d[l]:
				d[l].append([cnf])
				d[l].append(val)
			i = i + l			
	f.close()
	for key in d.keys():
		result.write(f'{key}: \n')
		lstvals = d.get(key)
		for k in range(len(lstvals)):
			res = []
			for elem in lstvals[k]:
				result.write(f'{elem}\n')
				if (list(lstvals[k])).index(elem) > 0:
					s = elem.split(', ')
					for m in range(len(s)):
						s[m] = int(s[m])
					res.append(s)
				cntinv = 0
				invers = []
				for i in range(len(res)):
					temp = [-x for x in res[i]] 
					for j in range(len(res)):
						if res[i] not in invers and res[j] == temp:
							invers.append(res[i])
							invers.append(temp)
							cntinv += 1
		result.write(f'Количество инверсных пар: {cntinv}:\n')
		for i in range(len(invers)):
			for j in range(len(invers[i])):
				result.write(f'{invers[i][j]} ')
			result.write('\n')
	result.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type = str)
    args = parser.parse_args()
    func(args.N)
