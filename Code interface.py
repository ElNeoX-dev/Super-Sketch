import pygame
from pygame.locals import *
import ctypes
from ctypes import windll
import time
from random import* 

# --> J'ai mit votre code dans SuperSketch.py
# PS: Déso pour le mal de crane

# Déclaration de la fonction de sélection de la couleur
def selection(pbt, cbt):
    global idFrame2
    global couleur  # Définition de variable globale du programme
    idFrame2 = (idFrame2 + 1) % 40  # Animation de l'image
    if idFrame2 < 20:
        fenetre.blit(pal1, pbt)
    else:
        fenetre.blit(pal2, pbt)
    if pygame.mouse.get_pressed() == (1, 0, 0):  # Changement de couleur lors d'un clic
        couleur = cbt
    return


def selectioncercle1():
    global rayon  # Définition de variable globale du programme
    if pygame.mouse.get_pressed() == (1, 0, 0):  # Changement de rayon lors d'un clic
        rayon = rayon + 5
        pygame.time.wait(100)
    return


def selectioncercle2():
    global rayon  # Définition de variable globale du programme

    if pygame.mouse.get_pressed() == (1, 0, 0):  # Changement de rayon lors d'un clic
        rayon = rayon - 5
    pygame.time.wait(100)
    return

def effacfx():
    pygame.draw.rect(fenetre, noir, (1720, 10, 190, 5))
    pygame.draw.rect(fenetre, noir, (1720, 10, 5, 80))
    pygame.draw.rect(fenetre, noir, (1910, 10, 5, 80))
    pygame.draw.rect(fenetre, noir, (1720, 85, 190, 5))    
    if pygame.mouse.get_pressed() == (1, 0, 0):  # Detection du clic
        pygame.draw.rect(fenetre, blanc, (400, 105, 1320, 865))
    

# Ouverture de la fenêtre Pygame en plein écran
pygame.init()
ctypes.windll.user32.SetProcessDPIAware()
true_res = (windll.user32.GetSystemMetrics(0), windll.user32.GetSystemMetrics(1))
fenetre = pygame.display.set_mode(true_res, pygame.FULLSCREEN)
pygame.display.set_caption("Super-sketch")
clock = pygame.time.Clock()
pygame.draw.rect(fenetre, (255, 255, 255), (0, 0, 1920, 1080))

# Initialisation des variables de couleur et des animations
largeur = ctypes.windll.user32.GetSystemMetrics(0)
logo1 = pygame.image.load("img/lobby/logo1.png")
logo2 = pygame.image.load("img/lobby/logo2.png")
pal1 = pygame.image.load("img/pal1.png").convert_alpha()
pal2 = pygame.image.load("img/pal2.png").convert_alpha()
fon = pygame.image.load("img/pal4.png").convert_alpha()
imgpeu = pygame.image.load("img/406sw.png").convert_alpha()
idFrame = 0
gris = (192, 192, 192)
rouge = (255, 0, 0)
vert = (0, 255, 0)
bleuf = (0, 0, 255)
blanc = (255, 255, 255)
noir = (0, 0, 0)
bleuc = (38, 188, 254)
violet = (238, 130, 238)
marron = (88, 41, 0)
police = pygame.font.SysFont("roboto-bold", 65)
police2 = pygame.font.SysFont("roboto-bold", 35)
MotEcrit=''
listecoord=[(50,200),(50,250),(50,300),(50,350),(50,400),(50,450),(50,500),(50,550),(50,600),(50,650)]
listmot=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
gomme1= pygame.image.load("img/gomme1.png").convert_alpha()
idFrame2=0
image =pygame.image.load("img/ima.png").convert_alpha()
ancienpx = 2500  # hors écran
ancienpy = 2500
px = 5000
py = 5000
choixmot = 'Z'
cache = "R"
motdevin="mot pas choisi"
easter=0
xE = 400
yE= 0



press = False
couleur = noir
rayon = 10
# Boucle infinie pour maintenir ou fermer la fenêtre
continuer = 1
while continuer:

    

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            continuer = 0
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RETURN:
                if MotEcrit == "406SW":
                    easter=1
                if MotEcrit != '' and MotEcrit!="406SW":                        
                    listmot.append(MotEcrit)
                MotEcrit=''                    
                           
            elif event.key == pygame.K_BACKSPACE:  # On enlève un carartère
                MotEcrit = MotEcrit[:-1]  # du 1er caractère inclus jusqu'au dernier exclu
                
            elif len(MotEcrit) < 16:  # 16 caractères max
                MotEcrit = MotEcrit+event.unicode

    # Détection de la position de la souris
    px, py = pygame.mouse.get_pos()

    # Placement des boutons sur l'écran
    entete = pygame.draw.rect(fenetre, gris, (400,0,1920,100))
    if easter != 1 or xE > 1520:
        
        if idFrame < 20:
            poslogo = logo1.get_rect(center=(int(largeur / 2), 50))
            fenetre.blit(logo1, poslogo)
        else:
            poslogo = logo2.get_rect(center=(int(largeur / 2), 50))
            fenetre.blit(logo2, poslogo)

    else:
        xE += 3
        fenetre.blit(imgpeu, (int(xE), yE))





    
    fenetre.blit(fon, (1820, 500))
    fenetre.blit(fon, (1720, 500))
    fonpal = pygame.draw.rect(fenetre, blanc, (1720,100, 200 ,980))
    btr = pygame.draw.rect(fenetre, rouge, (1820, 100, 100, 100))
    btbl = pygame.draw.rect(fenetre, blanc , (1820, 200, 100 ,100))
    btv = pygame.draw.rect(fenetre, vert, (1720, 100, 100, 100))
    btn = pygame.draw.rect(fenetre, noir, (1720, 200, 100, 100))
    btm = pygame.draw.rect(fenetre, marron, (1820, 300, 100, 100))
    btvi = pygame.draw.rect(fenetre, violet, (1720, 300, 100, 100))
    btbf = pygame.draw.rect(fenetre, bleuf, (1820, 400, 100, 100))
    btbc = pygame.draw.rect(fenetre, bleuc, (1720, 400, 100, 100))
    btcg = pygame.draw.circle(fenetre, noir, (1870, 550), 35)  # bouton circulaire gros rayon
    btcp = pygame.draw.circle(fenetre, noir, (1770, 550), 15)  # bouton circulaire petit rayon
    tab = pygame.draw.rect(fenetre, gris, (0, 0, 390, 1920))
    droite = pygame.draw.rect(fenetre, gris, (1720, 600, 200,1000))
    ligne = pygame.draw.rect(fenetre, noir, (390, 0, 10, 980))
    ligne2 = pygame.draw.rect(fenetre, noir, (0, 970, 1920, 10))
    bas = pygame.draw.rect(fenetre, gris, (0, 980, 1920, 1920))
    ligne3 = pygame.draw.rect(fenetre, noir, (1720, 100, 1000, 5))
    ligne4 = pygame.draw.rect(fenetre, noir, (1720, 200, 1000, 5))
    ligne5 = pygame.draw.rect(fenetre, noir, (1720, 300, 1000, 5))
    ligne6 = pygame.draw.rect(fenetre, noir, (1720, 400, 1000, 5))
    ligne7 = pygame.draw.rect(fenetre, noir, (1720, 500, 1000, 5))
    ligne8 = pygame.draw.rect(fenetre, noir, (1720, 600, 1000, 5))
    ligne9 = pygame.draw.rect(fenetre, noir, (1720, 100, 10, 1000))
    ligne10 = pygame.draw.rect(fenetre, noir, (1820, 100, 5, 500))
    ligne11 = pygame.draw.rect(fenetre, noir, (1915, 100, 5, 500))
    souligne = pygame.draw.rect(fenetre, noir,(10, 50, 340, 5))
    
    
    ligne12 = pygame.draw.rect(fenetre, noir, (390, 100, 1920, 5))
    

    
    fenetre.blit(gomme1, (1830,220))
    effac = pygame.draw.rect(fenetre, blanc, (1720,10,190,80))
    txteffac = police2.render("Tout effacer", True, (0, 0, 0))
    fenetre.blit(txteffac,(1745, 40))
    
    
    if choixmot != 'C':
        if cache != "K":
            limots = [word.strip() for word in open("dico.txt", encoding="utf-8")]
            mot1= choice(limots)
            mot2= choice(limots)
            mot3= choice(limots)
            affmot1 = police.render(mot1, True, (0, 0, 0))
            affmot2 = police.render(mot2, True, (0, 0, 0))
            affmot3 = police.render(mot3, True, (0, 0, 0))
            cache = "K"
                       

            
        bt1 = pygame.draw.rect(fenetre, gris, (460, 450, 380,75))
        bt2 = pygame.draw.rect(fenetre, gris, (850, 450, 380,75))
        bt3 = pygame.draw.rect(fenetre, gris, (1240, 450, 380,75))
        fenetre.blit(affmot1, (460, 450))
        fenetre.blit(affmot2, (850, 450))
        fenetre.blit(affmot3, (1240, 450))
        if bt1.collidepoint(px,py):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                choixmot='C'
                motdevin=mot1
                pygame.draw.rect(fenetre, blanc, (400, 105, 1320, 865))
        if bt2.collidepoint(px,py):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                    motdevin=mot2
                    choixmot='C'
                    pygame.draw.rect(fenetre, blanc, (400, 105, 1320, 865))
        if bt3.collidepoint(px,py):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                    motdevin=mot3
                    choixmot='C'
                    pygame.draw.rect(fenetre, blanc, (400, 105, 1320, 865))

    affmotdevin= police.render(motdevin, True, (0, 0, 0))
    fenetre.blit(affmotdevin, (1400, 1000))
    

    # Détection du moment quand la souris passe sur les boutons
    if btbf.collidepoint(px, py):
        selection(btbf, bleuf)
    if btr.collidepoint(px, py):
        selection(btr, rouge)
    if btv.collidepoint(px, py):
        selection(btv, vert)
    if btn.collidepoint(px, py):
        selection(btn, noir)
    if btm.collidepoint(px, py):
        selection(btm, marron)
    if btvi.collidepoint(px, py):
        selection(btvi, violet)
    if btbc.collidepoint(px, py):
        selection(btbc, bleuc)
    if btcg.collidepoint(px, py):
        selectioncercle1()
    if btcp.collidepoint(px, py):
        selectioncercle2()
    if btbl.collidepoint(px,py):
        selection(btbl, blanc)
    if effac.collidepoint(px,py):
        effacfx()

    # Détection clique gauche pour effectuer le dessin
    if pygame.mouse.get_pressed() == (1, 0, 0):
        pygame.draw.circle(fenetre, couleur, (px, py), rayon)

    i=0
    for i in range (10):
        listmot=listmot[-10:]
        textchat = police2.render(listmot[i], True, (0,0,0))
        fenetre.blit(textchat,(listecoord[i]))


    textMotEcrit = police.render('Ecrivez un mot : ' + MotEcrit, True, (0, 0, 0))  # txt,antialiasing,coul
    fenetre.blit(textMotEcrit, (50, 1000))
    textJoueur = police.render('joueurs en ligne : ', True, (0, 0, 0))  # txt,antialiasing,coul
    fenetre.blit(textJoueur, (10, 0))
    idFrame = (idFrame + 0.1) % 40
        
    
    pygame.display.update()
    clock.tick(300)
    
pygame.quit()
