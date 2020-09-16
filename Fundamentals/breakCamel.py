def solution(s):
    arry = list(s)
    arry2 = []
    arry3 = []
    print(arry)
    count = 0

    for i in range(len(arry)):
        for x in arry:
            if x is not x.lower():
                arry2.append(x)
                arry3.append(i)
                print(arry3)



solution('breakCamelCamp')
