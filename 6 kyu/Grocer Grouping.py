def group_groceries(groceries):
    d = {i:[] for i in ['fruit', 'meat', 'other', 'vegetable']}
    for x in groceries.split(','):
        a, b = x.split('_')
        d[a].append(b) if a in d else d['other'].append(b)
    return '\n'.join(f'{y}:{",".join(sorted(d[y]))}' for y in d)
