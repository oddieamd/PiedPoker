"""Run the main program"""

import pied_poker as pp
import numpy as np
import sys
sys.path.insert(1, 'C://Users//Alex//Documents//PiedPoker//pied_poker//hole_cards')
import points_percentiles as hc


def get_player_cards():
    p1c1 = input('Player hole card 1:')
    if p1c1 == 'exit':
        exit()
    p1c2 = input('Player hole card 2:')
    if p1c2 == 'exit':
        exit()
    p1 = pp.Player('Alex', pp.Card.of(p1c1, p1c2))
    print(p1)
    return p1c1, p1c2, p1


def get_flop():
    flop1 = input('Flop card 1:')
    if flop1 == 'exit':
        exit()
    flop2 = input('Flop card 2:')
    if flop2 == 'exit':
        exit()
    flop3 = input('Flop card 3:')
    if flop3 == 'exit':
        exit()
    # flop_play = input('Players still in hand:')
    # if flop_play == 'exit':
    #     exit()
    community_cards = pp.Card.of(flop1, flop2, flop3)
    return community_cards#, flop_play


def get_turn(community_cards):
    turn1 = input('Turn card:')
    if turn1 == 'exit':
        exit()
    # turn_play = input('Players still in hand:')
    # if turn_play == 'exit':
    #     exit()
    community_cards.append(pp.Card(turn1))
    return community_cards#, turn_play


def get_river(community_cards):
    river1 = input('River card:')
    if river1 == 'exit':
        exit()
    # river_play = input('Players still in hand:')
    # if river_play == 'exit':
    #     exit()
    community_cards.append(pp.Card(river1))
    return community_cards#, river_play


def run_simulation():
    p1c1, p1c2, p1 = get_player_cards()
    p2 = pp.Player('Opponent')
    holecard_score = hc.HolePercentiles().calculate(p1c1, p1c2)
    print(holecard_score)

    #Get Flop
    community_cards = get_flop()
    round_result = pp.PokerRound.PokerRoundResult([p1], community_cards)
    print(round_result)
    print(f'Current outs: {round_result.outs(p1)}')
    simulator = pp.PokerRound.PokerRoundSimulator(community_cards=community_cards, players=[p1, p2], total_players=3)#int(flop_play))
    num_simulations = 1000
    simulation_result = simulator.simulate(n=num_simulations, n_jobs=1, status_bar=False)
    print(simulation_result.probability_of(pp.Probability.PlayerWins(player = p1, includes_tie = False)))

    #Get Turn
    community_cards = get_turn(community_cards)
    round_result = pp.PokerRound.PokerRoundResult([p1], community_cards)
    print(round_result)
    print(f'Current outs: {round_result.outs(p1)}')
    simulator = pp.PokerRound.PokerRoundSimulator(community_cards=community_cards, players=[p1, p2], total_players=3)#int(turn_play))
    num_simulations = 1000
    simulation_result = simulator.simulate(n=num_simulations, n_jobs=1, status_bar=False)
    print(simulation_result.probability_of(pp.Probability.PlayerWins(player = p1, includes_tie = False)))

    #Get River
    community_cards = get_river(community_cards)
    round_result = pp.PokerRound.PokerRoundResult([p1], community_cards)
    print(round_result)
    simulator = pp.PokerRound.PokerRoundSimulator(community_cards=community_cards, players=[p1, p2], total_players=3)#int(river_play))
    num_simulations = 1000
    simulation_result = simulator.simulate(n=num_simulations, n_jobs=1, status_bar=False)
    print(simulation_result.probability_of(pp.Probability.PlayerWins(player = p1, includes_tie = False)))
    print(round_result.killer_cards(p1))


if __name__ == "__main__":
    run_simulation()
