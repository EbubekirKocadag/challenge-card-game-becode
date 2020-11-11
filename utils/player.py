from card import Card
import random

class Player:
    #We initialise Player
    def __init__(self, name:str, cards:[Card] , turn_count: int,number_of_cards: int, history: [Card]= []):
        self.name = name
        self.cards = cards
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history
    def play(self, cards, player1_played = ""):
        #From a list of cards we choose randomly one card and pop it
        if self.name != "player1":
            color = player1_played
            #verify if there is the same color in the deck
            list_of_card = [list_of_card for list_of_card in cards if color[0] in list_of_card]
            if len(list_of_card) != 0:
                #if there is try to find out the index
                indexOfCard = [[y,cards.index(y)] for y in cards if y in list_of_card]
                #play the first one, i could try to find out how to compare and play the biggest but that's enough for me
                i = indexOfCard[0][1]
            else:
                #if there is not a same color then play anything else
                i = random.randint(0, (len(cards)-1))
        else:
            print(self.cards)
            #if it's player one who playes, then ask with card he want to play, if he gives a int out af the range then ask again
            i = int(input("which card?: "))
            if i >= len(self.cards):
                i = int(input("Out of range, choose between 0 and {}: ".format(len(self.cards)-1)))
        card: Card = cards[i]
        self.cards.pop(i)
        self.history.append(card)
        self.turn_count +=1
        print(f"{self.name} {self.turn_count} played: {card[0]} {card[1]}")
        return card
        
    def __srt__(self):
        return (f"{self.cards}, {self.turn_count}, {self.number_of_cards}, {self.history}")
class Deck(Card):
    def __init__(self,color = "", icon = ["♥", "♦", "♣", "♠"], value: [str] = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']):
        super().__init__(color,icon,value)
    def fill_deck(self):
    #methode to create the deck
        cards = []
        for i in self.icon:
            for j in self.value:
                cards.append([i, j])
        return cards
    def shuffle(self):
    #methode to shuffle
        random.shuffle(self)
    def distribute(self, players, card):
    #methode to distrite when giving a list of players
        j = 0
        i = 52%(len(players))
        while j <52-i:
            for player in players:
                player.cards.append(card[j])
                j+=1
        return players
    def __srt__(self):
        return(f"{self.color} {self.icon} {self.value}")