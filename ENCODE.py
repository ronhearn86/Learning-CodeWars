def encode(st):
    strng = []
    for i in st:
        strng.append(i)

    count = 0
    for i in strng:
        count += 1
        if i == 'a':
            strng.insert(count, '1')
            strng.pop(count -1)

        elif i == 'e':
            strng.insert(count, '2')
            strng.pop(count -1)

        elif i == 'i':
            strng.insert(count, '3')
            strng.pop(count -1)

        elif i == 'o':
            strng.insert(count, '4')
            strng.pop(count -1)

        elif i == 'u':
            strng.insert(count, '5')
            strng.pop(count -1)

    stngs = ''.join(strng)
    return stngs

encode('for i and you e i o u')
def decode(st):
    strng = []
    for i in st:
        strng.append(i)

    count = 0
    for i in strng:
        count += 1
        if i == '1':
            strng.insert(count, 'a')
            strng.pop(count -1)

        elif i == '2':
            strng.insert(count, 'e')
            strng.pop(count -1)

        elif i == '3':
            strng.insert(count, 'i')
            strng.pop(count -1)

        elif i == '4':
            strng.insert(count, 'o')
            strng.pop(count -1)

        elif i == '5':
            strng.insert(count, 'u')
            strng.pop(count -1)

    stngs = ''.join(strng)
    return stngs

'''  
def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)
    
def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)
    
    
CIPHER = ("aeiou", "12345")

def encode(st):
    return st.translate(str.maketrans(CIPHER[0], CIPHER[1]))
    
def decode(st):
    return  st.translate(str.maketrans(CIPHER[1], CIPHER[0]))
'''