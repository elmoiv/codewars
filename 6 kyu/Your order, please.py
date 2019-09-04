def order(txt):
	lst = []
	for i in range(1,10):
		for t in txt.split(' '):
			if str(i) in t:lst.insert(i-1, t)
	return ' '.join(lst)