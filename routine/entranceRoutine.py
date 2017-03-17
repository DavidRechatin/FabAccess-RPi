#!/usr/bin/env python
# Fait par christophe JUNIER

from ClassAfficherNbUsers import *
from ClassRecupererIdBadge import *
from ClassJouerSon import *

personnePresente = NbUsers()          #initialisation du ombre d'utilisateurs
presenceBadge = Badge()               #initialisation de l'attente d'un badge
sonAJouer = jouerSon("bonjour.wav")   #initialisation du son à lancer
routine = 1                           #initialisation de la routine
while routine:                                                            #tant que vrai
    personnePresente.enleverGhostUsers()                                          #on enleve les utilisateurs fantomes
    personnePresente.afficherNbUsers()                                            #on affiche le nombre d'utilisateurs
    if presenceBadge.renvoieIdBadge() !== null :                                  #si un badge est lu
        badgeActuel = presenceBadge.renvoieIdBadge()                              #on affecte le numero de badge à la variable
        personnePresente.GererUtilisateurListe(badgeActuel)                       #on ajoute ou on retire le badge de la liste des personnes présentes
        sonAJouer.lancerLecture()                                                 #on dit bonjour
