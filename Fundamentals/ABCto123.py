def alphabet_position(text):
    text= text.lower()
    abclist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    newdict = {}
    nums = 0
    arry = []
    strlist = [i for i in text]

    for x in abclist:
        nums += 1
        newdict.setdefault(x, str(nums))

    for i in strlist:
        if i in newdict:
            arry.append(newdict.get(i))

    strng = ' '.join(arry)
    return strng


alphabet_position("The sunset sets at twelve o' clock.")
