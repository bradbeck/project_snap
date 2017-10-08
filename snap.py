#!/usr/bin/env python3
'''Snap! game implementation'''


import random
from cards import Card, Deck, Player
random.seed(42)


class Game(object):
    '''Game class'''
    def __init__(self, player1, player2):
        self._player1 = player1
        self._player1.hand = []
        self._player1.discard = []
        self._player1.played = []
        self._player2 = player2
        self._player2.hand = []
        self._player2.discard = []
        self._player2.played = []
        self._winner = None
        deck = Deck()
        deck.shuffle()
        while not deck.is_empty():
            player1.draw_card(deck)
            player2.draw_card(deck)

    @property
    def winner(self):
        return self._winner

    def play_round(self):
        card1 = self.do_play(self._player1)
        card2 = self.do_play(self._player2)
        if not card1 or not card2:
            if not card1:
                self._winner = self._player2
            if not card2:
                self._winner = self._player1
        elif card1 == card2:
            sum_rank = self._player1.skill + self._player2.skill
            player1_rank = self._player1.skill / sum_rank
            player2_rank = self._player2.skill / sum_rank
            if random.random() < player1_rank:
                self._player1.win_table(self._player2)
            else:
                self._player2.win_table(self._player1)

    def do_play(self, player):
        if player.is_empty_hand():
            if player.is_empty_discard():
                if player.is_empty_played():
                    return None
                player.discard_played()
            player.pick_discard()
        return player.play_card()

def play_game(player1, player2):
    '''Game main loop'''
    game = Game(player1, player2)
    rounds = 0
    while rounds <= 9999:
        rounds += 1
        game.play_round()
        if game.winner:
            return [game.winner.name, rounds]

    return ['Tie', rounds]

def main():
    '''Main function'''
    player1 = Player("Alice", 5)
    player2 = Player("Bob", 5)
    print('{} ({}) and {} ({}) are going to play 100 games!'.format(player1.name, player1.skill, player2.name, player2.skill))
    print('{:^10}{:^10}{:^10}'.format('Game', 'Winner', 'Rounds'))
    winners = {'Alice': 0, 'Tie': 0, 'Bob': 0}
    for i in range(1, 101):
        winner, rounds = play_game(player1, player2)
        winners[winner] += 1
        print('{:^10}{:^10}{:^10}'.format(i, winner, rounds))
    print(winners)

if __name__ == "__main__":
    main()
