def solution(s):
    arry = list(s)
    count_array = []
    count = 0
    for x in arry:
        if x.isupper():
            count_array.append(count)
        count += 1
    count_array.sort(reverse=True)
    for i in count_array:
        arry.insert(i, " ")

    listToStr = ''.join(arry)
    return listToStr
