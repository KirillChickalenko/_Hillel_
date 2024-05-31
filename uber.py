import uber_const


class Car:
    def __init__(
        self, name: str, model: str, cost_money: int, year: str, length_of_the_ride: int
    ):
        self.name = name
        self.model = model
        self.year = year
        self.cost = cost_money
        self.length = length_of_the_ride

    @property
    def which_clas(self) -> str:
        if self.cost > 10_000_000:
            return uber_const.Cost.ELITE
        if self.cost >= 2_000_000 and self.cost <= 10_000_000:
            return uber_const.Cost.MIDDLE
        if self.cost < 2_000_000:
            return uber_const.Cost.ECONOM
        if self.cost >= 100_000_000_000:
            return uber_const.Cost.LUX

    def depreciate_cost(self, km: int):
        self.cost -= km * 10

    def __str__(self) -> str:
        return (
            f"Car: {self.name}: model:{self.model} year: {self.year} cost: {self.cost}"
        )


auto = Car("Mersedes", "sedan", 100, 2008, 2)
auto.depreciate_cost(auto.length)
print(auto)
