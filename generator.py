import time
import psutil
import qsharp

from Qrng import SampleQuantumRandomNumberGenerator # We import the 
# quantum operation from the namespace defined in the file Qrng.qs

try:
    log_file = open("log.txt", 'r') #Opening the file for reading the last X coordinate
    lines = log_file.readlines() #Extracting each line as a list
    x,y = lines[len(lines)-1].split(',') #Extracting the last value of X
except:
    x = '-1'

while True:
    
    time.sleep(0.2) #pause between the numbers generated
    log_file = open("log.txt",'a') #opening file for writing
    
    max = 50 # Here we set the maximum of our range
    output = max + 1 # Variable to store the output
    while output > max:
        bit_string = [] # We initialise a list to store the bits that
        # will define our random integer
        for i in range(0, max.bit_length()): # We need to call the quantum
            # operation as many times as bits are needed to define the
            # maximum of our range. For example, if max=7 we need 3 bits
            # to generate all the numbers from 0 to 7. 
            bit_string.append(SampleQuantumRandomNumberGenerator.simulate()) 
            # Here we call the quantum operation and store the random bit
            # in the list
        output = int("".join(str(x) for x in bit_string), 2) 
    # Transform bit string to integer
    print("The random number generated is " + str(output)) #Printing the numbers generated
    
    x = str(int(x) + 1) #Adding X coordinate
    log_file.write(x+","+str(output)+"\n") #Wrting the x and y coordinates in the file
    log_file.close() #Closing the file