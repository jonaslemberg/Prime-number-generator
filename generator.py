import math

def isnumeric(i):

	# checks if the input is numeric
    return all(char in "0123456789.-+" for char in i)

def output(primes, size):

	# prints the list of prime numbers in a 10 column table
    row_count = 0
    r = ""
    
    for x in range(0, len(primes)):
        size_p = len(str(primes[x]))
        space = (size - size_p)*" "
        r += space + str(primes[x]) + " "
        row_count += 1
        if row_count == 9:
            r += space + str(primes[x])
            print(r)
            row_count = 0
            r = ""
    
    if r != "":
        print(r)

def main():

    x = "a"
    y = "b"

	#check if input is numeric
    while isnumeric(x) == False:
        x = input("Enter a number: ")
    
    while isnumeric(y) == False:
        y = input("Enter another number: ")
    
	# save the original numbers for later printing
    x_old = x
    y_old = y
	
    x = math.ceil(float(x))
    y = math.trunc(float(y))
    
	# if any of the given integers are negative, start generating numbers starting from 0, since there are no negative prime numbers.
    if x < 0:
        x = 0
    
    if y < 0:
        y = 0
    
	# if the second number given is smaller than the first number, the variable add gets a negative value
    if y < x:
        add = -1
        size = len(str(x))
    else:
        add = 1
        size = len(str(y))
        
    print("\nPrime numbers in the range {:s}".format(x_old),"- {:s}:\n".format(y_old))

	diff = abs(y - x) #the difference between the two given numbers
    primes = []
    
    for i in range (0, diff+1):
        num = x + (i*add)
        div = 2
        prime = 1
        while div <= num and prime == 1:
            if num % div == 0 and div < num:
                prime = 0
            elif div == num:
                primes.append(num)
            div += 1
    
    output(primes, size) #print the table
    
main()
