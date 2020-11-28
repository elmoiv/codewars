def solution(r,d=dict(zip('IVXLCDM',[1,5,10,50,100,500,1000]))):
    return sum(d[i]*[1,-1][n<len(r)-1and d[r[n+1]]>d[i]]for n,i in enumerate(r))
