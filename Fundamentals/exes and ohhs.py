def xo(s):
    list1=[]
    list1[:0]= s
    ex = 'xX'
    oh = 'oO'
    cnt1 = 0
    cnt2 = 0
    for i in list1:
        if i in ex:
            cnt1 = cnt1 + 1
        elif i in oh:
            cnt2 = cnt2 + 1

    if cnt1 == cnt2:
        return True
    else:
        return False
xo('xoxoxox')