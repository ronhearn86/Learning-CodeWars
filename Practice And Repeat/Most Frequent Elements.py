'''
Find the most frequent element or elements in the list.

Example:

find_most_frequent([1, 1, 2, 3]) == set([1])
find_most_frequent([1, 1, 2, 2, 3]) == set([1, 2])
find_most_frequent([1, 1, '2', '2', 3]) == set([1, '2'])
FUNDAMENTALSALGORITHMS
'''


def find_most_frequent(l):
    # Write your code here.
    newlist = {}
    keepcount = 0
    for i in l:
        if i in newlist:
            newlist[i] += 1
        elif i not in newlist:
            newlist[i] = 1
        if newlist[i] >= keepcount:
            keepcount = newlist[i]
    freq_num = set()
    for x in l:
        if keepcount == newlist[x]:
            freq_num.add(x)
    return freq_num

    return set()