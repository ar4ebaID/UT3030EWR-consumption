import os
import fnmatch


def work_file(item):
	file = open(item, 'r')
	count, itog, minimum, maximum = 0, 0, 1, 0

	for item_file in file:
		count += 1
		item1 = item_file.split('	')
		res = item1[2].split('A')
		res_float = float(res[0])

		if minimum > res_float:
			minimum = res_float*1000//1/1000
		if maximum < res_float:
			maximum = res_float*1000//1/1000

		itog += res_float

	srednee = (itog / count)*1000//1/1000
	
	print(' AVERAGE:', str(srednee)+' (A)', '\n',
		  'MIN:', str(minimum)+' (A)', '\n',
		  'MAX:', str(maximum)+' (A)', '\n')

	file.close()

while True:
	ent = input("To scan a folder, press Enter:\n")
	
	if ent == "":
		files = os.listdir('.')
		txt_files = fnmatch.filter(files, '*.txt')
		
		for h in txt_files:
			print('Use the file ',h + '?')
			ent1 = input()

			if ent1 == "":
				work_file(h)
				
				print(' Delete file ', h, '? ', '\n',
					  ' Enter — Yes', '\n',
					  ' Ctrl-c — Exit', sep='')
				razrechenie = input()
								
				if razrechenie == "":
					os.remove(h)
					break

		print("There are no more files with the '.txt' extension\n",
		' Ctrl-c — Exit\n')
