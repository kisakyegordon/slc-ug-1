def primes(n):
   j = 2
   primes = []
   while j <= n:
       k = 2
       while not(k == j) and not(j%k == 0):
           k = k + 1
       if k == j:
           primes.append(j)
       j = j + 1
   print primes
   
   
primes(20)  