
import pygame



mes_lettres=
            ["lettre_a","lettre_b","lettre_c","lettre_d","lettre_e","lettre_f","lettre_g","lettre_h","lettre_i",
             "lettre_j","lettre_k","lettre_l","lettre_m","lettre_n","lettre_o","lettre_p","lettre_q","lettre_r",
             "lettre_s","lettre_t","lettre_u","lettre_v","lettre_w","lettre_x","lettre_y","lettre_z"
             ]

mes_instructions =
    ["mode_solo","mode_duo","bonne_reponse","mauvaise_reponse", "Joueur1_identidiant", "Joueur2_identidiant","5_mauvaises_reponse"]  #instructions
    
mes_reussites =          ["bravo_a","bravo_b","bravo_c","bravo_d","bravo_e","bravo_f","bravo_g","bravo_h","bravo_i","bravo_j","bravo_k","bravo_l","bravo_m","bravo_n","bravo_o","bravo_p","bravo_q","bravo_r","bravo_s","bravo_t","bravo_u","bravo_v","bravo_w","bravo_x","bravo_y","bravo_z","j1_gagne","j2_gagne"]          #reussite lettre 0 à 25
    
mes_echecs = ["echec_a","echec_b","echec_c","echec_d","echec_e","echec_f","echec_g","echec_h","echec_i","echec_j","echec_k","echec_l","echec_m","echec_n","echec_o","echec_p","echec_q","echec_r","echec_s","echec_t","echec_u","echec_v","echec_w","echec_x","echec_y","echec_z","j1_perd","j2_perd"]          #echec lettre 0 à 25

mes_indices = ["indice_a","indice_b","indice_c","indice_d","indice_e","indice_f","indice_g","indice_h","indice_i","indice_j","indice_k","indice_l","indice_m","indice_n","indice_o","indice_p","indice_q","indice_r","indice_s","indice_t","indice_u","indice_v","indice_w","indice_x","indice_y","indice_z"]

def LancementLettre (identifiant) :
    pygame.mixer.init()
        pygame.mixer.Sound(mes_lettres[identifiant]+".wav").play().set_volume(0.7)

def LancementReussite (identifiant) :
    pygame.mixer.init()
        pygame.mixer.Sound(mes_reussites[identifiant]+".wav").play().set_volume(0.7)

def LancementInstructions(identifiant) :
    pygame.mixer.init()
        pygame.mixer.Sound(mes_instructions[identifiant]+".wav").play().set_volume(0.7)

def LancementEchec(identifiant) :
    pygame.mixer.init()
        pygame.mixer.Sound(mes_echecs[identifiant]+".wav").play().set_volume(0.7)

def LancementIndice(identifiant) :
    pygame.mixer.init()
        pygame.mixer.Sound(mes_indices[identifiant]+".wav").play().set_volume(0.7)


LancementLettre(0)
