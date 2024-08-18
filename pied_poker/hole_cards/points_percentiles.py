"""Calculate percentiles each distinct possible point values has. i.e. how many other hands is it better than."""

import points_system as hc

class HolePercentiles:
    ### Run all possible hands through points_system so that values are always up-to-date if the points system changes
    ALLOWED_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
    ALLOWED_SUITS = ['c', 'd', 'h', 's']  # clubs, diamonds, hearts, spades'

    def __init__(self):
        """Initialize attributes"""
        self.p1c1 = 0
        self.p1c2 = 0

    def calculate(self, p1c1, p1c2):
        """Initialize attributes"""
        self.p1c1 = p1c1
        self.p1c2 = p1c2


        # create all 52 possible card combinations
        ALLOWED_CARDS = [v + s for v in self.ALLOWED_VALUES for s in self.ALLOWED_SUITS]

        # create all 52*51 possible hand combinations
        # skipping filtering duplicate values for now, since every hand will be reversed once, it should not change the percentile rankings
        ALLOWED_HANDS = []
        POSSIBLE_VALUES = []
        for c1 in ALLOWED_CARDS:
            for c2 in ALLOWED_CARDS:
                if c2 == c1:
                    continue
                else:
                    ALLOWED_HANDS.append(c1+c2)
                    POSSIBLE_VALUES.append(hc.HolePoints().calculate(c1, c2))

        PERCENTILES = []
        for i in POSSIBLE_VALUES:
            temp_var = round(sum(j < i for j in POSSIBLE_VALUES)/len(ALLOWED_HANDS), 3)
            PERCENTILES.append(temp_var)

        # add hands, values, and percentiles to a dictionary
        hole_card_percentiles = {z[0]: list(z[1:]) for z in zip(ALLOWED_HANDS, POSSIBLE_VALUES, PERCENTILES)}

        # get percentile of current hole cards
        holecard_score = ('{:.1%}'.format(hole_card_percentiles[p1c1+p1c2][1]))

        return holecard_score
