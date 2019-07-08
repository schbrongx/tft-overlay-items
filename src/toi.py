#!/usr/bin/env python3
""" An item-overlay for Teamfight Tactics. """

import tkinter as tk
import os


PATH = os.path.dirname(os.path.abspath(__file__)) + "/.."
DIR_IMG_ITEMS = PATH + "/images/items"
print("DIR_IMG_ITEMS: %s" % DIR_IMG_ITEMS)


class Toi:
    """ A container class for the TOI window. """
    def __init__(self, item_images_path):
        self.items = {
            "b_f_sword": {
                "icon": "b_f_sword.png",
                "text": "text for b. f. sword",
            },
            "blade_of_the_ruined_king": {
                "icon": "blade_of_the_ruinged_king.png",
                "text": "text for blade of the ruined king",
            },
            "chain_vest": {
                "icon": "chain_vest.png",
                "text": "text for chain vest",
            },
        }

        self.categories = {
            "b_f_sword": {
                "mainitem": "b_f_sword",
                "subitems": [
                    "blade_of_the_ruined_king",
                    "chain_vest",
                ]
            },
            "chain_vest": {
                "mainitem": "chain_vest",
                "subitems": [
                    "b_f_sword",
                    "blade_of_the_ruined_king",
                ]
            },
        }
        # create tkinter window
        self.root = tk.Tk()

        # load the images
        self.item_images_path = item_images_path
        self.item_images = {}
        self.load_images()

        # create the buttons
        self.category_buttons = []
        self.create_buttons()

        # enter Tk mainloop
        self.mainloop()

    def load_images(self):
        """ load images for all items into a dict. """
        print("Loading images from %s" % self.item_images_path)
        _flist = [f for f in os.listdir(self.item_images_path)]
        for f in _flist:
            self.item_images[f] = tk.PhotoImage(file=self.item_images_path + "/" + f)
        print("Added %d images" % len(self.item_images))

    def create_buttons(self):
        """ create the buttons. """
        i = 0
        for c_name, c_content in self.categories.items():
            print("Category: %s" % c_name)
            print("  Main-Item: %s" % c_content["mainitem"])
            print("    Icon: %s" % self.items[c_content["mainitem"]]["icon"])
            print("    Text: %s" % self.items[c_content["mainitem"]]["text"])
            self.category_buttons.append(
                tk.Button(self.root,
                          text=self.items[c_content["mainitem"]]["text"],
                          command=lambda s=self.items[c_content["mainitem"]]["icon"]: print(s)
                         )
            )
            self.category_buttons[i].config(
                image=self.item_images[self.items[c_content["mainitem"]]["icon"]],
                width=64,
                height=64
            )
            self.category_buttons[i].grid(column=i+1, row=1, sticky="n")
            for i_name in c_content["subitems"]:
                print("  Sub-Item: %s" % i_name)
                print("    Icon: %s" % self.items[i_name]["icon"])
                print("    Text: %s" % self.items[i_name]["text"])
            i += 1

        #_icon = tk.PhotoImage(file=r"./images/items/b_f_sword.png")
        #_button = tk.Button(self.root,
        #                    image=_icon,
        #                    text="",
        #                    background="black",
        #                    command=quit)
        #_button.pack(side=tk.LEFT)

    def mainloop(self):
        """ enter the Tk mainloop. """
        self.root.mainloop()

if __name__ == "__main__":
    TOIWINDOW = Toi(DIR_IMG_ITEMS)
