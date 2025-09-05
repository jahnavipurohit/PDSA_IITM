'''Frequency of elements

Given a list of integers sorted in ascending order, 
find the number of occurrences for a given element in the list. 
The worst case running time of your program should be 

Write a function countOccurrence(AList, size, key) which returns the frequency of key in AList. 
If the element is not present in the list, your function should return 0.

Example

If the input list AList is : [3,3,4,4,4,5,6,6,9,9,9,9,9,10,10] and the key is 6, 
your program should return 2.

Note:- Do not use slicing in solution code for the list because it is O(n) operation.

Sample Input 1
[100,200,300,300,400] #AList
300 #key
Output
2 #Occurrence of key in AList

Sample Input 2
[2,3,3,8,9,10,10]
5
Output
0'''

def countOccurrence(AList, size, key):
	firstindex = firstOccurrence(AList, 0, size-1, key, size)
	if firstindex == 0:
		return firstindex
	lastindex = lastOccurrence(AList, 0, size-1, key, size);	
	return lastindex-firstindex+1

def firstOccurrence(AList, low, high, key, size):
	if high >= low:
		mid = (low + high)//2	
		if (mid == 0 or key > AList[mid-1]) and AList[mid] == key:
			return mid
		elif key > AList[mid]:
			return firstOccurrence(AList, (mid + 1), high, key, size)
		else:
			return firstOccurrence(AList, low, (mid -1), key, size)
	return 0

def lastOccurrence(AList, low, high, key, size):
	if high >= low:
		mid = (low + high)//2;
		if(mid == size-1 or key < AList[mid+1]) and AList[mid] == key :
			return mid
		elif key < AList[mid]:
			return lastOccurrence(AList, low, (mid -1), key, size)
		else:
			return lastOccurrence(AList, (mid + 1), high, key, size)	
	return 0