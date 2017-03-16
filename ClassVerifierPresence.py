#Fait par Jimmy FRAGNE

#!bin/bash/python3.5
# coding: utf-8

import requests
import json

class Presence:

    # Notre méthode constructeur
    def _init_(self, ID_user):
        self.presence = requests.post(urlserveur + "/user/isPresent/"+ID_user) #requete sur l'API pour recuperer le json sur la présence de l'utilisateur
        self.presence = json.JSONDecoder().decode(self.presence) #on decode le json

    # Notre méthode renvoyant si il y présence ou non d'un utilisateur
    def retourPresence(self):
        if self.presence["present"]:  #si l'utilisateur est present
            return true
        else:                         #sinon
            return false
