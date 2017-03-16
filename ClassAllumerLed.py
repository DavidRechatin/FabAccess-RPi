#!bin/bash/python3.5
# coding: utf-8

import RPi.GPIO as GPIO  # Librairie de gestion des entrées/sorties du GPIOs
import time  # Manipulation du temps
import sys  # Permet d'interagir avec le système

#Définition de notre class
class AllumerLed:

    # Notre méthode constructeur
    def __init__(self,reponseDroitAPI):
        rouge = () #port GPIO à définir
        orange = () #port GPIO à définir
        vert  = () #port GPIO à définir
        allumer = GPIO.HIGH  #simplification pour transmission du courant
        eteindre = GPIO.LOW  #simplification pour arret du courant
        GPIO.cleanup()  #Nettoyage des GPIOs
        GPIO.setmode(GPIO.BCM)  #Choix du mode de numérotation des ports : identique aux inscriptions sur le Cobbler
        GPIO.setup(rouge, GPIO.OUT) #Configuration des ports en mode sortie
        GPIO.setup(orange, GPIO.OUT) #Configuration des ports en mode sortie
        GPIO.setup(vert, GPIO.OUT) #Configuration des ports en mode sortie
        self.droit = reponseDroitAPI #la réponse de l'API sur les droits.

    # Allumage de la led en fonction du droit de l'utilisateur
    def allumerLedRGB(self):
        if self.droit == 0: #Si aucun droit
            GPIO.output(rouge, allumer) #on allume la led rouge.
            time.sleep (2000) #attente de deux seconde.
            GPIO.output(rouge, eteindre) #on eteint la led rouge.
        elif self.droit == 1: #Si droit avec concierge
            GPIO.output(orange, allumer) #on allume la led orange.
            time.sleep(2000) #attente de deux seconde.
            GPIO.output(orange, eteindre) #on eteint la led orange.
        elif self.droit == 2: #Si droit total
            GPIO.output(vert, allumer) #on allume la led verte.
            time.sleep(2000) #attente de deux seconde.
            GPIO.output(vert, eteindre) #on eteint la led verte.
