import time
import random
from rfid import *

BonneRep = 0
choix = random.randint(0,25)        #associe le nombre aux lettres alphabets
                                    #reperer code natif tag RFID
NumeroSerial = CodeSource[choix] 



while BonneRep != 8 :
    
    


NumSerial = LectureBadge()

