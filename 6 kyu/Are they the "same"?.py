def comp(a1, a2):
    return False if any(i is None for i in [a1, a2]) else len(a1) == len(a2) and sorted([i*i for i in a1 if i*i in a2]) == sorted(a2)
    
# This solution was way more better than mine
# I admit I was careless when I submitted my solution
# without revision or even applying DRY

# IvanKochura
def comp(a, b):
    try:
        return sorted(i*i for i in a) == sorted(b)
    except:
        return False
        
# Unnamed
def comp(xs, ys):
    if xs is None or ys is None:
        return False
    return sorted(x * x for x in xs) == sorted(ys)
