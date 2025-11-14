
class SumSolution:
    
    def compute(self, x, y):
        if not (0 <= x <= 100 or 0 <= y <= 100):
            raise ValueError('invalid value')
        return x + y

