import RPi.GPIO as GPIO
from pirc522 import RFID
import time


CodeJ1 = ["[230, 240, 141, 171, 60]","[109, 121, 140, 171, 51]","[230, 141, 230, 213, 88]","[37, 32, 141, 171, 35]"] #completer les numéros avec carte dans ordre alphabétique et marquez immédiatement sur les cartes

CodeJ2 = ["[181, 231, 144, 179, 104]","[66, 254, 80, 242, 30]","[16, 172, 141, 171, 154]","[162, 211, 141, 171, 87]"] #meme que le CodeJ1


rc522 = RFID() #on declare le premier RFID

def LectureBadge() :
 while True:
  rc522.wait_for_tag()
  (error, tag_type) = rc522.request()
  if not error:
    (error, uid) = rc522.anticoll()
    if not error:
      return str(uid)
      time.sleep(1)

def ComparaisonIndex(str UID) :
    for i=0:len(CodeJ1)-1 : 
        if CodeJ1[i]==UID :
            return i 
        


