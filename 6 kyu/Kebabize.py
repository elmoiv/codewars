from re import sub
kebabize=lambda s:sub('(?<!^)(?=[A-Z])','-',sub('\\d','',s)).lower()
