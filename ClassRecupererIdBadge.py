#!bin/bash/python3.5
# coding: utf-8

import os
import pwd


class Badge:
    # Notre méthode constructeur
    def __init__(self):
        self.ID_badge = pwd.getpwuid( os.getuid() ) #conversion du signal en id de badge

    # Notre méthode renvoyant le numero de badge
    def return_badge(self):
        return self.ID_badge #renvoie le numero de badge
