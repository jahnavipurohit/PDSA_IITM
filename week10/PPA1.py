'''Write a Python function BMCount(t, p) that accepts two arguments a text t and a pattern p and 
implements a string-matching algorithm based on Boyer-Moore skipping heuristic discussed in lectures, 
and returns intermediate steps data as listed below.
Record the indexes of the characters in text t that will be matched with the last character of p 
in a list say skipl. skipt is the list of integers sorted in ascending order, where each integer 
is an index of a character in text t.
Also count the number of character comparisons performed between t and p in a variable say count
and finally return skipt and count from the function in the same order.
Sample Input
straw plus berry is strawberry #t
strawberry #p
Sample Output
0 9 18 19 20
14'''

def BMCount(t, p):
    n = len(t)
    m = len(p)
    skipl = []
    count = 0

    # Bad character shift table
    bad_char = {}
    for i in range(m):
        bad_char[p[i]] = i

    s = 0  # shift of pattern
    while s <= n - m:
        j = m - 1

        # record the starting index of this alignment
        skipl.append(s)

        # compare from right to left
        while j >= 0 and p[j] == t[s + j]:
            count += 1
            j -= 1

        if j < 0:  # full match found
            # shift the pattern
            s += m - bad_char.get(t[s + m - 1], -1) if s + m < n else 1
        else:
            count += 1
            s += max(1, j - bad_char.get(t[s + j], -1))

    skipt = sorted(skipl)
    return skipt, count


t = input()
p = input()
list, c = BMCount(t, p)
print(*list)
print(c)