'''Write a Python function listunion (L1, L2) that accepts two integer lists L1 and L2 
and return a list that is the union(L1 u L2) of the two lists and is sorted in ascending order. 
Try to write a solution that runs in o(n log n) time.
L1 contains all distinct integers and L2 contains all distinct integers, 
but there can be many elements common between L1 and L2.
List L1 U L2 contains all distinct elements of L1 and L2 combined, 
and is sorted in ascending order'''

def listUnion(L1, L2):
  L1.sort()
  L2.sort()
  L3 = []

  s1 = len(L1)
  s2 = len(L2)

  p1 = p2 = 0
  while (p1<s1 and p2<s2):
    if (L1[p1] == L2[p2]):
      L3.append(L1[p1])
      p1+=1
      p2+=1
    elif (L1[p1] < L2[p2]):
      L3.append(L1[p1])
      p1+=1
    else:
      L3.append(L2[p2])
      p2+=1
  
  while(p1<s1):
    L3.append(L1[p1])
    p1+=1
  while(p2<s2):
    L3.append(L2[p2])
    p2+=1  
  return L3

set1 = [int(item) for item in input().split()]
set2 = [int(item) for item in input().split()]
print(*listUnion(set1, set2))