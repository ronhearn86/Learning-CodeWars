'''
A child is playing with a ball on the nth floor of a tall building. The height of this floor, h,  knownis.

He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

His mother looks out of a window 1.5 meters from the ground.

How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?
'''
def bouncing_ball(h, bounce, window):
    if not (h > 0 and (bounce > 0 and bounce < 1) and window < h):
        return -1
    else:
        return 1 if h < window else 2 + bouncing_ball((h * bounce), bounce, window)
