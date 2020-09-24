def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        time = g * 3600 / (v2 - v1)
        h = time / 3600
        mn = (time % 3600) / 60
        s = time % 60
        time_required = [int(h), int(mn), int(s)]
    return time_required