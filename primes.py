# Write a function that generates a list of the primes from 1 - 250
def genPrimesList():
    list = []

    # Add 2
    list.append(2)

    # Add the rest. No need to test even numbers
    for i in range(3, 250, 2):
        addIt = True
        
        for j in range(2, i // 2):
            if i % j == 0: addIt = False
        
        if addIt: list.append(i)

    return list

output = open("primes.txt", 'w')

for i in genPrimesList():
    output.write("{} ".format(i))