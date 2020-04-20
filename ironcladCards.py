'''@file ironcladCards
   @author Cameron Cooke
   @author Schuyler Ryan
   A database with all Ironclad cards stored as Card objects in a dictionary'''
"""and \
                self.cardClass == other.cardClass and\
                self.baseScore == other.baseScore and\
                self.cost == other.cost and\
                self.synergyType == other.synergyType and\
                self.synergyStrength == other.synergyStrength and\
                self.offenseRating == other.offenseRating and\
                self.energyGain == other.energyGain and\
                self.upgrade == other.upgrade and\
                self.repeatability == repeatability and\
                self.upgradeScore == other.upgradeScore:"""

from card import *
ste = 'Strength'
sti = 'Strike'
ex = 'Exhaust'
bl = 'Block'
x = 'X-times'
hp = 'Minus HP'
st = 'Status'
I = 'Ironclad'
all = ['Block' 'Exhaust', 'Minus HP', 'Status', 'Strength', 'Strike', 'X-times']

bash = Card("Bash", "Ironclad", [75, 68, 60], 2, ['Strength', 'Strike'], [4, 5], 10, 0, 5, 83)
defend = Card("Defend", "Ironclad", [10, 5, 2], 1, ['Block'], [3], 0, 0, 0, 20)
strike = Card("Strike", "Ironclad", [15, 10, 5], 1,['Strength','Strike'], [2, 7], 10, 0, 2, 25)
anger = Card("Anger", "Ironclad", [20, 18, 15], 0,['Strength'], [3], 10, 7, 0, 25)
armaments = Card("Armaments", "Ironclad", [50, 52, 55], 1, all, [6, 2, 3, 2, 5, 7, 8], 3, 0, 3, 110)
bodySlam = Card("Body Slam", "Ironclad", [60, 70, 80], 1, bl, [10], 10, 5, 0, 75)
clash = Card("Clash", "Ironclad", [32, 22, 15], 0, [ste, sti], [2, 6.5], 11, 0, 7, 37)
cleave = Card("Cleave", "Ironclad", [40, 32, 20], 1, ['Strength'], [2], 10, 0, 3, 45)
clothesline = Card("Clothesline", "Ironclad", [65, 70, 73], 2, [ste], [2], 7, 0, 3, 75)
flex = Card("Flex", "Ironclad", [35, 38, 42], 0, [ste, x], [9, 7], 10, 0, 5, 50)
havoc = Card("Havoc", "Ironclad", [35, 50, 65], 1, [ex], [10], 5, 0, 4, 50)
headbutt = Card("Headbutt", "Ironclad", [65, 72, 80], 1, [all], [5, 4, 3, 7, 5, 3, 2], 8, 0, 7, 68)
heavyBlade = Card("Heavy Blade", I, [30, 50, 70], 2, [ste], [10], 10, 0, 5, 50)
ironWave = Card("Iron Wave", I, [30, 25, 20], 1, [ste, bl], [2, 4], 5, 0, 3, 35)
perfectedStrike = Card("Perfected Strike", I, [45, 52, 55], [ste, sti], [3, 10], 10, 0, 6, 55)
pommelStrike = Card("Pommel Strike", I, [65, 70, 75], [ste, sti], [3, 7], 8, 0, 6, 85)

