import rpyc

class PrimeService(rpyc.Service):
    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def check_Prime(self, number):
        i=1
        primes = ""
        #any factors must be less than the square root
        #of the number, +1 for python not including upper limit
        upper=int((number ** 0.5))+1
        for i in range(2,upper):
            if number % i == 0: #composite -- do nothing
                break
        else:
            primes = str(number) #prime
        return primes #empty string if not prime, otherwise string of #

    def exposed_return_primes(self, number):
        allPrimes = ""
        if number > 1:
            for j in range(2, number+1):
               allPrimes += str(self.check_Prime(j)) #add each prime to str
        else:
            print("1 is not a prime number, and has no primes before it")
        return allPrimes #string containing all prime numbers

#Necessary to start server
from rpyc.utils.server import ThreadedServer
t = ThreadedServer(PrimeService, port = 12345)
t.start()



