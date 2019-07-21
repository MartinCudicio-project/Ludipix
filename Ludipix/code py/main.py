from time import *  #on importe la bibliothèque pour les timers
from RPI import GPIO # On import la récupération des signaux des boutons
from mode import *  # on importe les fonctions de la méthode mode.py qu'on a crée
from random import randrange
from audio import *
from rfid import *



if(soloduo()):   #Si soloduo = true on lance le mode solo
    LancementInstructions(0)
    compteur = 0
    ID = randrange(0,25)          #choix aléatoire d'une lettre
        LancementLettre(ID)
        CodeBadge = LectureBadge()
        while ((CodeBadge != CodeJ1[ID])||(CodeBadge != CodeJ2)) :     #trouver dans la bibliothéque RFID le code
            compteur++
            if (compteur %5 == 0) :
                LancementInstructions(6)
                    LancementIndice(ID)
            CodeBadge = LectureBadge()
            LancementInstructions(3)
        LancementReussite(ID)
else :
    LancementInstructions(2)    #mode duo
    ID = randrange(0,25)        #choix aléatoire lettre
        LancementLettre(ID)     #audio
        CodeBadge = LectureBadge()
        GagneJ1 = false
        GagneJ2 = false
        while (GagneJ1! || GagneJ2!) :      #tant qu'un joueur n'a pas gagné
            CodeBadge = LectureBadge()
            if (CodeBadge == CodeJ1[ID]) :
                GagneJ1 = true
                LancementInstructions(4)
            if (CodeBadge == CodeJ1[ID]) :
                GagneJ1 = true
                LancementInstructions(5)
            else :
                compteur++
                if (compteur %6 == 0) :
                LancementInstructions(6) #echecs repetés
                    LancementIndice(ID)
        if (GagneJ1) :
            LancementReussite(26)
            LancementEchec(27)
        else :
            LancementReussite(27)
            LancementEchec(26)








    

    
    
    
