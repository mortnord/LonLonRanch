import arcade

from Inventory import Inventory
from MainCharacters import MainCharacters



class Malon(MainCharacters):
    SPRITE_SCALING_PLAYER = 2

    def __init__(self):

        # start Liv
        self.health = 12
        # Lager Inventory til Link
        self.inventory_character = Inventory()
        # Kobler sprite .pngen til koden
        self.player_sprite = arcade.Sprite("Sprites/Malon.png", self.SPRITE_SCALING_PLAYER)
        # startposisjon
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 50
        #Flag for å sjekke om inventory skal tegnes eller ikke
        self.show_inventory = False

        self.PLAYER_MOVEMENT_SPEED = self.PLAYER_MOVEMENT_SPEED * 4  # Konstant med fart i bevegelse