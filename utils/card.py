import random
class Symbol:
#We create attributes color and icon
    def __init__(self, color: str = "", icon: [str] = ["♥", "♦", "♣", "♠"]):
        self.color = color
        self.icon = icon
    def __srt__(self):
        return (f"{self.color} , {self.icon}")

class Card(Symbol):
# We create card class inheriting from symbole
    def __init__(self, color = "", icon = ["♥", "♦", "♣", "♠"], value: [str] = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']):
        super().__init__(color,icon)
        self.value = value
    def __srt__(self):
        return (f"{self.value}")