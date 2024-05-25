from typing import Self

import Uber_const
class Car:
    def __init__(self, name: str, model: str, cost_money: int, year: str, length_of_the_ride: int):
        self.name = name
        self.model = model
        self.year = year
        self.cost = cost_money
        self.length = length_of_the_ride
    @property
    def which_clas(self) -> str:
        if self.cost > 10_000_000:
            return Uber_const.Cost.ELITE
        if self.cost>=2_000_000 and self.cost<=10_000_000:
           return Uber_const.Cost.MIDDLE
        if self.cost < 2_000_000:
           return Uber_const.Cost.ECONOM
        if self.cost >=100_000_000_000:
           return Uber_const.Cost.LUX
    def __str__(self) -> str:
        return (f'Car: {self.name}: model:{self.model} year: {self.year} cost: {self.cost - self.length*10}')

auto = Car('Mersedes', 'sedan', 100, 2008, 2)
print(auto)
