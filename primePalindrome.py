def primePalindrome(self, N):
   """
   :type N: int
   :rtype: int
   """

   def is_prime(n):
       i = 1
       ctr = 0
       while (i <= n):

           if (n % i == 0):
               ctr = ctr + 1
           i = i + 1
       if (ctr == 2):
           return True

   i = 0
   val = 0
   while (i == 0):
       N = N + 1
       if (is_prime(N) == True):
           if (str(N) == str(N)[::-1]):
               i=1
   return N
if __name__=="__main__":
<<<<<<< HEAD:primePalindrome.py
   print(primePalindrome("self",10000))
=======
   print(primePalindrome("self",100000))
>>>>>>> 31c7e357a98ed26fa8e75fac2f2b2fca14b1015f:PrimePalindrome.py
