'''
def encrypt(text, n):
    newtext = text
    arry = []
    if n > 0:
        n = n - 1
        for i in newtext:
            arry.append(i)

        arry2 = arry[::2]
        arry = arry[1::2]
        x = arry + arry2

        while n > 0:
            n = n-1
            arry2 = x[::2]
            arry = x[1::2]
            x = arry + arry2

        z = ''.join(x)
        return z
    else:
        return text

encrypt("This is a test!", 0)
'''

def decrypt(encrypted_text, n):
    newtext = encrypted_text
    arry = []

    if n > 0:
        n = n - 1
        for i in newtext:
            arry.append(i)

        x = len(arry)
        c = x / 2
        c = int(c)
        arry2 = arry[0:c:]
        arry3 = arry[c::]
        print(arry2)
        print(arry3)
        while in range(x):
            x = x -1



decrypt("hskt svr neetn!Ti aai eyitrsig", 1)


