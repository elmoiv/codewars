def get_issuer(n):
    dct = {'AMEX':[['34','37'],[15]],
           'VISA':[['4'],[13, 16]],
           'Discover':[['6011'],[16]],
           'Mastercard':[['51','52','53','54','55'],[16]]}
    for k, v in dct.items():
        if len(str(n)) in v[1]:
            for i in v[0]:
                if str(n)[:len(i)] == i:
                    return k
    return 'Unknown'
