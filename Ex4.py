import argparse
maximum = 100
PrimeNumbers = []
OutputArray = []


def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("Num", metavar='N', type=int, choices=range(1,maximum),help='Input number for the process')

	ssd = parser. parse_args()
	NumIn = ssd.Num
	PrimeNumbers = [2, 3,5 ,7] 		# inserting prime numbers into the array
	for number in range(3, maximum, 1):
		if (number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0):
			PrimeNumbers.append(number)

	#print(PrimeNumbers)
	for primeNo in PrimeNumbers:

		while NumIn % primeNo == 0:
			NumIn = NumIn/primeNo
			OutputArray.append(primeNo)
			print(NumIn)

	print(OutputArray)

if __name__ == '__main__':
	Main()

