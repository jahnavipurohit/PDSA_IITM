'''Goldbach's conjecture is one of the oldest and best-known unsolved problems in number theory. 
It states that every even number greater than 2 is the sum of two prime numbers.
For Example:
12 = 5+7
26323 or 7 + 19 or 13 +13
Write a function Goldbach(n) where n is a positive even number n > 2 ) 
that returns a list of tuples. In each tuple (a, b) where a <= b, 
a and b should be prime numbers and the sum of a and b should be equal to n.
Sample Input 1
1 12
Output
1[(5,7)]
Sample Input 2
1 26
Output
1 [(3,23),(7,19),(13,13)]'''

def prime(n):
  if n < 2:
    return False
  for i in range(2,n//2+1):
    if n%i==0:
      return False
  return True

def Goldbach(n):
  Res=[]
  for i in range((n//2)+1):
    if prime(i)==True:
      if prime(n-i)==True:
        Res.append((i,n-i))
  return(Res)

n=int(input())
print(sorted(Goldbach(n)))