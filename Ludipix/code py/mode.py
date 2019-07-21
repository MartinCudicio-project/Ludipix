import RPi.GPIO as GPIO
import time

pinsolo=3
pinapprentissage=12
apprentissage=true
solo =true

def soloduo():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinsolo, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #définition du port d'entrée

    while true:
        entree=GPIO.input(pinsolo)
        if (entree):
            if (solo):
                solo=false
            else :
                solo= true
            return solo
            time.sleep(1)


def pratiqueapprentissage():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinapprentissage,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    while true :
        entree=GPIO.input(pianpprentissage)
        if (entree==true):
            if (apprentissage):
                apprentissage=false
            else:
                apprentissage=true
            return apprentissage
        time.sleep(1)

        

                
