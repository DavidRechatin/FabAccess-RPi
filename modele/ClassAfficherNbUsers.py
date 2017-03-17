#!/usr/bin/env python
# Fait par dany BITARD

from datetime import datetime

class NbUsers:

    # Notre méthode constructeur
    def _init_(self):
        self.usersDictionnary = {} #dictionnaire clef: valeur = badge: date
        self.usersLogTime = datetime.now() #date de l'entrer ou de la sortie

    # Notre méthode  qui genere et actualise la liste des utilisateurs present
    def GererUtilisateurListe(self,ID_badge):
        if self.usersDictionnary.has_key(ID_badge):  #si le badge est presente dans le dictionnaire
            del self.usersDictionnary[ID_badge]         #on l'enlève
        else:                                        #sinon
            self.usersDictionnary[ID_badge] = self.usersLogTime #on l'ajoute

    # Notre méthode  qui renvoie le nombre d'utilisateur
    def afficherNbUsers(self):
        return("Nombre de personne présente :" + len(liste_entrer))#retourne le nombre de personne présente

    # Notre méthode enleve les utilisateurs fantome
    def enleverGhostUsers(self):
        for cle,valeur in self.usersDictionnary.items():  #pour chaque combinaison du dictionnaire
            self.duree = datetime.now() - self.usersDictionnary.get[cle]  #la durée entre le temps actuelle et l'heure de badgage de l'utilisateur
            if self.duree.seconds > 43200:  #si cette durée est supérieur a 43200 secondes , soit 12heures
                del self.usersDictionnary[cle] #on le supprime de la liste
