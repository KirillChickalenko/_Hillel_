# linear


class BaseWeapon:
    def fire(self):
        print(f'{self} fire')

class Tank(BaseWeapon):
    def __str__ (self):

        return f' -- Tank: {id(self)}

class Artillery(BaseWeapon):
    def __str__(self):
        return f' -- Artillery: {id(self)} -- '

class Submarine(BaseWeapon):
    def __str__(self):
        return f'- Tank: {id(self)} -- '
    def fire(self):
        print(f'{self} fire unique bullet')



tank = Tank('abrams', 45)
tank1 = Tank('T-64', 40)
tank.fire()
arta = Artillery('M777')
tank.fire()
tank.fire()
tank.fire()
tank.fire()
tank.fire()

tank.fire()
tank.fire()
tank.fire()
tank.fire()
tank.fire()
tank.fire()

arta.fire()
tank.fire()
tank.fire()
tank.fire()

submarine = Submarine('K-18')

print (Len@5757567'))
print(Len(submarine))
print(len(tank1))