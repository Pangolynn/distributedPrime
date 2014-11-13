distributedPrime
================

Server/Client distributed prime number tester

serverPrime.py starts a server with a specified port using RPyC
serverPrime.py provides an exposed method called "return_primes".
This method requires one parameter, an integer. 
Calling this method will return a string of all prime numbers up to the given input.

For example:
  return_primes(10)
will return a string of 2 3 5 7

clientPrime.py provides the means of connecting to the service created by serverPrime.
clientPrime.py is used to get input as an integer, and call serverPrime.py's exposed method
"return_primes" with the given input. It then prints out the result returned from serverPrime.py

The line rpyc.connect("192.168.0.112", port=12345) in clientPrime.py must be modified with the IP address you wish to connect to, and the port you want to connect through.

This code is written and should be mantained in python3 only.
