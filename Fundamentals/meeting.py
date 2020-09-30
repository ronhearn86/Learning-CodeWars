
def meeting(s):
    list = s.split(';')
    for i in range(len(list)):
        last = list[i].split(':')
        list[i]= ("("+last[1]+", "+last[0]+")").upper()
    list.sort()
    return ''.join(list)
