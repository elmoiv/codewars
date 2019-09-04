def time_convert(num):
    return '%02d:%02d' % (num // 60, num % 60) if num > 0 else '00:00'
