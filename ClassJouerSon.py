#!/usr/bin/env python
# Fait par Jean BONNARD
import subprocess
import pygame

class jouerSon:
    # Notre méthode constructeur
    def __init__(self,wavToPlay):
		self.sound = wavToPlay #affectation du nom du fichier sonore a la variable local.

    # Notre méthode lancant le fichier audio
    def lancerLecture(self):
        pygame.mixer.init() #on initialise le lecteur audio
		pygame.mixer.Sound(self.sound).play() # on lance la lecture du fichier audio
