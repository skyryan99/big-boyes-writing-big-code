

class relic:
        def __init__(self, rarity, synergy, energy):
            self.rarity = rarity
            self.synergy = synergy
            self.energy = energy

        def __str__(self):
            return 'Relic is: {self.rarity}, works with this {self.synergy}, adds {self.energy} energy.'
