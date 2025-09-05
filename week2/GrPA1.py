'''Write a Python function combinationSort(strList) that takes a list of unique strings strList 
as an argument, where each string is a combination of a letter from a to z and a number from 0 to 99, 
the initial character in string being the letter. For example a23, d5, q99 are some strings in this format. 
This function should sorts the list and return two lists (L1, L2) in the order mentioned below.
L1: First list should contain all strings sorted in ascending order with respect to the first character only. 
All strings with same initial character should be in the same order as in the original list.
L2: In the list L1 above, sort the strings starting with same character, 
in descending order with respect to the number formed by the remaining characters.
Example:
Sample input 1:
d34, g54, d12, b87, g1, c65, g40, g5, d77
Sample output 1:
L1: b87, c65, d34, d12, d77, g54, g1, g40, g5
L2: b87, c65, d77, d34, d12, g54, g40, g5,g1'''

import string
def combinationSort(strList):
  # Create a dictionary with 26 keys from characters 'a' to 'z', each key has an empty list as value.
  groups = {k: [] for k in string.ascii_lowercase}

  # Using this dictionary to group strings with same initial character.  
  for i in range(len(strList)):
    char=strList[i][0]
    groups[char].append(strList[i])
  
  strList=[]
  # Recreate the list from all the strings in groups, iterating on groups from a to z.
  for char in groups.keys():
    for s in groups[char]:
      strList.append(s)
  
  L1 = strList.copy() # Saving intermediate result to return later.
  i = 1
  left = 0
  # As there can be no more than 100 strings with same initial character.
  # Using insertion sort within group.
  while i<len(strList):
    right = i
    while(right>left and strList[right][0] == strList[right-1][0] and int(strList[right-1][1:])<int(strList[right][1:])):
      strList[right], strList[right-1] = strList[right-1], strList[right]
      right -= 1
    i += 1
  
  return L1, strList