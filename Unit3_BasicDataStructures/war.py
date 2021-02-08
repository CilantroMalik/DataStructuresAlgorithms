"""
--- War: The Card Game ---
Implementation of the classic card game War using basic data structures. In War, each turn players put down one card
from their hand; whichever player's card is higher than their opponent's gets to take both cards. If there is a tie,
a "war" occurs where each player puts down three additional face-down cards and then a fourth face-up, and the score of
that card decides who takes the entire pool. The first person to empty their opponent's hand wins the game.
"""

# --- imports ---
import random
import os
from DoublyLinkedList import DoublyLinkedList as DLL
from efficientQueue import Queue


# --- helper functions ---
def display_card(value):
    value -= 1  # get it in the range 0-51 so it is easier to work with
    # find the suit by figuring out which segment of 13 cards the value is in
    suit = ""
    if value // 13 == 0:
        suit = "Spades"
    elif value // 13 == 1:
        suit = "Hearts"
    elif value // 13 == 2:
        suit = "Diamonds"
    elif value // 13 == 3:
        suit = "Clubs"
    # then the value is much simpler from there using modulo within each segment of 13
    val = (value % 13)+2  # add 2 so it aligns with the real card values
    if val == 11:
        val = "Jack"
    if val == 12:
        val = "Queen"
    if val == 13:
        val = "King"
    if val == 14:
        val = "Ace"
    return f"{val}/{suit}"


# --- game setup ---

# create deck: insert the numbers 1 to 52 (representing cards) in random positions, repeat for the number of decks
numDecks = int(input("How many decks (1-6) would you like to play with? "))
deck = DLL()
for i in range(numDecks):
    for j in range(1, 53):
        deck.insert(random.randint(0, deck.size()), j)

# add the cards to each player's hand (represented with a queue) in alternating order
playerDeck = Queue()
aiDeck = Queue()
counter = 0  # keep track of alternation
current = deck.getHead()
while current is not None:
    if counter % 2 == 0:
        playerDeck.enqueue(current.getData())
    else:
        aiDeck.enqueue(current.getData())
    current = current.getNext()
    counter += 1

# TODO begin main game loop
