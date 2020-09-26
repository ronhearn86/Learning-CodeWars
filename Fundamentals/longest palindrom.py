def longest_palindrome (s):
    length =0
    for x in range( 1,len(s)+1):
        for pos in range(0, len(s) - x+ 1):
            word = s[pos:pos + x]
            if word == word[::-1]:
                length = x
    return length