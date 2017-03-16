#!bin/bash/python3.5
# coding: utf-8
#Fait par Jimmy FRAGNE

import RPi.GPIO as GPIO

class GestionEquipement:

    # Notre méthode constructeur
    def _init_(self, autorisation):
        self.allumer = GPIO.HIGH  #simplification pour transmission du courant
        self.eteindre = GPIO.LOW  #simplification pour arret du courant
        self.alimentation = () #port GPIO à définir
        self.acces = autorisation #le niveau d'autorisation de l'utilisateur.
        GPIO.cleanup()  #Nettoyage des GPIOs
        GPIO.setmode(GPIO.BCM)  #Choix du mode de numérotation des ports : identique aux inscriptions sur le Cobbler
        GPIO.setup(self.alimentation, GPIO.OUT) #Configuration des ports en mode sortie



    # Notre méthode  qui allume un equipement
    def allumerEquipement(self):
        if self.acces == 2:   #si les droit d'accès sont de niveau 2
            GPIO.output(self.alimentation, self.allumer) #on allimente le relais

    # Notre méthode qui eteind un equipement
    def eteindreEquipement(self):
        if self.acces == 2: #si les droit d'accès sont de niveau 2
            GPIO.output(self.alimentation, self.eteindre) #on eteind le relais
