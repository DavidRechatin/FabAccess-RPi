#!/usr/bin/env python
# Fait par dany BITARD

from datetime import datetime

class afficherNbUsers:

    def _init_(self):
        self.usersDictionnary = {}
        self.usersLogTime = datetime.now()

    def GererUtilisateurListe(self,ID_badge):
        if self.usersDictionnary.has_key(ID_badge):
            del self.usersDictionnary[ID_badge]
        else:
            self.usersDictionnary[ID_badge] = self.usersLogTime

    def afficherNbUsers(self):
        return("Nombre de personne présente :" + len(liste_entrer))#retourne le nombre de personne présente


    def enleverGhostUsers(self):
        for cle,valeur in self.usersDictionnary.items():
            self.duree = self.usersLogTime() - self.usersDictionnary.get[cle]
            if self.duree.seconds > 43200:
                del self.usersDictionnary[cle]
