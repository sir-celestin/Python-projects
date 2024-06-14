# calculate number of k-permutations of n items
# Celestin Nahimana
# 17 April 2024

def get_integer(n):
   
   numb = input (f"Enter {n}:\n")
   while not numb.isdigit ():
      numb = input (f"Enter {n}:\n")
   numb = eval (numb) 
   
   return numb 
   
 
def calc_factorial(nfactorial):
      total = 1
      for i in range (nfactorial,0,-1):
         total *= i
      return total

