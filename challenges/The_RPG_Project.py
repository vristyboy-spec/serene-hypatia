class Fighter:
    def __init__(self,name ,health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage, {target.name} has {target.health} Health Left")

player = Fighter("Hero", 100, 20)
enemy = Fighter("Goblin", 50, 10)

player.attack(enemy)