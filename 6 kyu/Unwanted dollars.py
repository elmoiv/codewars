def money_value(s):
    try:
        return float(s.replace("$", "").replace(" ", ""))
    except:
        return 0
