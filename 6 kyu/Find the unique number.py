def find_uniq(a, inf=float('inf')):
    return eval('{0} if a.count({0})==1else {1}'.format(*set(a)))
