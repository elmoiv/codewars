def sum_arrays(x,y):
    e=eval(f"{str(x)[1:-1].lstrip('0').replace(', ','')or 0}+{str(y)[1:-1].lstrip('0').replace(', ','')or 0}")
    l=list(map(int,str(abs(e))))
    return [l,[-1*l[0]]+l[1:]][e<0]if x+y!=[]else[]
