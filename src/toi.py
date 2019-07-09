#!/usr/bin/env python3
""" An item-overlay for Teamfight Tactics. """

import os
import tkinter as tk
import configparser


PATH = os.path.dirname(os.path.abspath(__file__)) + "/.."
DIR_IMG_ITEMS = PATH + "/images/items"
CONFIG = PATH + "/toi.conf"
print("DIR_IMG_ITEMS: %s" % DIR_IMG_ITEMS)
print("CONFIG: %s" % CONFIG)


class Toi:
    """ A container class for the TOI window. """
    def __init__(self, item_images_path, config_path):
        # load config from config_path
        self.config = configparser.ConfigParser(interpolation=None)
        self.config.read(config_path)

        # load all items from config [GLOBAL]itemlist
        self.items = {}
        for _i in self.config.get("GLOBAL", "itemlist", fallback=None).split(", "):
            self.items[_i] = {
                "name": self.config.get(_i, "name", fallback="missing name"),
                "icon": self.config.get(_i, "icon", fallback="missing_image.png"),
                "text": self.config.get(_i, "text", fallback="missing text")
            }

        self.categories = {}
        for _c in self.config.get("GLOBAL", "categorylist", fallback=None).split(", "):
            self.categories[_c] = {
                "mainitem": self.config.get(_c, "mainitem", fallback="missing main item"),
                "subitems": self.config.get(_c, "subitems", fallback="missing subitems").split(", ")
            }

        # create tkinter window
        self.root = tk.Tk()

        # load the images
        self.item_images_path = item_images_path
        self.item_images = {}
        self.load_images()

        # create the buttons
        self.buttons = []
        self.create_buttons()

        # enter Tk mainloop
        self.mainloop()

    def load_images(self):
        """ load images for all items into a dict. """
        print("Loading images from %s" % self.item_images_path)
        _flist = [f for f in os.listdir(self.item_images_path)]
        for _f in _flist:
            self.item_images[_f] = tk.PhotoImage(file=self.item_images_path + "/" + _f)
        print("Added %d images" % len(self.item_images))

    def create_buttons(self):
        """ create the buttons. """
        i = 0
        for c_key, c_val in self.categories.items():
            #c_name = c_val["mainitem"]
            c_icon = self.items[c_val["mainitem"]]["icon"]
            c_text = self.items[c_val["mainitem"]]["text"]
            self.buttons.append(tk.Button(self.root, text=c_text))
            # pylint: disable=cell-var-from-loop
            self.buttons[i].config(
                image=self.item_images[c_icon],
                width=64,
                height=64,
                command=lambda s=c_icon: print(s)
            )
            # pylint: enable=cell-var-from-loop
            self.buttons[i].grid(column=i+1, row=1, sticky="n")
            for i_val in c_val["subitems"]:
                s_name = i_val
                s_icon = self.items[i_val]["icon"]
                s_text = self.items[i_val]["text"]
                #print("  Sub-Item: %s, Icon: %s, Text: %s" % (s_name, s_icon, s_text))
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
    TOIWINDOW = Toi(DIR_IMG_ITEMS, CONFIG)
