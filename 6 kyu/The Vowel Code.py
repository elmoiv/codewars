encode=lambda s,n=1:s.translate(str.maketrans(*['aeiou','12345'][::n]))
decode=lambda s:encode(s,-1)
