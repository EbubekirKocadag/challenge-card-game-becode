import sys, os
sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)])
from utils.card import Card
from utils.player import Player,Deck
from utils.game import Board
import random

if __name__ == "__main__":

    card:[Card] = []
    print(card)
    player1 = Player("player1", card, 0, [], [])
    player2 = Player("player2", card, 0, [], [])
    player3 = Player("player3", card, 0, [], [])
    player4 = Player("player4", card, 0, [], [])
    player5 = Player("player5", card, 0, [], [])
    Board([player1, player2, player3, player4, player5], 0, [], []).start_game()