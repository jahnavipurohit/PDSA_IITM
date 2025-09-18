'''Write a Python function MoM7Pos(arr) that accepts a list arr of integers(not necessarily distinct) 
and computes the median of medians(of blocks) м dividing the list arr into blocks of 7 and returns 
the position of m in arr if it were sorted. If mis repeated more than once in the list arr return 
the index of first occurrence of m in arr if it were sorted.
For simplicity the size of arr will be a multiple of 7. Your solution should run in O(n) time.
Sample Input
44 9 31 12 15 98 48 45 13 75 23 6 35 74
Sample Output
7'''

def partitionPos(arr, pivot):
  arr[pivot], arr[0] = arr[0], arr[pivot]
  l = 1
  r = len(arr)-1
  while (l<r):
    while(arr[l] < arr[0]):
      l+=1
    while(arr[r]>=arr[0]):
      r-=1
    arr[l], arr[r] = arr[r], arr[l]

  return l-1

def MoM7(arr):
  if len(arr) <= 7:
    arr.sort()
    return(arr[len(arr)//2])

  # Construct list of block medians
  M = []

  for i in range(0, len(arr), 7):
    X = arr[i:i+7]
    X.sort()
    M.append(X[len(X)//2])

  return(MoM7(M))

def MoM7Pos(arr): 
  mom = MoM7(arr)
  return partitionPos(arr, arr.index(mom))
arr=[int(item) for item in input().split(" ")]
print(MoM7Pos(arr))