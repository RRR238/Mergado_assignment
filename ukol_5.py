class Warrior:
    def __init__(self,name,maximum_health):
        self.name = name
        self.maximum_health = maximum_health

    @property
    def is_alive(self):
        if self.maximum_health > 0:
            is_alive = True
        else:
            is_alive = False
        return is_alive

    def __str__(self):
        return 'Warrior(name = ' + self.name + ' ,maximum_health = ' + str(self.maximum_health) + ' ,is_alive = ' + str(self.is_alive) + ')'

    def __add__(self, other):
        if self.maximum_health > 0 and other.maximum_health > 0:
            return Warrior(self.name + " " + other.name,self.maximum_health + other.maximum_health)
        else:
            return None

    def __sub__(self, other):
        if self.maximum_health > 0 and other.maximum_health > 0:
            self.maximum_health -= 1
            other.maximum_health -= 1

        return None
