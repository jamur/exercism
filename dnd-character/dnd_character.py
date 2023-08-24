import random

ABILITIES = ("strength", "dexterity", "constitution",
             "intelligence", "wisdom", "charisma")

class Character:

    def __init__(self):
        for ability in ABILITIES:
            setattr(self, ability, self.ability())
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability():
        dices = [random.randint(1,6) for _ in range(4)]
        dices.remove(min(dices))
        return sum(dices)
    

def modifier(constitution):
    return (constitution - 10) // 2



#character = Character()
