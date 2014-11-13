# Joseph Pannizzo
# RPYC Client

import rpyc

def sentPrime(input): 
    # host needs to be changed for remote access
    conn = rpyc.connect("127.0.0.1", 12345) # connect to the server on my local machine for testing. 
    print conn # print connection
    print conn.root.return_primes(input) # send input to return primes, then print
    
# --Start Program--
input = int(input("Enter a number: ")) # ask user for number
sentPrime(input) # send input to sentPrime function
