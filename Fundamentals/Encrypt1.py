''' working on decrypt
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
''' their solution
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
        while n > 0:
            arry = arry3 + arry2
            arry2 = arry[0:c:]
            arry3 = arry[c::]
            print(arry)
            n = n -1

        arry2.reverse()
        arry3.reverse()
        count = 0
        for i in arry2:
            arry3.insert(count, i)
            count = count + 2

        arry3.reverse()
        final = " ".join(arry3)

        print(final)

decrypt(" Tah itse sits!", 3)

    if n <= 0:
        return encrypted_text
    textList = list(encrypted_text)
    length = len(textList)
    if length % 2 == 0:
        splitOn = length // 2
    else:
        splitOn = (length - 1) // 2
    first = textList[0:splitOn]
    second = textList[splitOn:length]

    resultList = [second[i // 2] if i % 2 == 0 else first[(i - 1) // 2] for i in range(0, length)]
    result = ''.join(resultList)
    return decrypt(result, n - 1)


def encrypt_once(text):
    e_str = ""
    o_str = ""

    for i in range(0, len(text)):
        if i % 2 != 0:  ## check if index is even
            e_str += text[i]  ## creat string with odd indices
        else:
            o_str += text[i]  ## creat string with even indices

    return e_str + o_str


def decrypt(text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))
    return text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text
'''


print(encrypt_once("This is a test!"))


def encrypt(text, n):  ## this function repeat encrypt_once n times

    s = [text]

    for i in range(1, n + 1):
        s.append(encrypt_once(s[i - 1]))

    return s[n]


print(encrypt("This is a test!", -1))


def decrypt_once(text):
    decry_one = ""
    decry_two = ""

    mid = int(len(text) / 2)  ##find mid index

    decry_one += text[0:mid]  ## breaks string into two strings
    decry_two += text[mid:]

    s = ""

    for i in range(0, mid):
        s += decry_two[i] + decry_one[i]  ## combine alternating even and odd indices

    if len(text) % 2 != 0:
        s += decry_two[mid]  ## if length is odd , add the last index of decry_two

    return s


def decrypt(text, n):
    s = [text]

    for i in range(1, n + 1):
        s.append(decrypt_once(s[i - 1]))

    return s[n]


print(decrypt("s eT ashi tist!", 2))