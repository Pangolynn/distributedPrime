# Joseph Pannizzo
# RPYC Client
#edited by Samantha Holloway 11/14

import rpyc

def sentPrime(input): 
    # host needs to be changed for remote access
    conn = rpyc.connect("192.168.0.112", 12345) # connect to the server on my local machine for testing.
    print(conn) # print connection
    print(conn.root.return_primes(input)) # send input to return primes, then print
    
# --Start Program--
input = int(input("Enter a number: ")) # ask user for number
sentPrime(input) # send input to sentPrime function
