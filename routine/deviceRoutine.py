#!/usr/bin/env python
# Fait par christophe JUNIER

from ClassRecupererIdBadge import *
from ClassInfosEquipement import *
from ClassRecupererPermission import *
from ClassVerifierPresence import *
from ClassAllumerLed import *
from ClassAlimentationEquipement import *

infosEquipement = InfosEquipement()                        #initialisation des infos d'un equipement
idEquipement = infosEquipement.renvoieIdEquipement()       #on recupere l'id de l'equipement'
pathServeur = infosEquipement.renvoieUrlServeur()          #on recupere l'url du serveur'
presenceBadge = Badge()                                    #initialisation de l'attente d'un badge
state = 0                                                  #switch pour allumer ou eteindre une machine


routine = 1                                                               #initialisation de la routine
while routine:                                                            #tant que vrai
    if presenceBadge.renvoieIdBadge() !== null :                              #si un badge est lu
        badgeActuel = presenceBadge.renvoieIdBadge()                              #on affecte le numero de badge à la variable
        permissionUtilisateur = Permission(badgeActuel,idEquipement,pathServeur)  #on initialise la recuperation des permissions de l'utilisateur
        idUser = permissionUtilisateur.retourUserId()                             #on recupere l'id de l utilisateur
        permissionLevel = permissionUtilisateur.retourAutorisation()              #on recupere son niveau d'autorisation
        presenceUtilisateur = Presence(idUser)                                    #on initialise la recuperation de la presence de l'utilisateur
        if presenceUtilisateur.retourPresence():                                  #Si l'utilisateur c'est bien badger
            allumageLED = AllumerLed(permissionLevel)                             #on initialise l'allumage de la led
            allumageLED.allumerLedRGB()                                           #on allume la led correspondant à ses permission
            fonctionnementEquipement = GestionEquipement(permissionLevel)         #on initialise la gestion des equipements
            if state == 0:                                                        #si etat 0
                fonctionnementEquipement.allumerEquipement()                       #on allume l'equipement
                state = 1                                                          #on passe a l'etat 1
            elif state == 1:                                                      #si etat 1
                fonctionnementEquipement.eteindreEquipement()                      #on eteind l'equipement
                state = 0                                                           #on passe a l'etat 0
