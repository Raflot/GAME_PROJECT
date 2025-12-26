from action import *
from bot import *
from characters import *
from board import *

def main():
    board = board_init()
    print("Game started")

    #Initialisation
    Formulaire_de_setup() #sortie: Setup=[[player1;name;nation];[...];[map_seed;size;caracteristique_topographique]]
    gound_creation(nb_players,map_seed,size,list_nation_elements,caracteristique_topographique) #Affichage de la carte. nouvelle_map(y/n)

    #Player's turn


    #IA's turn