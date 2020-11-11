from player import Player, Deck
from card import Card
class Board:
    turn_count = 0
    def __init__(self, players:[Player], turn_count: int, active_cards:[Card], history_cards:[Card]):
        #initialise our borad
        self.players = players
        self.turn_count = turn_count
        self.active_cards = active_cards
        self.history_cards = history_cards
    def start_game(self):
        #it start the game, fille the deck, shuffle, distribute and then play player by player
        cards = Deck().fill_deck()
        turn_count = self.turn_count
        active_cards = self.active_cards
        Deck.shuffle(cards)
        players = Deck().distribute(self.players, cards)
        finished = False
        while finished == False:
            for player in players:
                if player.name == "player1":
                    player.play(player.cards)
                else:
                    player.play(player.cards, players[0].history[len(players[0].history)-1])
                self.active_cards.append(player.history[self.turn_count])
                if players[len(players)-1].cards == []:
                    finished = True
            turn_count += 1
            print(turn_count)
            #print(active_cards[turn_count-1])
            self.history_cards.append(active_cards[turn_count])
            print(len(self.history_cards)*len(self.players))
    def __str__(self):
        return f"{self.players}, {self.turn_count}, {self.active_cards}, {self.history_cards}"