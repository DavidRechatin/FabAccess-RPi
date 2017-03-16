#
#  Projet FabAccess
#  Réalisé par DTA - BTS Simone Weil
#
#  Fichier "ClassInfosEquipement.py"
#  Réalisé par Clément Ballet DTA
#
#  La classe "infos équipement" remplit les fonctions suivantes :
#  - ouvrir et lire le fichier JSON qui contient les informations des équipements
#  - récupérer l'ID de l'équipement en cours d'utilisation
#  - récupérer l'URL du serveur en liaison avec l'équipement
#

#!bin/bash/python3.5
# coding: utf-8

import json

class InfosEquipement:

    #methode constructeur
    def __init__(self):
        self.config_json = open('FabAccess-RPi/config.json', 'r') # On ouvre le json
        self.file = json.load(self.config_json)  # On lit le JSON

    #methode qui renvoie l'id de l'equipement present dans le fichier de config
    def renvoieIdEquipement(self):
        if type(self.file["IdEquipement"]) == int: # Vérif si l'ID est bien un entier
            return self.file["IdEquipement"] # On récupère l'ID de l'équipement utilisé

    #methode qui renvoie l'URL du serveur presente dans le fichier de config
    def renvoieUrlServeur(self):
        if type(self.file["UrlServeur"]) == str: # Vérif si l'URL est bien une chaîne de caractère
            return self.file["UrlServeur"] # On récupère l'URL du serveur
