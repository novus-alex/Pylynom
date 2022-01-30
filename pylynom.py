class Polynom:
    def __init__(self, X_index, Coeffs) -> None:
        self.X = self.getX(X_index)
        self.c = Coeffs

    @staticmethod
    def getX(index) -> list:
        return [1*_ for _ in index]

    def __getitem__(self, key) -> list:
        if key > 1:
            raise MaxKey(f"Max key of Polynom object if 1, not '{key}'")
        else:
            return self.c if key == 0 else self.X

    def __add__(self, p):
        self.C, self.x = [], []
        for i in range(max(len(self.X), len(p[1]))):
            self.C.append(self.c[i] + p[0][i])
            self.x.append(self.X[i] + p[1][i])
            for i in range(len(self.x)):
                if self.x[i] > 1:
                    self.x[i] = 1
        
        return Polynom(self.x, self.C)

class MaxKey(Exception):
    pass

p = Polynom([1, 0, 1], [2, 0, 6])
p2 = Polynom([1, 0, 1], [2, 0, 9])

a = p + p2

print(a[1])