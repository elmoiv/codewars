class Harshad:
    @staticmethod
    def is_valid(n):
        return n % sum(map(int, str(n))) == 0
    
    @staticmethod
    def get_next(n):
        n += 1
        return n if Harshad.is_valid(n) else Harshad.get_next(n)
    
    @staticmethod
    def get_series(c, s = 0):
        series = [Harshad.get_next(s)]
        while len(series) < c:
            series.append(Harshad.get_next(series[-1]))
        return series
