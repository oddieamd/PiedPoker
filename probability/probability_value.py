class ProbabilityValue:
    def __init__(self, event_count: int, given_count: int):
        probability = event_count / given_count
        self.event_count = event_count
        self.given_count = given_count
        self.probability = probability

    @property
    def __percent_str__(self):
        return f'{round(self.probability * 100, 2)}%'

    @property
    def __odds_str__(self):
        r = 1/self.probability
        if r >= 2:
            return f'1:{round(r - 1, 2)} odds'
        else:
            return f'{round(1/(r - 1), 2)}:1 odds'

    @property
    def __ratio_str__(self):
        return f'{self.event_count}/{self.given_count}'

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'{self.__percent_str__} == {self.__odds_str__} == ({self.__ratio_str__})'