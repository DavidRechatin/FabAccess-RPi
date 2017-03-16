#
#  Projet FabAccess
#  Réalisé par DTA - BTS Simone Weil
#
#  Fichier "permission.py"
#  Réalisé par Clément Ballet DTA
#
#  La classe permission remplit les fonctions suivantes :
#  - récupérer un fichier JSON de l'API FabAccess contenant les infos d'un badge quand celui-ci est
#  lu par un lecteur RFID
#  - renvoie le niveau de permission du badge (0 = aucune permission, 1 = doit être accompagné pour
#  utiliser la machine, 2 = permission d'utiliser la machine).
#

#!bin/bash/python3.5
# coding: utf-8

import requests
import json


class Permission:

    # Notre méthode constructeur
    def __init__(self,ID_badge,id):
        self.permission = requests.post(urlserveur + "/getAuth/"+id+"/"+ID_badge) #on interroge l'API avec le tagRFID recuperer precedemment.
        self.permission = json.JSONDecoder().decode(self.permission)   #on decode le json envoyer par l'API


    # Notre méthode renvoie l'autorisation
    def retourAutorisation(self):
        if type(self.permission['acces']) == int and self.permission['access'] < 3:  #si l'autorisation est d'un format correct
            return self.permission['access'] #on renvoie l'autorisation

    # Notre méthode pour recuperer l'id d'un utilisateur
    def retourUserId(self):
        if type(self.permission['user']) == int:  #si l'id utilisateur est un entier
            return self.permission['user'] #on renvoie l'id utilisateur
