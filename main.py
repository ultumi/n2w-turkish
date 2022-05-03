# -*- coding: utf-8 -*-

def n2w(number):
	# NORMALIZATION
	inputvalue = ""
	for i in number:
		if i.isnumeric():
			inputvalue += i
	number = inputvalue

	while number[0] == "0" and len(number) > 1:
		number = number[1:]

	#DICTIONARIES
	ones = {"0": "",
			"1": "bir",
			"2": "iki",
			"3": "üç",
			"4": "dört",
			"5": "beş",
			"6": "altı",
			"7": "yedi",
			"8": "sekiz",
			"9": "dokuz"}

	tens = {"0": "",
			"1": "on",
			"2": "yirmi",
			"3": "otuz",
			"4": "kırk",
			"5": "elli",
			"6": "altmış",
			"7": "yetmiş",
			"8": "seksen",
			"9": "doksan"}

	hundreds = {"0": "",
			"1": "yüz",
			"2": "iki yüz",
			"3": "üç yüz",
			"4": "dört yüz",
			"5": "beş yüz",
			"6": "altı yüz",
			"7": "yedi yüz",
			"8": "sekiz yüz",
			"9": "dokuz yüz"}
	
	unitnames = ["", "bin ", "milyon ", "milyar ", "trilyon ", "katrilyon "]

	#SLICING 3-UNITS
	units = []
	while len(number) > 3:
		units.append(number[-3:])
		number = number[:-3]
	units.append(number)
	units.reverse()

	#INTERPRETING
	i = 0
	result = ""
	unitnames = unitnames[:len(units)]
	unitnames.reverse()
	for unit in units:
		if len(unit) == 1 and unit[0] == "0":
			result += "sıfır"
		elif len(unit) == 1:
			result += ones[unit[0]] + " "
		elif len(unit) == 2:
			result += tens[unit[0]] + " " + ones[unit[1]] + " "
		else:
			result += hundreds[unit[0]] + " " + tens[unit[1]] + " " + ones[unit[2]] + " "
		if unit != "000":
			result += unitnames[i]			
		i += 1

	if len(units) >= 2 and units[-2] == "001":
		result = result.replace("bir bin", "bin")

	return " ".join(result.split())

print(n2w("84.680.273"))