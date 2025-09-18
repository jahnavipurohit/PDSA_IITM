'''Write a recursive function constructword (word, wordList) which returns a list of lists in which 
all the ways word can be constructed from the elements of wordList. Return an empty list if 
there are no possible ways to construct word with wordList. Reusing elements of wordList is allowed.
Note: Write an efficient solution to pass all test cases.
Sample Input
constructword('apple', ['ap', 'pple', 'app', 'apl', 'appl', 'le', 'ple'])
Sample Output
[['ap', 'ple'], ['app', 'le']]'''

memo = {}
def constructWord(word, wordList):
    if word == '':
        return [[]]
    if word in memo.keys():
        return memo[word]
    totalwordlist = []
    for subword in wordList:
        if subword == word[:len(subword)]:
            subwordList = constructWord(word[len(subword):], wordList)
            totalwordlist.extend([[subword] + lst for lst in subwordList])
    memo[word] = totalwordlist
    return totalwordlist