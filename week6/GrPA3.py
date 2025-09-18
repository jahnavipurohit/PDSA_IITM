'''Given an array based min Heap arr, write a Python function min_max(arr) that to convert 
arr to a max Heap. The function should change the original arr to max heap. 
The expected time complexity is O(n).'''

def heapify(A, n, i):
    largest = i  
    l = 2 * i + 1    
    r = 2 * i + 2     
    if l < n and A[largest] < A[l]:
        largest = l
    if r < n and A[largest] < A[r]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i] 
        heapify(A, n, largest)
 

def min_max(A):
    n = len(A)
    for i in range(n//2,-1,-1):
        heapify(A,n,i)