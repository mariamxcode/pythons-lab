sum = 0
for number in range(100,1000):
    while number != 0:
	    digit = number % 10
	    number = number / 10
	    sum+=digit*digit
    if sum == number:
        print(number)
       
    
