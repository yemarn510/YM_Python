from time import sleep
k = 0
x = 0
while (x <= 0):
	x = int(input("Enter the Positive Integer "))
	SleepTime = 1/x

while 1:
	k +=1
	if(k%15 == 0):
		print("FizzBuzz")

	elif(k%5 == 0):
		print("Buzz")

	elif(k%3 == 0):
		print("Fizz")
	
	else:
		print(k)

	sleep(SleepTime)
