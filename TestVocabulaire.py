"""
Le test de vocabulaire (The Vocabulary Test)

Ce script contient toutes les lignes de codes necessaires a la creation d'un
prototype d'un test de vocabulaire.
Pour passer du prototype a la version qui sera utilisee, il suffit de changer
les images, les bandes sons et les videos qui sont, pour le moment, toujours les
memes.
"""

__author__ = 'Mariette Marant <mariette.marant@orange.fr'
__version__ = '0.0'
__revision__ = ''
__date__ = '19-01-2020'

### ----- IMPORTATIONS -----

import expyriment
from PIL import Image
import os.path

### ----- INITIALISATION -----

exp = expyriment.design.Experiment(name="QUILS-Prototype")
expyriment.control.set_develop_mode(on=True) # enleve la possibilite d'entrer l'id du sujet
expyriment.control.defaults.window_mode = False # mise en plein ecran de l'interface

expyriment.control.initialize(exp)
mouse = expyriment.io.Mouse(show_cursor=True) #laisse la souris visible
screen = exp.screen
screen_size = screen.size
#ici les dimensions de l'ecran et celle de la fenetre sont les memes
center_x = exp.screen.center_x #abscisse du centre de l'ecran
center_y = exp.screen.center_y #ordonnee du centre de l'ecran

### ----- FONCTIONS -----

# ----- Utilitaires

def _conversion_origin(position):
    """Convertit des coordonnees.

    A partir de coordonnees exprimees dans un repere centre au coin bas gauche
    de l'ecran, retourne les coordonnees correspondantes exprimees dans un
    repere dont l'origine est le centre le l'ecran.

    Arguments :
        position : un tuple de deux entiers.

    Returne :
        Un tuple de deux entiers correspondant aux coordonnees re-exprimees
        dans le nouveau repere (dont l'origine est le centre de l'ecran).
    """
    x = position[0]-round(screen_size[0]/2)
    y = position[1]-round(screen_size[1]/2)
    return (x,y)

def save_data(block, trial, img, anim, top, nb, answer):
    """Enregistre les donnees de l'essai.

    Enregistre les donnees de l'essai sous la forme : nom du block en cours,
    numero de l'essai, reponse fournie par l'utilisateur, booleen correspondant
    a si la reponse fournie etait celle attendue (dans ce cas : True, sinon :
    False). La reponse est d'abord recuperee a partir du stimulus sur lequel
    l'utilisateur a clique, elle est comparee a l'ensemble des stimuli presentes
    dans cet essai pour savoir quel est son index dans cette liste de stimuli.
    Cet index est ensuite modifie en tenant compte de si, dans la liste des
    stimuli, une animation etait presente, si une image etait presentee en haut
    des autres, et si une deuxieme presentation etait faite. Cela amene donc a
    un retour a la meme numerotation que celle utilisee pour definir quelle
    reponse est la bonne.

    Arguments :
        block : bloc prealablement cree
        trial : essai prealablement cree et qui fait partie du bloc
        img : stimulus sur lequel l'utilisateur a clique
        anim : booleen (True si une animation est presente dans l'essai)
        top : booleen (True si une image est presentee au dessus des autres)
        nb : entier correspondant au nombre de presentations dans l'essai
        answer : iterateur sur la liste des reponses attendues par bloc
    """
    # Selection de la reponse attendue pour cet essai
    a = next(answer)
    for i in range(len(trial.stimuli)):
        # Recherche de l'index du stimulus clique
        if img == trial.stimuli[i]:
            # Prise en compte des caracteristiques de l'essai
            response = i - top - anim - nb + 1
            if response >= 5: # le stimulus fait partie de la 2eme presentation
                response-=4
            # Enregistrement des donnees
            exp.data.add([block.name, trial.id, response, a == response])

# ----- Carres

def _displaySquare(images, TRIAL):
    """Cree les stimulus necessaires a la creation d'un essai qui consiste en la
    presentation de 4 images de maniere carree (une en haut a droite, une en
    haut a gauche, une en bas a doite, une en bas a gauche : le 'carre' est
    centre par rapport a l'ecran), et les ajoute a l'essai correspondant.

    Definie une marge arbitraire. Utilise la classe Image pour avoir acces aux
    dimensions des images. A partir de ces dimensions et de la marge, calcule
    l'espace qui se trouvera entre chaque image. Calcule ensuite les positions
    de chaque image dans un repere centre au coin bas gauche de l'ecran et
    reconverties dans le repere utilise par expyriment, c'est-a-dire celui dont
    l'origine est le centre de l'ecran. Convertit enfin ces images, pour
    lesquelles on precise les positions, en stimuli visuels. Ajoute ces stimuli
    a l'essai passe en argument. Ces stimuli sont aussi stockes dans une liste
    pour definir une box qui va rendre les images cliquables. Ajoute cette box
    a la liste de toutes les boxes.

    Arguments :
        images : liste de 4 chaines de caracteres (noms des fichiers images)
        TRIAL : essai prealablement cree
    """
    # Definition d'une marge arbitraire

    margin = round((screen_size[0]/100)*8)

    # Creation des objets images

    image1 = Image.open(images[0])
    image2 = Image.open(images[1])
    image3 = Image.open(images[2])
    image4 = Image.open(images[3])

    # Definition de l'espace entre deux images

    # Recuperation des dimensions des images
    w, h = image1.size
    # Calcul de l'espace restant dans la fenetre apres avoir pris en compte les marges : "la boite"
    box_size = (screen_size[0]-2*margin,screen_size[1]-2*margin)
    # Calcul de l'espace restant dans la boite apres avoir pris en compte la taille des images : "le reste"
    rest = (box_size[0]-2*w, box_size[1]-2*h)
    # Definition de l'ecart entre deux images
    gap = round(rest[1]/1)

    # Creation et ajout des stimuli a l'essai

    stimuli = list()

    k = 0

    for i in [1, 0]:
        for j in [1, 0]:
            # Definition de la position des images sur l'ecran
            p = _conversion_origin((round(screen_size[0]/2 + (-1)**(j) * (gap/2 + w/2)), round(margin + i * (h+gap) + h/2)))
            # Creation des stimuli
            stim = expyriment.stimuli.Picture(images[k], position = p)
            # Stockage des stimuli dans une liste
            stimuli.append(stim)
            # Ajout des stimuli a l'essai
            TRIAL.add_stimulus(stim)
            k+=1

    # Ajout de la nouvelle box dans la liste BOXES

    BOXES.append(expyriment.io.TouchScreenButtonBox(stimuli))

## ---------- Images : une presentation par essai ----------

# ----- Lignes

def displayLine4Images(images, TRIAL):
    """Cree les stimulus necessaires a la creation d'un essai qui consiste en la
    presentation de 4 images sur la ligne horizontale qui passe par le centre de
    la fenetre, et les ajoute a l'essai correspondant.

    Definie une marge arbitraire. Utilise la classe Image pour avoir acces aux
    dimensions des images. A partir de ces dimensions et de la marge, calcule
    l'espace qui se trouvera entre chaque image. Calcule ensuite les positions
    de chaque image dans un repere centre au coin bas gauche de l'ecran et
    reconverties dans le repere utilise par expyriment, c'est-a-dire celui dont
    l'origine est le centre de l'ecran. Convertit enfin ces images, pour
    lesquelles on precise les positions, en stimuli visuels. Ajoute ces stimuli
    a l'essai passe en argument. Ces stimuli sont aussi stockes dans une liste
    pour definir une box qui va rendre les images cliquables. Ajoute cette box
    a la liste de toutes les boxes. Ajoute un tuple dans la liste des
    caracteristiques des essais pour renseigner celles de l'essai qui vient
    d'etre modifie.

    Arguments :
        images : liste de 4 chaines de caracteres (noms des fichiers images)
        TRIAL : essai prealablement cree
    """
    # Definition d'une marge arbitraire

    margin = round((screen_size[0]/100))

    # Creation des objets images

    image1 = Image.open(images[0])
    image2 = Image.open(images[1])
    image3 = Image.open(images[2])
    image4 = Image.open(images[3])

    # Definition de l'espace entre deux images

    # Recuperation des dimensions des images
    w, h = image1.size
    # Calcul de l'espace restant dans la fenetre apres avoir pris en compte les marges : "la boite"
    box_size = (screen_size[0]-2*margin,screen_size[1])
    # Calcul de l'espace restant dans la boite apres avoir pris en compte la taille des images : "le reste"
    rest = (box_size[0]-4*w, box_size[1]-1*h)
    # Definition de l'ecart entre deux images cote a cote
    gap = round(rest[0]/3)

    # Creation et ajout des stimuli a l'essai

    stimuli = list()

    for i in range(4):
        # Definition de la position des images sur l'ecran
        p = _conversion_origin((round(margin+i*(w+gap)+w/2), round(screen_size[1]/2)))
        # Creation des stimuli
        stim = expyriment.stimuli.Picture(images[i], position = p)
        # Stockage des stimuli dans une liste
        stimuli.append(stim)
        # Ajout des stimuli a l'essai
        TRIAL.add_stimulus(stim)

    # Ajout de la nouvelle box dans la liste BOXES

    BOXES.append(expyriment.io.TouchScreenButtonBox(stimuli))

    # Ajout des caracteristiques de l'essai dans la liste CARACTERISTICS

    CARACTERISTICS.append((False, False, 1))

def displayLine3Images(images, TRIAL):
    """Cree les stimulus necessaires a la creation d'un essai qui consiste en la
    presentation de 3 images sur la ligne horizontale qui passe par le centre de
    la fenetre, et les ajoute a l'essai correspondant.

    Definie une marge arbitraire. Utilise la classe Image pour avoir acces aux
    dimensions des images. A partir de ces dimensions et de la marge, calcule
    l'espace qui se trouvera entre chaque image. Calcule ensuite les positions
    de chaque image dans un repere centre au coin bas gauche de l'ecran et
    reconverties dans le repere utilise par expyriment, c'est-a-dire celui dont
    l'origine est le centre de l'ecran. Convertit enfin ces images, pour
    lesquelles on precise les positions, en stimuli visuels. Ajoute ces stimuli
    a l'essai passe en argument. Ces stimuli sont aussi stockes dans une liste
    pour definir une box qui va rendre les images cliquables. Ajoute cette box
    a la liste de toutes les boxes. Ajoute un tuple dans la liste des
    caracteristiques des essais pour renseigner celles de l'essai qui vient
    d'etre modifie.

    Arguments :
        images : liste de 3 chaines de caracteres (noms des fichiers images)
        TRIAL : essai prealablement cree
    """
    # Definition d'une marge arbitraire

    margin = round((screen_size[0]/100)*10)

    # Creation des objets images

    image1 = Image.open(images[0])
    image2 = Image.open(images[1])
    image3 = Image.open(images[2])

    # Definition de l'espace entre deux images

    # Recuperation des dimensions des images
    w, h = image1.size
    # Calcul de l'espace restant dans la fenetre apres avoir pris en compte les marges : "la boite"
    box_size = (screen_size[0]-2*margin,screen_size[1])
    # Calcul de l'espace restant dans la boite apres avoir pris en compte la taille des images : "le reste"
    rest = (box_size[0]-3*w, box_size[1]-1*h)
    # Definition de l'ecart entre deux images cote a cote
    gap = round(rest[0]/2)

    # Creation et ajout des stimuli a l'essai

    stimuli = list()

    for i in range(3):
        # Definition de la position des images sur l'ecran
        p = _conversion_origin((round(margin+i*(w+gap)+w/2), round(screen_size[1]/2)))
        # Creation des stimuli du bas de l'ecran
        stim = expyriment.stimuli.Picture(images[i], position = p)
        # Stockage des stimuli dans une liste
        stimuli.append(stim)
        # Ajout des stimuli a l'essai
        TRIAL.add_stimulus(stim)

    # Ajout de la nouvelle box dans la liste BOXES

    BOXES.append(expyriment.io.TouchScreenButtonBox(stimuli))

    # Ajout des caracteristiques de l'essai dans la liste CARACTERISTICS

    CARACTERISTICS.append((False, False, 1))

# Une image en haut, les autres en bas

def display1top3bottom(images, TRIAL):
    """Cree les stimulus necessaires a la creation d'un essai qui consiste en la
    presentation de 4 images telle que la premiere image est celle qui sera en
    haut de l'ecran (et ne sera pas cliquable) et les 3 autres seront disposees
    en dessous, et les ajoute a l'essai correspondant.

    Definie une marge arbitraire. Utilise la classe Image pour avoir acces aux
    dimensions des images. A partir de ces dimensions et de la marge, calcule
    l'espace qui se trouvera entre chaque image. Calcule ensuite les positions
    de chaque image dans un repere centre au coin bas gauche de l'ecran et
    reconverties dans le repere utilise par expyriment, c'est-a-dire celui dont
    l'origine est le centre de l'ecran. Convertit enfin ces images, pour
    lesquelles on precise les positions, en stimuli visuels. Ajoute ces stimuli
    a l'essai passe en argument. Ces stimuli sont aussi stockes dans une liste
    pour definir une box qui va rendre les images cliquables. Ajoute cette box
    a la liste de toutes les boxes. Ajoute un tuple dans la liste des
    caracteristiques des essais pour renseigner celles de l'essai qui vient
    d'etre modifie.

    Arguments :
        images : liste de 2 elements (le premier est une chaine de caracteres
        correspondant au nom de l'image que l'on veut placer en haut, le
        deuxieme est une liste de 3 chaines de caracteres correspondant aux noms
        des images que l'on veut placer en dessous)
        TRIAL : essai prealablement cree
    """
    # Recuperation du nom de l'image a placer en haut et de la liste de noms des images a placer en bas
    [top, bottom] = images

    # Definition d'une marge arbitraire

    margin_w = round((screen_size[0]/100)*30)
    margin_h = round((screen_size[0]/100)*4)

    # Creation des objets images

    imageTop = Image.open(top)
    imageBot1 = Image.open(bottom[0])
    imageBot2 = Image.open(bottom[1])
    imageBot3 = Image.open(bottom[2])

    # Definition de l'espace entre deux images

    # Recuperation des dimensions de l'image du haut
    wTop, hTop = imageTop.size
    # Recuperation des dimensions des images du bas
    w, h = imageBot1.size
    # Calcul de l'espace restant dans la fenetre apres avoir pris en compte les marges : "la boite"
    box_size = (screen_size[0]-2*margin_w,screen_size[1]-2*margin_h)
    # Calcul de l'espace restant dans la boite apres avoir pris en compte la taille des images : "le reste"
    rest = (box_size[0]-3*w, box_size[1]-h-hTop)
    # Definition de l'ecart entre deux images du bas cote a cote
    gap_w = round(rest[0]/2)
    # Definition de l'ecart entre l'image du dessus et celles du dessous
    gap_h = round(rest[1]/1)

    # Creation et ajout des stimuli a l'essai

    # Definition de la position de l'image du haut sur l'ecran
    pTop = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    # Creation du stimulus du haut de l'ecran
    stimTop = expyriment.stimuli.Picture(top, position = pTop)
    # Ajout du stimulus du haut de l'ecran a l'essai
    TRIAL.add_stimulus(stimTop)

    stimuli = list()

    for i in range(3):
        # Definition de la position des images du bas sur l'ecran
        p = _conversion_origin((round(screen_size[0]/2 + (i-1)*(gap_w/2 + w + w/2)), round(margin_h+h/2)))
        # Creation des stimuli du bas de l'ecran
        stim = expyriment.stimuli.Picture(bottom[i], position = p)
        # Stockage des stimuli du bas de l'ecran dans une liste
        stimuli.append(stim)
        # Ajout des stimuli du bas de l'ecran a l'essai
        TRIAL.add_stimulus(stim)

    # Ajout de la nouvelle box dans la liste BOXES

    BOXES.append(expyriment.io.TouchScreenButtonBox(stimuli, stimTop))

    # Ajout des caracteristiques de l'essai dans la liste CARACTERISTICS

    CARACTERISTICS.append((False, True, 1))

def display1top4bottom(images, TRIAL):
    """Cree les stimulus necessaires a la creation d'un essai qui consiste en la
    presentation de 5 images telle que la premiere image est celle qui sera en
    haut de l'ecran (et ne sera pas cliquable) et les 4 autres seront disposees
    en dessous, et les ajoute a l'essai correspondant.

    Definie une marge arbitraire. Utilise la classe Image pour avoir acces aux
    dimensions des images. A partir de ces dimensions et de la marge, calcule
    l'espace qui se trouvera entre chaque image. Calcule ensuite les positions
    de chaque image dans un repere centre au coin bas gauche de l'ecran et
    reconverties dans le repere utilise par expyriment, c'est-a-dire celui dont
    l'origine est le centre de l'ecran. Convertit enfin ces images, pour
    lesquelles on precise les positions, en stimuli visuels. Ajoute ces stimuli
    a l'essai passe en argument. Ces stimuli sont aussi stockes dans une liste
    pour definir une box qui va rendre les images cliquables. Ajoute cette box
    a la liste de toutes les boxes. Ajoute un tuple dans la liste des
    caracteristiques des essais pour renseigner celles de l'essai qui vient
    d'etre modifie.

    Arguments :
        images : liste de 2 elements (le premier est une chaine de caracteres
        correspondant au nom de l'image que l'on veut placer en haut, le
        deuxieme est une liste de 4 chaines de caracteres correspondant aux noms
        des images que l'on veut placer en dessous)
        TRIAL : essai prealablement cree
    """
    # Recuperation du nom de l'image a placer en haut et de la liste de noms des images a placer en bas

    [top, bottom] = images

    # Definition d'une marge arbitraire

    margin_w = round((screen_size[0]/100)*5)
    margin_h = round((screen_size[0]/100)*4)

    # Creation des objets images

    imageTop = Image.open(top)
    imageBot1 = Image.open(bottom[0])
    imageBot2 = Image.open(bottom[1])
    imageBot3 = Image.open(bottom[2])
    imageBot4 = Image.open(bottom[3])

    # Definition de l'espace entre deux images

    # Recuperation des dimensions de l'image du haut
    wTop, hTop = imageTop.size
    # Recuperation des dimensions des images du bas
    w, h = imageBot1.size
    # Calcul de l'espace restant dans la fenetre apres avoir pris en compte les marges : "la boite"
    box_size = (screen_size[0]-2*margin_w,screen_size[1]-2*margin_h)
    # Calcul de l'espace restant dans la boite apres avoir pris en compte la taille des images : "le reste"
    rest = (box_size[0]-4*w, box_size[1]-h-hTop)
    # Definition de l'ecart entre deux images du bas cote a cote
    gap_w = round(rest[0]/3)
    # Definition de l'ecart entre l'image du dessus et celles du dessous
    gap_h = round(rest[1]/1)

    # Creation et ajout des stimuli a l'essai

    # Definition de la position de l'image du haut sur l'ecran
    pTop = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    # Creation du stimulus du haut de l'ecran
    stimTop = expyriment.stimuli.Picture(top[0], position = pTop)
    # Ajout du stimulus du haut de l'ecran a l'essai
    TRIAL.add_stimulus(stimTop)

    stimuli = list()

    for i in range(4):
        # Definition de la position des images du bas sur l'ecran
        p = _conversion_origin((round(margin_w + i * (w+gap_w) + w/2), round(margin_h + h/2)))
        # Creation des stimuli du bas de l'ecran
        stim = expyriment.stimuli.Picture(bottom[i], position = p)
        # Stockage des stimuli du bas de l'ecran dans une liste
        stimuli.append(stim)
        # Ajout des stimuli du bas de l'ecran a l'essai
        TRIAL.add_stimulus(stim)

    # Ajout de la nouvelle box dans la liste BOXES

    BOXES.append(expyriment.io.TouchScreenButtonBox(stimuli, stimTop))

    # Ajout des caracteristiques de l'essai dans la liste CARACTERISTICS

    CARACTERISTICS.append((False, True, 1))

## ---------- Images : deux presentations par esssai ----------

# Avec animation

def display1anim1image(images, TRIAL):
    """Cree les stimulus necessaires a la creation d'un essai qui consiste en
    deux presentations, et les ajoute a l'essai correspondant. La premiere est
    celle d'une animation au centre de l'ecran. La deuxieme est celle d'une
    image au centre de l'ecran et qui sera cliquable.

    Convertit les images en stimuli visuels. Ajoute ces stimuli a l'essai passe
    en argument. Rend la deuxieme image cliquable en l'integrant a une box.
    Ajoute cette box a la liste de toutes les boxes. Ajoute un tuple dans la
    liste des caracteristiques des essais pour renseigner celles de l'essai qui
    vient d'etre modifie.

    Arguments :
        images : liste de 2 chaines de caracteres (la premiere correspond au nom
        de l'image qui va servir d'animation et la deuxieme correspond au nom de
        l'image qui sera cliquable).
        TRIAL : essai prealablement cree
    """
    # Recuperation du nom de l'image correspondant a l'animation, du nom de l'image a placer en haut et de la liste de noms des images a placer en bas

    [anim, image] = images

    # Creation et ajout des stimuli a l'essai

    # Creation du stimulus qui sert d'animation
    stimAnim = expyriment.stimuli.Picture(anim)
    # Ajout du stimulus qui sert d'animation a l'essai
    TRIAL.add_stimulus(stimAnim)
    # Creation du stimulus qui sera cliquable
    stim = expyriment.stimuli.Picture(image)
    # Ajout du stimulus qui sera cliquable a l'essai
    TRIAL.add_stimulus(stim)

    # Ajout de la nouvelle box dans la liste BOXES

    BOXES.append(expyriment.io.TouchScreenButtonBox(stim))

    # Ajout des caracteristiques de l'essai dans la liste CARACTERISTICS

    CARACTERISTICS.append((True, False, 2))

def display1anim1top3bottom(images, TRIAL):
    """Cree les stimulus necessaires a la creation d'un essai qui consiste en
    deux presentations, et les ajoute a l'essai correspondant. La premiere est
    celle d'une animation au centre de l'ecran. La deuxieme est celle de 4
    images telle que la premiere image est celle qui sera en haut de l'ecran (et
    ne sera pas cliquable) et les 3 autres seront disposees en dessous.

    Definie une marge arbitraire. Utilise la classe Image pour avoir acces aux
    dimensions des images. A partir de ces dimensions et de la marge, calcule
    l'espace qui se trouvera entre chaque image. Calcule ensuite les positions
    de chaque image dans un repere centre au coin bas gauche de l'ecran et
    reconverties dans le repere utilise par expyriment, c'est-a-dire celui dont
    l'origine est le centre de l'ecran. Convertit enfin ces images, pour
    lesquelles on precise les positions, en stimuli visuels. Ajoute ces stimuli
    a l'essai passe en argument. Ces stimuli sont aussi stockes dans une liste
    pour definir une box qui va rendre les images cliquables. Ajoute cette box
    a la liste de toutes les boxes.Ajoute un tuple dans la liste des
    caracteristiques des essais pour renseigner celles de l'essai qui vient
    d'etre modifie.

    Arguments :
        images : liste de 3 elements (le premier est une chaine de caracteres
        correspondant au nom de l'image qui va servir d'animation, le deuxieme
        est une chaine de caracteres correspondant au nom de l'image que l'on
        veut placer en haut, le toisieme est une liste de 3 chaines de
        caracteres correspondant aux noms des images que l'on veut placer en
        dessous)
        TRIAL : essai prealablement cree
    """
    # Recuperation du nom de l'image correspondant a l'animation, du nom de l'image a placer en haut et de la liste de noms des images a placer en bas

    [anim, top, bottom] = images

    # Definition d'une marge arbitraire

    margin_w = round((screen_size[0]/100)*30)
    margin_h = round((screen_size[0]/100)*4)

    # Creation des objets images

    imageAnim = Image.open(anim)
    imageTop = Image.open(top)
    imageBot1 = Image.open(bottom[0])
    imageBot2 = Image.open(bottom[1])
    imageBot3 = Image.open(bottom[2])

    # Definition de l'espace entre deux images

    # Recuperation des dimensions de l'image du haut
    wTop, hTop = imageTop.size
    # Recuperation des dimensions des images du bas
    w, h = imageBot1.size
    # Calcul de l'espace restant dans la fenetre apres avoir pris en compte les marges : "la boite"
    box_size = (screen_size[0]-2*margin_w,screen_size[1]-2*margin_h)
    # Calcul de l'espace restant dans la boite apres avoir pris en compte la taille des images : "le reste"
    rest = (box_size[0]-3*w, box_size[1]-h-hTop)
    # Definition de l'ecart entre deux images du bas cote a cote
    gap_w = round(rest[0]/2)
    # Definition de l'ecart entre l'image du dessus et celles du dessous
    gap_h = round(rest[1]/1)

    # Creation et ajout des stimuli a l'essai

    # Definition de la position de l'animation sur l'ecran
    pAnim = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    # Creation du stimulus qui sert d'animation
    stimAnim = expyriment.stimuli.Picture(anim, position = pAnim)
    # Ajout du stimulus qui sert d'animation a l'essai
    TRIAL.add_stimulus(stimAnim)

    # Definition de la position de l'image du haut sur l'ecran
    pTop = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    # Creation du stimulus du haut de l'ecran
    stimTop = expyriment.stimuli.Picture(top, position = pTop)
	# Ajout du stimulus du haut de l'ecran a l'essai
    TRIAL.add_stimulus(stimTop)

    stimuli = list()

    for i in range(3):
        # Definition de la position des images du bas sur l'ecran
        p = _conversion_origin((round(screen_size[0]/2 + (i-1)*(gap_w/2 + w + w/2)), round(margin_h+h/2)))
        # Creation des stimuli du bas de l'ecran
        stim = expyriment.stimuli.Picture(bottom[i], position = p)
        # Stockage des stimuli du bas de l'ecran dans une liste
        stimuli.append(stim)
        # Ajout des stimuli du bas de l'ecran a l'essai
        TRIAL.add_stimulus(stim)

    # Ajout de la nouvelle box dans la liste BOXES

    BOXES.append(expyriment.io.TouchScreenButtonBox(stimuli, stimTop))

    # Ajout des caracteristiques de l'essai dans la liste CARACTERISTICS

    CARACTERISTICS.append((True, True, 2))

def display1anim1top4bottom(images, TRIAL):
    """Cree les stimulus necessaires a la creation d'un essai qui consiste en
    deux presentations, et les ajoute a l'essai correspondant. La premiere est
    celle d'une animation au centre de l'ecran. La deuxieme est celle de 5
    images telle que la premiere image est celle qui sera en haut de l'ecran (et
    ne sera pas cliquable) et les 4 autres seront disposees en dessous.

    Definie une marge arbitraire. Utilise la classe Image pour avoir acces aux
    dimensions des images. A partir de ces dimensions et de la marge, calcule
    l'espace qui se trouvera entre chaque image. Calcule ensuite les positions
    de chaque image dans un repere centre au coin bas gauche de l'ecran et
    reconverties dans le repere utilise par expyriment, c'est-a-dire celui dont
    l'origine est le centre de l'ecran. Convertit enfin ces images, pour
    lesquelles on precise les positions, en stimuli visuels. Ajoute ces stimuli
    a l'essai passe en argument. Ces stimuli sont aussi stockes dans une liste
    pour definir une box qui va rendre les images cliquables. Ajoute cette box
    a la liste de toutes les boxes. Ajoute un tuple dans la liste des
    caracteristiques des essais pour renseigner celles de l'essai qui vient
    d'etre modifie.

    Arguments :
        images : liste de 3 elements (le premier est une chaine de caracteres
        correspondant au nom de l'image qui va servir d'animation, le deuxieme
        est une chaine de caracteres correspondant au nom de l'image que l'on
        veut placer en haut, le toisieme est une liste de 4 chaines de
        caracteres correspondant aux noms des images que l'on veut placer en
        dessous)
        TRIAL : essai prealablement cree
    """
    # Recuperation du nom de l'image correspondant a l'animation, du nom de l'image a placer en haut et de la liste de noms des images a placer en bas

    [anim, top, bottom] = images

    # Definition d'une marge arbitraire

    margin_w = round((screen_size[0]/100)*2)
    margin_h = round((screen_size[0]/100)*2)

    # Creation des objets images

    imageAnim = Image.open(anim)
    imageTop = Image.open(top)
    imageBot1 = Image.open(bottom[0])
    imageBot2 = Image.open(bottom[1])
    imageBot3 = Image.open(bottom[2])
    imageBot4 = Image.open(bottom[3])

    # Definition de l'espace entre deux images

    # Recuperation des dimensions de l'image du haut
    wTop, hTop = imageTop.size
    # Recuperation des dimensions des images du bas
    w, h = imageBot1.size
    # Calcul de l'espace restant dans la fenetre apres avoir pris en compte les marges : "la boite"
    box_size = (screen_size[0]-2*margin_w,screen_size[1]-2*margin_h)
    # Calcul de l'espace restant dans la boite apres avoir pris en compte la taille des images : "le reste"
    rest = (box_size[0]-4*w, box_size[1]-h-hTop)
    # Definition de l'ecart entre deux images du bas cote a cote
    gap_w = round(rest[0]/3)
    # Definition de l'ecart entre l'image du dessus et celles du dessous
    gap_h = round(rest[1]/1)

    # Creation et ajout des stimuli a l'essai

    # Definition de la position de l'animation sur l'ecran
    pAnim = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    # Creation du stimulus qui sert d'animation
    stimAnim = expyriment.stimuli.Picture(anim, position = pAnim)
    # Ajout du stimulus qui sert d'animation a l'essai
    TRIAL.add_stimulus(stimAnim)

    # Definition de la position de l'image du haut sur l'ecran
    pTop = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    # Creation du stimulus du haut de l'ecran
    stimTop = expyriment.stimuli.Picture(top, position = pTop)
    # Ajout du stimulus du haut de l'ecran a l'essai
    TRIAL.add_stimulus(stimTop)

    stimuli = list()

    for i in range(4):
        # Definition de la position des images du bas sur l'ecran
        p = _conversion_origin((round(margin_w + i * (w+gap_w) + w/2), round(margin_h + h/2)))
        # Creation des stimuli du bas de l'ecran
        stim = expyriment.stimuli.Picture(bottom[i], position = p)
        # Stockage des stimuli du bas de l'ecran dans une liste
        stimuli.append(stim)
        # Ajout des stimuli du bas de l'ecran a l'essai
        TRIAL.add_stimulus(stim)

    # Ajout de la nouvelle box dans la liste BOXES

    BOXES.append(expyriment.io.TouchScreenButtonBox(stimuli, stimTop))

    # Ajout des caracteristiques de l'essai dans la liste CARACTERISTICS

    CARACTERISTICS.append((True, True, 2))

# Sans animation

def displaySquareTwice(images, TRIAL):
    """Cree les stimulus necessaires a la creation d'un essai qui consiste en
    deux presentations, et les ajoute a l'essai correspondant. Chacune des deux
    presentations consiste en l'affichage de 4 images de maniere carree : une en
    haut a droite, une en haut a gauche, une en bas a doite, une en bas a
    gauche. Le 'carre' est centre par rapport a l'ecran.

    Appelle deux fois la fonction _displaySquare. Ajoute un tuple dans la liste
    des caracteristiques des essais pour renseigner celles de l'essai qui vient
    d'etre modifie.

    Arguments :
        images : liste de 2 listes (chacune des deux listes contient 4 chaines
        de caracteres correspondant aux noms des fichiers images)
        TRIAL : essai prealablement cree
    """
    list1 = images[0]
    list2 = images[1]
    _displaySquare(list1, TRIAL)
    _displaySquare(list2, TRIAL)
    CARACTERISTICS.append((False, False, 2))

def display1top3bottomTwice(images, TRIAL):
    """Cree les stimulus necessaires a la creation d'un essai qui consiste en
    deux presentations, et les ajoute a l'essai correspondant. Chacune des deux
    presentations consiste en l'affichage de 4 images telle que la premiere
    image est celle qui sera en haut de l'ecran (et ne sera pas cliquable) et
    les 3 autres seront disposees en dessous.

    Appelle deux fois la fonction display1top3bottom. Etant donne que cette
    fonction est aussi utilisee pour modifier des essais, elle ajoute un tuple
    dans la liste des caracteristiques a chaque fois qu'elle est appellee. Pour
    eliminer ces 'fausses' informations creees par les deux appels de cette
    fonction ici, supprime les deux derniers elements de la liste des
    caracteristiques. Ajoute la 'vraie' information en ajoutant un tuple dans la
    liste des caracteristiques des essais pour renseigner celles de l'essai qui
    vient d'etre modifie.

    Arguments :
        images : liste de 2 listes (chacune des deux listes contient 2 elements,
        le premier est une chaine de caracteres correspondant au nom de l'image
        que l'on veut placer en haut, le deuxieme est une liste de 3 chaines de
        caracteres correspondant aux noms des images que l'on veut placer en
        dessous)
        TRIAL : essai prealablement cree
    """
    list1 = images[0]
    list2 = images[1]
    display1top3bottom(list1, TRIAL)
    display1top3bottom(list2, TRIAL)
    CARACTERISTICS.pop()
    CARACTERISTICS.pop()
    CARACTERISTICS.append((False, True, 2))

## ---------- Videos : transitions entre les blocs ----------

def displayVideo(video):
    """Cree un stimulus video et le pre-charge.

    Cree le stimulus. Arrete le syteme audio de l'ordinateur pour pouvoir le
    pre-chargement de la video. Remet le systeme audio en route. Ajoute le
    stimulus a la liste des transitions videos.

    Arguments :
        video : chaine de caracteres correspondant au nom d'un fichier video
        contenu dans le fichier 'videos'.
    """
    video = expyriment.stimuli.Video(os.path.join("videos", video))
    expyriment.control.stop_audiosystem()
    video.preload()
    expyriment.control.start_audiosystem()
    TRANSITIONS.append(video)

## ---------- Audio : pendant les essais ----------

def displayAudio(audio, TRIAL):
    """Cree un stimulus audio et l'ajoute a l'essai correspondant.

    Si plusieurs audio sont donnes, boucle sur la liste de ces audios en creant
    les stimuli et les ajoutant a l'essai. Si un seul audio est donne, cree le
    stimulus et l'ajoute a l'essai.

    Arguments :
        audio : chaine de caracteres correspondant au nom d'un fichier audio
        contenu dans le fichier 'sounds'
        TRIAL : essai prealablement cree
    """
    if isinstance(audio, list):
        for a in audio:
            stimAudio = expyriment.stimuli.Audio(os.path.join("sounds", a))
            TRIAL.add_stimulus(stimAudio)
    else:
        stimAudio = expyriment.stimuli.Audio(os.path.join("sounds", audio))
        TRIAL.add_stimulus(stimAudio)

### ----- VARIABLES -----

## ---------- Variables specifiques a la version prototype ----------

carre = 'degas-carre-petit.jpg'
rectangle = 'degas-rectangle.jpg'
portrait = 'degas-portrait.jpg'
son = '1.wav'
video = 'Flower.mp4'

## ---------- Varibales mises a jour lors de l'appel des fonctions ----------

# Liste des caracteristiques des essais
CARACTERISTICS = list()

# Liste des boxes
BOXES = list()

# Liste des transitions entre les blocs
TRANSITIONS = list()

## ---------- Variables qui definissent le contenu du test ----------

list_of_blocks = ["PRACTISE",
                    "WH-QUESTIONS",
                    "PAST TENSE",
                    "VERB LEARNING",
                    "PREPOSITIONAL PHRASES",
                    "CONVERTING ACTIVE TO PASSIVE",
                    "EMBEDED CLAUSES",
                    "NOUNS",
                    "VERBS",
                    "NOUN LEARNING",
                    "PREPOSITIONS",
                    "ADJECTIVE LEARNING",
                    "CONJUNCTIONS"]

list_of_lengths = [3, 5, 4, 4, 3, 2, 4, 3, 5, 5, 5, 5, 3] # nb d'essais par bloc

list_of_functions = [[displayLine4Images, displayLine3Images, display1top3bottom],
                        display1top3bottom,
                        display1anim1image,
                        display1anim1top3bottom,
                        displayLine3Images,
                        display1anim1top3bottom,
                        display1anim1top4bottom,
                        displayLine4Images,
                        displayLine3Images,
                        displaySquareTwice,
                        displayLine3Images,
                        display1top3bottomTwice,
                        display1top3bottom]

list_of_images = [[[carre, carre, carre, carre], [carre, carre, carre], [rectangle, [carre, carre, carre]]],
                        [rectangle, [carre, carre, carre]],
                        [rectangle, rectangle],
                        [rectangle, rectangle, [carre, carre, carre]],
                        [carre, carre, carre],
                        [rectangle, rectangle, [carre, carre, carre]],
                        [rectangle, rectangle, [carre, carre, carre, carre]],
                        [carre, carre, carre, carre],
                        [carre, carre, carre],
                        [[carre, carre, carre, carre], [carre, carre, carre, carre]],
                        [portrait, portrait, portrait],
                        [[carre, [carre, carre, carre]], [carre, [carre, carre, carre]]],
                        [rectangle, [carre, carre, carre]]]

list_of_sounds = [[son, son, son],
                    son,
                    [son, son],
                    [son, son],
                    son,
                    [son, son],
                    [son, son],
                    son,
                    son,
                    [son,son],
                    son,
                    [son,son],
                    son]

list_of_transitions = [video,
                        video,
                        video,
                        video,
                        video,
                        video,
                        video,
                        video,
                        video,
                        video,
                        video,
                        video,
                        video]

list_of_answers = [[2, 3, 3],
                    [1, 1, 3, 2, 2],
                    [1, 1, 1, 1],
                    [2, 1, 3, 2],
                    [1, 2, 3],
                    [3, 2],
                    [2, 4, 1, 3],
                    [2, 3, 4],
                    [1, 3, 2, 1, 2],
                    [1, 3, 2, 2, 4, 3, 3, 1, 2, 4],
                    [1, 2, 3, 2, 1],
                    [1, 3, 3, 2, 3, 1, 2, 2, 2, 4],
                    [1, 1, 3]] # reponses attendues pour chaque essai, par bloc

### ----- EXPERIENCE -----

## ---------- Entrainement : bloc 0 ----------

name0 = list_of_blocks[0]
length0 = list_of_lengths[0]
functions0 = list_of_functions[0]
images0 = list_of_images[0]
sounds0 = list_of_sounds[0]

block0 = expyriment.design.Block(name=name0)

for t in range(length0):
    trial0 = expyriment.design.Trial()
    displayAudio(sounds0[t], trial0)
    functions0[t](images0[t], trial0)
    block0.add_trial(trial0)
exp.add_block(block0)

## ---------- Test : bloc 1 à bloc 12 ----------

for b in range(1,13):
    block = expyriment.design.Block(name=list_of_blocks[b])
    for t in range(list_of_lengths[b]):
        trial = expyriment.design.Trial()
        displayAudio(list_of_sounds[b], trial)
        list_of_functions[b](list_of_images[b], trial)
        block.add_trial(trial)
    exp.add_block(block)

## ---------- Transitions : videos ----------

for t in list_of_transitions:
    displayVideo(t)

## ---------- Iterateurs : suivi de l'avancement de l'experience ----------

cara = iter(CARACTERISTICS)
box = iter(BOXES)
tran = iter(TRANSITIONS)

### ---------- MAIN ----------

exp.add_data_variable_names(['block', 'trial', 'response', 'True/False'])

expyriment.control.start()

for block in exp.blocks:

    t = next(tran)
    answers = list_of_answers[block.id]
    answer = iter(answers)

    for trial in block.trials:

        c = next(cara)
        anim = c[0]
        top = c[1]
        nb = c[2]
        b = next(box)

        if not anim and nb == 1:
            # Presentation de l'audio
            trial.stimuli[0].play()
            # Presentation du set d'images
            b.show()
            # Attente de la fin de l'audio
            expyriment.control.wait_end_audiosystem()
            # Recuperation de la reponse de l'utilisateur
            img, resptime = b.wait()
            # Enregistrement de la reponse
            save_data(block, trial, img, anim, top, nb, answer)

        elif anim and nb == 2:
            # Presentation du 1er audio
            trial.stimuli[0].play()
            # Presentation de l'animation
            trial.stimuli[2].present()
            # Attente de la fin de l'audio
            expyriment.control.wait_end_audiosystem()
            # Nettoyage de l'ecran
            exp.clock.wait(1000)
            exp.screen.clear()
            exp.screen.update()
            # Presentation du 2eme audio
            trial.stimuli[1].play()
            # Presentation du set d'images
            b.show()
            # Attente de la fin de l'audio
            expyriment.control.wait_end_audiosystem()
            # Recuperation de la reponse de l'utilisateur
            img, resptime = b.wait()
            # Enregistrement de la reponse
            save_data(block, trial, img, anim, top, nb, answer)

        else:
            # Presentation du 1er audio
            trial.stimuli[0].play()
            # Presentation du 1er set d'images
            b.show()
            # Attente de la fin de l'audio
            expyriment.control.wait_end_audiosystem()
            # Recuperation de la reponse de l'utilisateur
            img1, resptime = b.wait()
            # Nettoyage de l'ecran
            exp.screen.clear()
            exp.screen.update()
            exp.clock.wait(1000)
            # Presentation du 2eme audio
            trial.stimuli[1].play()
            # Presentation du 2eme set d'images
            b = next(box)
            b.show()
            # Attente de la fin de l'audio
            expyriment.control.wait_end_audiosystem()
            # Recuperation de la reponse de l'utilisateur
            img2, resptime = b.wait()
            # Enregistrement des reponses
            save_data(block, trial, img1, anim, top, nb, answer)
            save_data(block, trial, img2, anim, top, nb, answer)

        exp.screen.clear()
        exp.screen.update()
        exp.clock.wait(1000)

    exp.screen.clear()
    exp.screen.update()

    # Transition

    expyriment.control.stop_audiosystem()
    t.play()
    expyriment.control.start_audiosystem()
    t.present()
    t.wait_end()
    t.stop()

    exp.screen.clear()
    exp.screen.update()
    exp.clock.wait(2000)

expyriment.control.end()

# Enregistrement des reponses donnees dans un fichier CSV

expyriment.misc.data_preprocessing.write_concatenated_data(data_folder = 'data', file_name = 'VocabularyTest', output_file = 'results.csv' )
