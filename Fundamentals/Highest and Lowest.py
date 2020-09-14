def high_and_low(numbers):

    new_list = numbers.rsplit()
    intlist = []
    for i in new_list:
        intlist.append(float(i))

    intlist.sort()
    print(intlist)
    max = int(intlist[-1])
    min = int(intlist[0])
    newstr = str(max) +' '+ str(min)
    return newstr
print(high_and_low('988 2876 2974 2712 1060 2784 1651 1999 1908 112 -84 516 203 164 228 2789 1775 1289 2798 563 1757 1704'))
