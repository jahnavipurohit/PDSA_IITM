'''A popular meeting hall in a city receives many overlapping applications to hold meetings. 
The manager wishes to satisfy as many customers as possible. Each application is a 
tuple (id, start_day, end_day) where id, start_day and end_day are the unique id assigned to the 
application, starting day of the meeting and ending day of meeting ends inclusive respectively. 
Write a function no_overlap (L) to return the list of customer ids whose applications are 
accepted that ensures optimal scheduling. Let L be a list tuples with (id, start_day, end_day).
Sample Input
L = [
(0, 1, 2),
(1, 1, 3),
(2, 1, 5),
(3, 3, 4),
(4, 4, 5),
(5, 5, 8),
(6, 7, 9),
(7, 10, 13),
(8, 11, 12)
]
Sample output
[0, 3, 6, 8]'''

def tuplesort(L, index):
    L_ = []
    for t in L:
        L_.append(t[index:index+1] + t[:index] + t[index+1:])
    L_.sort()

    L__ = []
    for t in L_:
        L__.append(t[1:index+1] + t[0:1] + t[index+1:])
    return L__

def no_overlap(L):
    sortedL = tuplesort(L, 2)
    accepted = [sortedL[0][0]]
    for i, s, f in sortedL[1:]:
        if s > L[accepted[-1]][2]:
            accepted.append(i)
    return accepted 