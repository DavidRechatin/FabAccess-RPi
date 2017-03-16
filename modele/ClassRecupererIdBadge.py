#!bin/bash/python3.5
# coding: utf-8
# Fait par Jimmy FRAGNE

import os
import pwd
import rfidreader

class Badge:
    
    # Notre méthode constructeur
    def __init__(self):
        self.ID_badge = pwd.getpwuid( os.getuid() ) #conversion du signal en id de badge

    # Notre méthode renvoyant le numero de badge
    def renvoieIdBadge(self):
        return self.ID_badge #renvoie le numero de badge
