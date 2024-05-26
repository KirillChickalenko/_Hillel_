from typing import Self

import game_const


class Character:
    def __init__(self, name: str):
        self.name = name
        self.money = game_const.INITIAL_MONEY
        self.hp = game_const.BASE_HP
        self.stars = game_const.Stars.REGULAR_CITIZEN

    def __str__(self) -> str:
        return f"Name: {self.name}: health:{self.hp}"

    def hit_someone(self, other: Self):
        if other.is_alive:
            self.log_my_actions(f"I hit {other}")
            other.hp -= 8
        if not other.is_alive:
            other.hp = 0
            self.stars = game_const.Stars.WANTED_LOW
            self.log_my_actions(f"I deal with {other}")

    __repr__ = __str__

    @property
    def is_alive(self) -> bool:
        return self.is_bigger_zero(self.hp)

    def log_my_actions(self, message: str) -> None:
        with open(f"{self.name}_{id(self)}.txt", "a") as logfile:
            logfile.write(f"{message}\n")

    @classmethod
    def get_max_wanted_rate(cls):
        return game_const.Stars.WANTED_LOW

    @staticmethod
    def is_bigger_zero(number: int | float) -> bool:
        return number > 0


def create_character(name) -> Character:
    return Character(name)


pedro = Character("Pedro")
npc = Character("NPC")

print(pedro.is_alive)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)


pedro.get_max_wanted_rate()
print([pedro])
