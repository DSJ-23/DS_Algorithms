class Prime:

    prime = {0: False, 1:False, 2:True, 3: True, 4:False}

    def countPrimes(self,n):
        prime_total = 0
        for num in range(2,n):
            if self.isPrime(num):
                prime_total = prime_total + 1
        return prime_total

    def isPrime(self, n):
        if n in self.prime:
            return self.prime[n]
        else:
            for i in range(2,n):
                if n % i == 0:
                    self.prime[n] = False
                    return False
        self.prime = True
        return True

a = Prime()
# print(a.isPrime(10))
print(a.countPrimes(10))