import argparse  

def Main():
	parser=argparse.ArgumentParser()								#for getting numbers from comment line
	parser.add_argument('numbers', type=float, nargs='+',
                        help='an numbers for the process')
	args= parser.parse_args()
	Numbers =args.numbers	#sort the numbers
	Numbers.sort()
	print(Numbers)
	print("The Maximum Number is",Numbers[-1]) 		 
	print("The Minimum Number is",Numbers[0])
	
if __name__ == '__main__':
	Main()