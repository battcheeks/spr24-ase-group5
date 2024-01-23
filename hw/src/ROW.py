import math
class ROW:
    k=1
    def __init__(self, cells):
        self.cells = cells
    
    #likes()
    def likes(self, datas):
        n, nHypotheses = 0, 0
        for k, data in datas.items():
            n += len(data['rows'])
            nHypotheses += 1
        for k, data in datas.items():
            tmp = self.like(data, n, nHypotheses)
            if most is None or tmp > most:
                most, out = tmp, k
        return out, most
    
    #like()
    def like(self,data, n, nHypotheses):
        prior = (len(data['rows']) + the.k) / (n + the.k * nHypotheses)
        out = math.log(prior)
        for _, col in data['cols']['x'].items():
            v = self.cells[col['at']]
            if v != "?":
                inc = col.like(v, prior)
                out += math.log(inc)

        return math.exp(1) ** out