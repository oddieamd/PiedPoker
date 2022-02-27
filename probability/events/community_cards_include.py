from typing import List

from card_internals.card import Card
from probability.base_poker_event import BasePokerEvent
from round.round_result import RoundResult


class CommunityCardsInclude(BasePokerEvent):
    def __init__(self, target_cards: List[Card]):
        """
        Checks whether ALL of target_cards are included in the community cards
        :param target_cards: The target cards
        :type target_cards: List[Card]
        """
        super().__init__()
        self.target_cards = set(target_cards)

    def is_event(self, round_result: RoundResult) -> bool:
        return len(self.target_cards.intersection(set(round_result.community_cards))) == len(set(self.target_cards))