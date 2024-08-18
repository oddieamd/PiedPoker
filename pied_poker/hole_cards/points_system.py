"""Calculate a ranking for hole cards based on a modified "Chen Formula"""

class HolePoints:
    ALLOWED_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
    ALLOWED_SUITS = ['c', 'd', 'h', 's']  # clubs, diamonds, hearts, spades'
    HIGHEST_CARD = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 10.0]
    IS_PAIR = 2 # Multiplier if hole cards are a pair
    IS_SUITED = 2 # Increase to hole card value if cards are suited
    CLOSENESS_FACTOR = -1 # Decrease to hole card value depending on closeness

    def __init__(self):
        """Initialize attributes"""
        self.p1c1 = 0
        self.p1c2 = 0

    def calculate(self, p1c1, p1c2):
        """Calculate hole card points and generate percentiles"""
        self.p1c1 = p1c1
        self.p1c2 = p1c2


        # Get highest card value
        # Get rank of hole cards
        rank_c1 = self.p1c1[:-1]
        rank_c2 = self.p1c2[:-1]

        # Get indexes of those ranks
        index_c1 = self.ALLOWED_VALUES.index(rank_c1)
        index_c2 = self.ALLOWED_VALUES.index(rank_c2)

        # Get highest card values of those indexes
        value_c1 = self.HIGHEST_CARD[index_c1]
        value_c2 = self.HIGHEST_CARD[index_c2]
        max_value = max(value_c1, value_c2)


        # Determine if cards are pairs
        if rank_c1 == rank_c2:
            pair_multiplier = 2
        else:
            pair_multiplier = 1


        # Determine if cards are suited
        if self.p1c1[-1] == self.p1c2[-1]:
            suited_addor = 2
        else:
            suited_addor = 0


        # Determine how close the 2 cards are
        # Get distance between indexes and allow Ace to be high or low
        if rank_c1 == 'a':
            closeness_score = min(abs(index_c1-index_c2)-1, index_c2)
        elif rank_c2 == 'a':
            closeness_score = min(abs(index_c1-index_c2)-1, index_c1)
        else:
            closeness_score = abs(index_c1-index_c2)-1
        closeness_score = max(min(closeness_score * self.CLOSENESS_FACTOR, 0), -5)


        # Calculate final hole card score
        holecard_score = (max_value * pair_multiplier) + suited_addor + closeness_score

        return holecard_score
