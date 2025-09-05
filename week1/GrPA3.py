'''Write a function named odd_one (L) that accepts a list Las argument. 
Except for one element, all other elements in Lare of the same data type. 
The function odd_one should return the data type of this odd element.
For example, if L is equal to [1, 2, 3.4, 5, 10], then the function should return the string float. 
This is because the element 3.4 is the odd one here, all other elements are integers.
Note
(1) L has at least three elements.
(2) For each test case, the elements in the list will only be of one of these four types: int, float, str, bool.
(3) The function must return one of these four strings: int, float, str, bool.
(4) Hint: type(1) == int evaluates to True.'''

def odd_one(L):
  P = {}
  for elem in L:
    if type(elem) not in P:
      P[type(elem)] = 0
    P[type(elem)] += 1
  for key, value in P.items():
    if value == 1:
      return key.__name__
    
print(odd_one(eval(input().strip())))