#!/usr/bin/env python3
""" An item-overlay for Teamfight Tactics. """

import tkinter as tk

class Toi:
    """ A container class for the TOI window. """
    def __init__(self):
        self.items = {
            "b_f_sword": {
                "icon": "images/items/b_f_sword.png",
                "text": "text for b. f. sword",
            },
            "blade_of_the_ruined_king": {
                "icon": "images/items/blade_of_the_ruinged_king.png",
                "text": "text for blade of the ruined king",
            },
            "chained_vest": {
                "icon": "images/items/chained_vest.png",
                "text": "text for chaied vest",
            },
        }

        self.categories = {
            "b_f_sword": {
                "mainitem": "b_f_sword",
                "subitems": [
                    "blade_of_the_ruined_king",
                    "chained_vest",
                ]
            },
            "chained_vest": {
                "mainitem": "chained_vest",
                "subitems": [
                    "b_f_sword",
                    "blade_of_the_ruined_king",
                ]
            },
        }
        # create tkinter window
        self.root = tk.Tk()
        # create the buttons
        self.create_buttons()
        # enter Tk mainloop
        self.mainloop()

    def create_buttons(self):
        """ create the buttons. """
        for _mainitem, _subitems in self.categories.items():
            print("%s" % _mainitem)
            for k, v in _subitems.items():
                print(k, v)

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
    TOIWINDOW = Toi()
