import arcade

import SetupObjects
from Enumerators import Veggies
from InventoryObject import InventoryObject

INVENTORY_SCALING = 2  # Konstant for størrelse


class SpritePosition:
    def __init__(self, PosX, PosY):
        self.PosX = PosX
        self.PosY = PosY


class Inventory:
    def __init__(self):
        self.item_list = None
        self.held_item = None
        self.held_item_original_position = None
        pass

    def setup(self):
        self.held_item = []
        self.held_item_original_position = []
        self.item_list = arcade.SpriteList()
        testCarrot = SetupObjects.create_carrot()
        testCarrot.position = (200,200)
        self.item_list.append(testCarrot)

    def pick_up_item(self, item: arcade.Sprite):
        self.item_list.remove(item)
        self.item_list.append(item)

    def item_interaction_mouse(self, x, y, button):
        print(x)
        print(y)
        items = arcade.get_sprites_at_point((x, y), self.item_list)
        if len(items) > 0:
            primary_item = items[-1]

            # All other cases, grab the face-up card we are clicking on
            self.held_item = [primary_item]
            # Save the position
            self.held_item_original_position = [self.held_item[0].position]
            # Put on top in drawing order
            self.pick_up_item(self.held_item[0])

    def item_interaction_mouse_moving(self, dx, dy):
        for item in self.held_item:
            item.center_x += dx
            item.center_y += dy

    def item_interaction_mouse_release(self, x, y):
        if len(self.held_item) == 0:
            return
        self.held_item=[]