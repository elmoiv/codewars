findSquares = lambda x,y: sum((max(x, y) - n) * (min(x, y) - n) for n in range(min(x, y)))
