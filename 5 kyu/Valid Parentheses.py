def valid_parentheses(string):
    lst = [i for i in string if i in ['(',')']]
    try:
       if lst.count('(') == lst.count(')') and lst[0] == '(' and lst[-1] == ')':
          return True
    except:
        return True
    return False