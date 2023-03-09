import random
import pandas as pd
from tkinter import *
from tkinter import ttk
import json
import requests
import urllib.request
from PIL import Image  
import os
import sys

#Setting directory
os.chdir(os.path.dirname(sys.argv[0]))

class Game():
    def __init__(self):
        self.deck: list = []
        self.board: list = []
        self.hand: list = []
        self.window: Tk()

    def Get_hand(self):
        for x in range(7):
            self.Draw()

    def Draw(self):
        self.hand.append(self.deck.pop()) 

    def Go(self):
        x = 2


def Run_game():

    def on_click():
        print(Current_game.deck)

    def Get_Deck(file):
        df = open("Decks/"+file).read().splitlines()
        deck = []
        for line in df:
            # Goldfish add sidebord after an empty line. As we do not want sideboard, the for loop breaks after empty line.
            if line != "":
                for i in range(0,int(line[0])):
                    deck.append(line[2:]) # As there is max 4 copies name of the card starts at positon 2
            else:
                break
        #Saving it as a list to pass it to convertet
        return(deck)

    def Shuffle():
        random.shuffle(Current_game.deck)

    def Get_images():
        for cards in Current_game.deck:
            if not os.path.isfile("Card_images/"+cards+".png"):
                try:
                    request = requests.get("https://api.scryfall.com/cards/search?order=set&q=name="+cards+"+unique:prints") 
                    urllib.request.urlretrieve(request.json()["data"][0]['image_uris']['normal'],"Card_images/"+cards+'.png')
                except KeyError:
                    request = requests.get("https://api.scryfall.com/cards/search?order=set&q=name="+cards+"+unique:prints") 
                    urllib.request.urlretrieve(request.json()["data"][0]["card_faces"][0]['image_uris']['normal'],"Card_images/"+cards+'.png')
        print("done")
    
    Deck = Get_Deck("Deck.txt")
    Current_game = Game()
    Current_game.deck = Deck
    Current_game.window = Tk()

    frm = ttk.Frame(Current_game.window, padding=10)
    frm.grid()
    ttk.Label(frm, text="test").grid(column=1, row=1)
    Deck_name= Entry(frm).grid(column=1, row=3)
    ttk.Button(frm, text="Get images", command=Get_images).grid(column=2, row=2)
    
    ttk.Button(frm, text="Quit", command=Current_game.window.destroy).grid(column=3, row=3)

    Current_game.window.mainloop()

















if __name__ == "__main__":
    
    Run_game()





