# FYI
# Trooper - The infantry of the Star Wars Films
# Jedi - A member of the mystical knightly order in the Star Wars films, trained to guard peace 
#        and justice in the Universe.  Examples: Yoda, Obi Wan Kenobi, Luke Skywalker, etc.
# Sith - The opposite of a Jedi.  Trained to destroy peace and rule the Universe through strength and brutality.
#        Examples: Darth Vader, Darth Maul, The Emperor, etc.

from random import randint

class Trooper:
    game_name = "Star Wars Dojo Duel"
    everyone = []
    def __init__(self,name,attack):
        self.name = name
        self.weapon = "Blaster"
        self.attack = attack
        self.health = 100
        Trooper.everyone.append(self)

    def fight(self,foe):
        rand_attack = randint(0,self.attack)
        foe.health -= rand_attack
        if(foe.health > 0):
            print(f"{self.name} damages {foe.name} with a {self.weapon} by {rand_attack}")
            print(f"{foe.name} Health: {foe.health}")
        else:
            print(f"{self.name} obliterated {foe.name} with an attack of {rand_attack} using their {self.weapon}")

        return self

    def heal(self): 
        rand_health = randint(1,10)
        future_health = self.health + rand_health
        if Trooper.can_heal(future_health):
            self.health += rand_health
            print(f"{self.name} healed by {rand_health} | Current Health: {self.health}")
        else:
            self.health = 100
            print(f"{self.name} health can't go above 100 | Current Health: {self.health}")
    
        return self

    @staticmethod
    def can_heal(future_health):
        if future_health > 100:
            return False
        else:
            return True

    @classmethod
    def all_fighters(cls):
        print("Fighters:")
        for fighter in Trooper.everyone:
            print(fighter.name)


# rex = Trooper("Rex",50)
# cody = Trooper("Cody",40)
# helmetTrooper = Trooper("Helmet",30)
# rex.fight(cody)
# cody.fight(rex)
# cody.heal()
# rex.heal()
# Trooper.all_fighters()
    

class Jedi(Trooper):
    def __init__(self,name,attack):
        super().__init__(name,attack)
        self.health = 200
        self.weapon = "Light Saber"
        self.force_push_attack = 50
        self.trooper = Trooper("123654",25)

    def force_push(self,foe):
        foe.health -= self.force_push_attack
        if(foe.health > 0):
            print(f"{self.name} damages {foe.name} with a Force Push by {self.force_push_attack}")
            print(f"{foe.name} Health: {foe.health}")
        else:
            print(f"{self.name} obliterated {foe.name} with a Force Push")

    def heal(self): 
        rand_health = randint(10,20)
        future_health = self.health + rand_health
        if Jedi.can_heal(future_health):
            self.health += rand_health
            print(f"{self.name} healed by {rand_health} | Current Health: {self.health}")
        else:
            self.health = 200
            print(f"{self.name} health can't go above 200 | Current Health: {self.health}")

        return self

    @staticmethod
    def can_heal(future_health):
        if future_health > 200:
            return False
        else:
            return True        
    
rex = Trooper("Rex",50)
cody = Trooper("Cody",40)
obi = Jedi("Obi Wan", 75)
yoda = Jedi("Yoda", 100) 
print(obi.name)
print(yoda.name)
print(obi.trooper.name)
print(obi.health)
yoda.force_push(obi)
obi.heal()


class Sith(Jedi):
    def __init__(self,name,attack):
        super().__init__(name,attack)
        self.force_lightning_attack = 70

    def force_lightning(self,foe):
        foe.health -= self.force_lightning_attack
        if(foe.health > 0):
            print(f"{self.name} damages {foe.name} with Force Lightning by {self.force_lightning_attack}")
            print(f"{foe.name} Health: {foe.health}")
        else:
            print(f"{self.name} obliterated {foe.name} with Force Lightning") 

        return self 

obi = Jedi("Obi Wan", 75)
vader = Sith("Darth Vader",75)

print(vader.name)
print(vader.attack)
print(vader.health)
print(vader.weapon)
vader.heal()
vader.fight(vader)
vader.force_push(vader)

vader.force_lightning(obi)
#obi.force_lightning(vader)




# obi = Jedi("Obi Wan", 75)
# rex = Trooper("Rex", 10)
# rex.fight(obi)
# obi.force_push(rex)
# rex.force_push(obi)
# obi.heal()


# print(obi.trooper.name)
# print(obi.trooper.health)
# print(obi.name)


# rex = Trooper("Rex",50)
# cody = Trooper("Cody",12)

# Trooper.all_fighters()


# rex.fight(cody)
# cody.heal()

# print(f"Welcome to {Trooper.game_name}")
# print(f"{rex.name} vs {cody.name}")
# print(f"{rex.name}: Attack - {rex.attack} | Health: {rex.health}")
# print(f"{cody.name}: Attack - {cody.attack} | Health: {cody.health}")




# rex = {
#     "name":"Rex",
#     "attack":15,
#     "weapon":"Blaster",
#     "health":100
# }
# cody = {
#     "name":"Cody",
#     "attack":15,
#     "weapon":"Blaster",
#     "health":100
# }

# print(rex["name"])
# print(rex["attack"])
# print(rex["weapon"])
# print(rex["health"])
# print(cody["name"])
# print(cody["attack"])
# print(cody["weapon"])
# print(cody["health"])