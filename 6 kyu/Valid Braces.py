def validBraces(s):
    for n, i in enumerate(s):
        if i in '{[(' and n != len(s) - 1:
            if s[n+1] == {'{':'}', '[':']', '(':')'}[i]:
                return validBraces(s.replace(i+s[n + 1], ''))
    return not s
