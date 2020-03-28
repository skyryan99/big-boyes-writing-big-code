'''@file card.py
   @author Cameron Cooke
   @author Schuyler Ryan'''

class Card:
    '''Class to implement card objects representing cards in Slay the Spire'''

    def __init__(self, cardName, cardClass, baseScore, cost, synergyType, synergyStrength, offenseRating):
        '''a list of attributes to add to later if we have additional considerations
        @param cardName - Name of the card
        @param cardClass - What class the card belongs to (Ironclad, Defect, Silent, Watcher, Neutral)
        @oaram baseScore - The score given to a card if it was pure card goodness was the only 
            thing to consider
        @param cost - How much energy the card costs
        @param synergyType - What synergy group the card belongs to
        @param synergyStrength - How heavily the card plays into the given synergy type
        @param offenseRating - How offensive vs. defensive the card is from 0 being very defensive -> 10
            being very offensive'''
        self.cardName = cardName
        self.cardClass = cardClass
        self.baseScore = baseScore
        self.cost = cost
        self.synergyType = synergyType
        self.synergyStrength = synergyStrength
        self.offenseRating = offenseRating

    def __eq__(self, other):
        '''Overriding equals because fuck object locations'''
        if self.cardName == other.cardName and \
                self.cardClass == other.cardClass and\
                self.baseScore == other.baseScore and\
                self.cost == other.cost and\
                self.synergyType == other.synergyType and\
                self.synergyStrength == other.synergyStrength and\
                self.offenseRating == other.offenseRating
            return True
        return False

    def __str__(self):
        '''Overriding print statement because FFFFUUUUUCK hex'''
        return(self.cardName + ':\n    ' + self.cardClass + '\n    ' + self.baseScore + '\n    ' + self.cost
                + '\n    ' + self.synergyType + '\n    ' + self.syergyStrength + '\n    ' self.offenseRating)

    def format(self):
        '''in case you forget what order to put the cards in'''
        print("1. card name, 2. card class, 3. base score, 4. cost, 
                5. synergy type, 6. synergy strength, 7. offense rating(0 ->10)")
        return
