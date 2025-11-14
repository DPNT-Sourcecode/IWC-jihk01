
class SumSolution:
    
    def compute(self, x, y):
        if not (0 <= x <= 100 or 0 <= y <= 100):
            return "incorrect argument x and y both need to be between 0 and 100"
            # raise ValueError('invalid value')
        return x + y
