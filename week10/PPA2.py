'''You are given a string 8 8182...8.. where n is the length of string 8, and s, is its ith character. 
The prefix of the string s of length l(1 <= l < n) is string $182..81.
Write a function PrefixMatch(s) that accepts a string s and returns a list of all unique substrings 
of s[1:] that matches with any prefix of s.
Hint:- Use concept of KMP algorithm to write an efficient solution.
Sample Input 
ababa #s
Output
['a', 'ab', 'aba'] #substrings that matched with prefix of s
Explanation
All possible unique substring of s[1:] or baba are b, a, ba, bab, baba, ab, and aba but 
only a, ab, aba matched with prefix of s'''

def PrefixMatch(s):
    n = len(s)
    lps = [0] * n   # prefix function (KMP)

    # Build lps array
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = lps[j - 1]
        if s[i] == s[j]:
            j += 1
            lps[i] = j

    result = set()
    sub = s[1:]   # only substrings from s[1:]

    # For every prefix length
    for l in range(1, n):
        prefix = s[:l]
        if prefix in sub:  # occurs in s[1:]
            result.add(prefix)

    return result


s = input()
print(sorted(PrefixMatch(s)))