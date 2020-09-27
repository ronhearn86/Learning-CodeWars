def find_it(seq):
    # Initialize result
    res = 0

    # Traverse the array
    for element in seq:
        # XOR with the result
        res = res ^ element
        print(res)
    print(res)

find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])

''' 
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
'''