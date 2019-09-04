def delete_nth(order,n):
    dic, _order, x = [{}, order.copy(), 0]
    for i in order:
        if not i in dic.keys():dic[i] = [1, x]
        else:
            if dic[i][0] == n:del _order[x - (len(order)-len(_order))]
            else:dic[i] = [dic[i][0]+1, x]
        x += 1
    return _order