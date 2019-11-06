def solution(string, markers):
    res, run = '', 1
    for char in string:
        if char in markers:
            run = 0
            res = res.strip(' ')
        if char == '\n' or run:
            run = 1
            res += char
    return res
