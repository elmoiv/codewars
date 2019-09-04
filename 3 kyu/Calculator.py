class Calculator(object):
    def evaluate(self, string):
        self.all = string.split()
        for sn in ['/', '*', '-', '+'] * 2:
            self.operate(sn)
        return int(self.all[0][:-2]) if self.all[0][-2:] == '.0' else float(self.all[0])
    def operate(self, sign):
        clc = {'/':op.truediv, '*':op.mul, '+':op.add, '-':op.sub}
        i = 0
        while i + 2 < len(self.all):
            if self.all[i + 1] == sign:
                res = clc[sign](float(self.all[i]), float(self.all[i + 2]))
                del self.all[i:i + 3]
                self.all.insert(i, str(res))
            i += 1
        return all
