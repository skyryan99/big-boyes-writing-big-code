'''@file ironcladCards
   @author Cameron Cooke
   @author Schuyler Ryan
   A database with all Ironclad cards stored as Card objects in a dictionary'''

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

bash = Card("Bash", "Ironclad", 68, 2, [ 'Strength', 'Strike'], [4, 5], 10, 5, 0, 83)
defend = Card("Defend", "Ironclad", 10, 1, ['Block'], [3], 0, 0, 0, 20)
strike = Card("Strike", "Ironclad", 15, 1,['Strength','Strike'], [7, 2], 10, 2, 0, 25)
anger = Card("Anger", "Ironclad", 20, 0,['Strength'], [3], 10, 7, 0, 25)
armaments = Card("Armaments", "Ironclad", 50, 1, all, [6, 2, 3, 2, 5, 7, 8], 3, 3, 0, 110)
bodySlam = Card("Body Slam", "Ironclad", 60, 1, bl, [10], 10, 5, 0, 75)
clash = Card("Clash", "Ironclad", 32, 0, ['Strike', 'Strength'], [6.5, 2], 11, 7, 0, 37)


