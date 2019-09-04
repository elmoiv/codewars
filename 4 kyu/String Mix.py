def mix(s1, s2):
	dat, lst = [{}, []]
	if s1 == s2:
		return ''
	for i in s1 + s2:
		if i.isalpha() and i.islower() and (s1.count(i) > 1 or s2.count(i) > 1):
			dat[i] = [s1.count(i), s2.count(i)]
	for e in list(dat.keys()):
		if dat[e][0] != dat[e][1]:
			lst += [str(dat[e].index(max(dat[e])) + 1) + ':' + e * max(dat[e])]
		else:
			lst += ['=:' + e * max(dat[e])]
	return '/'.join(sorted(lst, key=lambda x:(-len(x), x[0], x[2])))