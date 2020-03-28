# big-boyes-writing-big-code
for big boyes who write big code

-Goal: To write a deck building program to choose the best card out of available options in Slay the Spire. This will take into account deck cost, card synergies, defensive vs offensive, relics, deck size, etc.

-Steps:
  1. Create database of ironclad cards
  2. Create database of relics
  3. Card objects:
    Card name,
    Card cost,
    Synergy group,
    Card type,
    Card rating,
    Synergy rating,
    Energy gain
    Upgraded bool,
    Upgrade Score
  4. Relic objects:
    Relic name,
    Synergy group,
    Relic rating,
    Synergy rating,
  5. Adjust weights every card selection/after combat
  6. Form equation to give values of card choices
  7. Make opencv/overlay to automatically update
 
-Future:
  1. Create pathing program
  2. Create combat program
  3. Create money management program
  4. Combine programs into sentient being that plays Slay the Spire so we don't have to
