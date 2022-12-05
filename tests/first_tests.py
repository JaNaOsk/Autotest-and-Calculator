# import pytest
from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calc= Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) ==4
        assert self.calc.multiply(self, 4, 4) ==16

    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self,2,2)==5

    def test_division(self):
        assert self.calc.division(self,2,2)==1
        assert self.calc.division(self, 4, 2) == 2

    def test_subtraction(self):
        assert self.calc.subtraction(self,2,2)==0
        assert self.calc.subtraction(self, 6, 2) == 4
        assert self.calc.subtraction(self, 6, -2) == 8
        assert self.calc.subtraction(self, 0, 2) == -2

    def test_adding(self):
        assert self.calc.adding(self,2,2)==4
        assert self.calc.adding(self, 6, 2) == 8

    def test_adding_1(self):
        assert self.calc.adding(self,-3,-3)==-6
        assert self.calc.adding(self, -30, 3) == -27


