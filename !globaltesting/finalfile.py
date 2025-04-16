import argparse
import pathlib
import os
from collections import defaultdict

def func(N):
	dirname = pathlib.Path(N)
	os.chdir(dirname)
	# считываются данные из файла в формате: число решений, кнф  далее строки с решениями
	f = open(N + '.txt', "r")

	# файл res для записи результата работы функции
	result = open(N + 'res.txt', 'w')

	# считываем все строки файла в список
	forparsing = []
	for line in f:
		forparsing.append(line[:-1])
#	print(*forparsing, sep = '\n')

	# заполняем словарь, {количество решений:{название кнф файла:конфигурация решений}}
	dd = defaultdict(dict)
	for i in range(len(forparsing)):
		if 'for' in forparsing[i]:
			# парсим строку и выделяем кол-во решений и название кнф
			l = int(forparsing[i][0:2])
			cnf = '(' + forparsing[i][(forparsing[i].index('r') + 2):(forparsing[i].index('n') + 2)] + ')'
			# сохраняем конфигурацию решений этой кнф в отдельный временный перезаписываемый массив
			val = []
			for j in range(l):
				line = forparsing[i + 1 + j][1:-1]
				val.append(line)
			val.sort()
			# если такой конфигурации решений еще нет по ключу "количество решений", то добавляем как вложенный словарь {кнф: конфигурация}
			if val not in dd[l].values():
				info = dd[l].setdefault(f'{cnf}',val)
			# если конфигурация уже есть, то находим соответствующий ей кнф файл и удаляем его	
			else:
				print(cnf)
				os.remove(f'{cnf[1:-1]}')
			# перемещаем каретку по массиву на кол-во строк конфигурации(кол-во решений) вниз, то есть к след строке формата "количество решений и имя кнф"
			i = i + l			
	f.close()
#	print(*dd)

	# сортируем словарь по ключам - количествам решений для удобства
	d = dict(sorted(dd.items()))
#	print(d)

	# БЛОК ПОДСЧЁТА ИНВЕРСНЫХ ПАР
	# скачем по ключам - кол-ву решений
	for key in d.keys():
		# пишем в файл res кол-во решений:
		result.write(f'{key}:\n')
		# перебираем список значений по каждому словарю {кнф:список конфигураций}
		for cnfname in d.get(key):
			# пишем в файл res имя кнф:
			result.write(f'{cnfname}:\n')
#			print(cnfname)
			# записываем конфигурацию в список
			configuration = list(d.get(key).get(cnfname))
#			print(configuration)
			# создаем массив массивов, где каждую строка конфигурации (она в формате строки)- массив интов 
			res = []
			# перебираем конфигурацию поэлементно (по решениям) и преобразуем в массив интов
			for k in range(len(configuration)):
				s = configuration[k].split(', ')
#				print(s)
				for m in range(len(s)):
					s[m] = int(s[m])
				res.append(s)
#			print(res)
			# заводим счетчик инверсных пар и массив для их накопления
			cntinv = 0
			invers = []
			# перебираем массив res в поиске инверсных пар
			for i in range(len(res)):
				# создаем искусственно инверсную пару для каждого элемента массива
				temp = [-x for x in res[i]]
				for j in range(len(res)):
					if res[i] not in invers and res[j] == temp and i != j:
						invers.append(res[i])
						invers.append(temp)
						cntinv += 1
			result.write(f'Количество инверсных пар: {cntinv}:\n')
			if cntinv in [1, 3, 5]:
				URA = open('URA' + N + '.txt', "a")
				URA.write(f'{cnfname} {key} решений \n')
				for k in range(len(configuration)):
					URA.write(f'{configuration[k]}\n')
				URA.write(f'Количество инверсных пар:  {cntinv}\n')
				for j in range(len(invers)):
					URA.write(f'{invers[j]}\n')
				URA.close()
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
