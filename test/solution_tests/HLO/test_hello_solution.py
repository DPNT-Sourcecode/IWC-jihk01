from solutions.HLO.hello_solution import HelloSolution

class TestSum():
    def test_sum(self):
        assert HelloSolution().hello('test') == "Hello, World!"

