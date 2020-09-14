'''
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
def increment_string(strng):
    return strng

'''
def increment_string(strng):
    numx = '012345678'
    numy = '9'
    if strng[-1] in numx:
        x = strng[-1]
        print(x)
        numz = int(x) +1
        tempstr = strng[:-1]
        tempstr = tempstr + str(numz)
        return tempstr
    elif strng[-1] in numy:
        if strng[-3] in numx and strng[-2] in numy:
            x = strng[-3]
            x2 = strng[-2]
            num1 = x + x2
            numz = int(num1) + 1
            tempstr = strng[:-1]
            tempstr2 = tempstr[:-1]
            tempstr3 = tempstr2[:-1]
            tempstr4 = tempstr3 + str(numz) + '0'
            return tempstr4
        elif strng[-2] in numx:
            x = strng[-2]
            numz = int(x) + 1
            tempstr = strng[:-1]
            tempstr2 = tempstr[:-1]
            tempstr3 = tempstr2 + str(numz) + '0'
            print(tempstr3)
            return tempstr3
        elif strng[-2] in numy:
            x = strng[-1]
            print(x)
            x2 = strng[-2]
            print(x2)
            x3 = x + x2
            x4 = int(x3)+1
            tempstr = strng[:-1]
            tempstr2 = tempstr[:-1]
            tempstr3 = tempstr2 + str(x4)
            return tempstr3
    else:
        tempstr = strng + '1'
        print(tempstr)
        return tempstr
increment_string('989989j89j')
