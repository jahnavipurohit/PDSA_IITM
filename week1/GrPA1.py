'''Write a function find_Min_Difference(L, P) that accepts a list L of integers 
and P (positive integer) where the size of L is greater than P. 
The task is to pick P different elements from the list L, where the difference between
the maximum value and the minimum value in selected elements is minimum compared to 
other differences in possible subset of p elements. 
The function returns this minimum difference value.
Note - The list can contain more than one subset of p elements that have the same minimum difference value.

Example

Let L = [3, 4, 1, 9, 56, 7, 9, 12, 13] and P = 5

If we see the following two subsets of 5 elements from L

[3, 4, 7, 9, 9] or [7, 9, 9, 12, 13]

Here, the difference between the maximum value and the minimum value
in both subset is 9 - 3 = 6 or 13 - 7 = 6 which is minimum. So the output will be 6.'''

def find_Min_Difference(L,P):
  L.sort()
  N = P
  M = len(L)
  min_diff = max(L) - min(L)
  for i in range(M-N+1):
    if L[i+N-1] - L[i] < min_diff:
      min_diff = L[i+N-1] - L[i]
  return min_diff

L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))