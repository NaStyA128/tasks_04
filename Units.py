import random
import math


START_RECHARGE = 100
END_RECHARGE = 2000


class Unit(object):
    health = None
    recharge = None

    def __init__(self):
        self.health = 100
        self.recharge = random.randint(START_RECHARGE, END_RECHARGE)

    def do_attack(self):
        pass

    # def take_damage(self):
        # pass

    @property
    def get_recharge(self):
        return self.recharge

    @property
    def get_health(self):
        return self.health


class Soldiers(Unit):

    experience = 0

    def __init__(self):
        super().__init__()

    @property
    def do_attack(self):
        a = 0.5 * (1 + self.get_health/100) * \
            random.randint(50+self.experience, 100)/100
        return a

    # @property
    # def take_damage(self, v):
        # self.health = self.get_health - v
        # a = 0.05 + self.experience/100
        # return a


class Vechiles(Unit):

    operators = []

    def __init__(self):
        super().__init__()
        op = random.randint(1, 3)
        i = 0
        self.operators = [Soldiers for _ in range(1, op)]
        sum_health = 0
        for j in self.operators:
            sum_health += j.get_health

        self.health = int(sum_health/len(self.operators))
        self.recharge = random.randint(1000, END_RECHARGE)

    def do_attack(self):
        sr_geo = 1
        for i in self.operators:
            sr_geo *= i.do_attack
        sr_geo = math.pow(sr_geo, (1/len(self.operators)))
        a = 0.5 * (1 + self.health/100) * sr_geo
        print(a)
        return a

    # def take_damage(self):
        # a = 0.1 + sum(self.operators/100)
        # return a


class Squard(object):

    units = None

    def __init__(self, solders, vechiles):
        self.units = [Soldiers() for _ in range(1, solders)] + [Vechiles() for _ in range(1, vechiles)]

    def get_power(self):
        sum_at = 0
        for i in self.units:
            sum_at += i.do_attack
        print(sum_at)

# s = Squard(2, 2)
# s.get_power()
