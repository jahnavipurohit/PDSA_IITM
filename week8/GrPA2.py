'''In a 2-dimensional space, given two sets of n points 51 [p1, p2, .pn] and s2=[q1, q2, ....qn] 
on two parallel lines y=y1 and y=y2 respectively. Every point pi in $1 is connected to 
every corresponding point qi in 52 through a line segment. x1 and x2 are two lists that contains 
x coordinates of the points in set 51 and s2 respectively.
Write a Python function countintersection (X1, X2) that accepts the two Lists x1 and x2 as 
described above and returns the number of intersection points where the line segments intersect. 
The function should run in O(nlogn) time.'''

def mergeAndCount(A,B):
  (m,n) = len(A), len(B)
  (C, i, j, k, count) = ([], 0, 0, 0, 0)
  while k< m+n:
    if i == m:
      C.append(B[j])
      (j,k) = (j+1, k+1)
    elif j == n:
      C.append(A[i])
      (i,k) = (i+1, k+1)
    elif A[i] < B[j]:
      C.append(A[i]) 
      (i,k) = (i+1, k+1)
    else:
      C.append(B[j])
      (j, k, count) = (j+1, k+1, count+(m-i))
  return (C,count)

def sortAndCount(A):
  n = len(A)

  if n <= 1:
    return(A,0)
  
  (L,countL) = sortAndCount(A[:n//2])
  (R,countR) = sortAndCount(A[n//2:])
  
  (B,countB) = mergeAndCount(L,R)
  
  return(B,countL+countR+countB)

def countIntersection(X1, X2):
  # Sort according to one points while keeping the matching of points in X1 to X2
  combined = [(X1[i], X2[i]) for i in range(0, len(X1))]
  combined.sort()
  X1, X2 = zip(*combined)

  # Now we just need to count the inversions in X2 for number of intersection points.
  return sortAndCount(X2)[1]
L1 = [int(i) for i in input().split(" ")]
L2 = [int(i) for i in input().split(" ")]
timeout = 2.0  # Timeout in sec
