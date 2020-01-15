import math

def is_prime(number):
        
    root = math.floor(pow(number, 0.5))
    
    prime = True
    
    for i in range(2, root):
        if number % i == 0:
            #print (number, "is a Composite number. A factor is", i)
    
            return False
            break
        
    if prime == True:
        #print (number, " is a Prime number")
        return True

# Testing
is_prime(3243)

number = 600851475143

for x in range(math.floor(pow(number, 0.5)),2):
    if number % x == 0:
        if is_prime(x):
            print (x, 'is the largest prime factor')
            break

