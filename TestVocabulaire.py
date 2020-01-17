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

### ----- INITIALIZATION -----

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

### ----- FUNCTIONS -----

def _conversion_origin(position):
    """Convertit des coordonnees.

    A partir de coordonnees exprimees dans un repere centre au coin bas gauche
    de l'ecran, retourne les coordonnees correspondantes exprimees dans un
    repere centre au centre le l'ecran.

    Args:
        position: un tuple de deux entiers.

    Returns:
        Un tuple de deux entiers correspondant aux coordonnees re-exprimees
        dans le nouveau repere (dont l'origine est le centre de l'ecran).
    """
    x = position[0]-round(screen_size[0]/2)
    y = position[1]-round(screen_size[1]/2)
    return (x,y)

## ---------- Images : one presentation per trial ----------

# Ligns

def displayLine4Images(images, TRIAL):
    """Cree les stimulus et informations necessaires a la creation d'un essai
    qui consiste en la presentation de 4 images sur la ligne horizontale qui
    passe par le centre de la fenetre"

    Convertit le fichier audio en stimulus audio qui a pour but d'etre presente
    en meme temps que les 4 images. Utilise la classe Image pour avoir acces
    aux dimensions des images. A partir de ses dimensions et de marges decidees
    arbitrairement, calcule l'espace qui se trouvera entre chaque photo. Calcule
    ensuite les positions de chaque image dans un repere centre au coin bas
    gauche de l'ecran et reconverties dans le repere utilise par expyriment,
    c'est-a-dire dont l'origine est le centre de l'ecran. Convertit enfin ces
    images, pour lesquelles on precise les positions, en stimuli visuels.
    Retourne le stimulus audio, la liste des 4 stimuli visuels, le booleen False
    qui correspond a la presence d'une animation parmi ces stimulis (ici, ce
    n'est pas le cas, donc vaut False), le booleen False qui correspond a la
    presence d'une image au dessus des autres et qui ne sera pas cliquable (ici,
    ce n'est pas le cas, donc vaut False), l'entier 1 pour specifier que la
    presentation se fera en une seule fois.

    Arguments :
        audio : chaine de caracteres (nom du fichier audio)
        images : liste de 4 chaines de caracteres (noms des fichiers images)

    Retourne :
        Un stimulus audio
        Une liste de 4 stimuli visuels
        Un booleen (False : pas d'animation pour cet essai)
        Un booleen (False : pas d'image au dessus des autres pour cet essai)
        Un entier (1 : une seule presentation pour cet essai)
    """
    margin = round((screen_size[0]/100))

    image1 = Image.open(images[0])
    image2 = Image.open(images[1])
    image3 = Image.open(images[2])
    image4 = Image.open(images[3])

    w, h = image1.size
    box_size = (screen_size[0]-2*margin,screen_size[1])
    rest = (box_size[0]-4*w, box_size[1]-1*h) #attention ici 4
    gap = round(rest[0]/3) #attention ici 3

    stimuli = list()

    for i in range(4):
        p = _conversion_origin((round(margin+i*(w+gap)+w/2), round(screen_size[1]/2)))
        stim = expyriment.stimuli.Picture(images[i], position = p)
        stimuli.append(stim)
        TRIAL.add_stimulus(stim)

    BOXES.append(expyriment.io.TouchScreenButtonBox(stimuli))

    CARACTERISTICS.append((False, False, 1))

def displayLine3Images(images, TRIAL):
    """Cree les stimulus et informations necessaires a la creation d'un essai
    qui consiste en la presentation de 3 images sur la ligne horizontale qui
    passe par le centre de la fenetre"

    Convertit le fichier audio en stimulus audio qui a pour but d'etre presente
    en meme temps que les 3 images. Utilise la classe Image pour avoir acces
    aux dimensions des images. A partir de ses dimensions et de marges decidees
    arbitrairement, calcule l'espace qui se trouvera entre chaque photo. Calcule
    ensuite les positions de chaque image dans un repere centre au coin bas
    gauche de l'ecran et reconverties dans le repere utilise par expyriment,
    c'est-a-dire dont l'origine est le centre de l'ecran. Convertit enfin ces
    images, pour lesquelles on precise les positions, en stimuli visuels.
    Retourne le stimulus audio, la liste des 3 stimuli visuels, le booleen False
    qui correspond a la presence d'une animation parmi ces stimulis (ici, ce
    n'est pas le cas, donc vaut False), le booleen False qui correspond a la
    presence d'une image au dessus des autres et qui ne sera pas cliquable (ici,
    ce n'est pas le cas, donc vaut False), l'entier 1 pour specifier que la
    presentation se fera en une seule fois.

    Arguments :
        audio : chaine de caracteres (nom du fichier audio)
        images : liste de 3 chaines de caracteres (noms des fichiers images)

    Retourne :
        Un stimulus audio
        Une liste de 3 stimuli visuels
        Un booleen (False : pas d'animation pour cet essai)
        Un booleen (False : pas d'image au dessus des autres pour cet essai)
        Un entier (1 : une seule presentation pour cet essai)
    """
    margin = round((screen_size[0]/100)*10)

    image1 = Image.open(images[0])
    image2 = Image.open(images[1])
    image3 = Image.open(images[2])

    w, h = image1.size
    box_size = (screen_size[0]-2*margin,screen_size[1])
    rest = (box_size[0]-3*w, box_size[1]-1*h) #attention ici 3
    gap = round(rest[0]/2) #attention ici 2

    stimuli = list()

    for i in range(3):
        p = _conversion_origin((round(margin+i*(w+gap)+w/2), round(screen_size[1]/2)))
        stim = expyriment.stimuli.Picture(images[i], position = p)
        stimuli.append(stim)
        TRIAL.add_stimulus(stim)

    BOXES.append(expyriment.io.TouchScreenButtonBox(stimuli))

    CARACTERISTICS.append((False, False, 1))
    """
    p1 = _conversion_origin((round(margin+0*(w+gap)+w/2), round(screen_size[1]/2)))
    p2 = _conversion_origin((round(margin+1*(w+gap)+w/2), round(screen_size[1]/2)))
    p3 = _conversion_origin((round(margin+2*(w+gap)+w/2), round(screen_size[1]/2)))

    stim1 = expyriment.stimuli.Picture(images[0], position = p1)
    stim2 = expyriment.stimuli.Picture(images[1], position = p2)
    stim3 = expyriment.stimuli.Picture(images[2], position = p3)
    """

# Squares

def _displaySquare(images, TRIAL):
    """Cree les stimulus et informations necessaires a la creation d'un essai
    qui consiste en la presentation de 4 images de maniere carree : un en haut a
    droite, un en haut a gauche, un en bas a doite, un en bas a gauche. Le
    'carre' est centre par rapport a l'ecran"

    Convertit le fichier audio en stimulus audio qui a pour but d'etre presente
    en meme temps que les 4 images. Utilise la classe Image pour avoir acces
    aux dimensions des images. A partir de ses dimensions et de marges decidees
    arbitrairement, calcule l'espace qui se trouvera entre chaque photo. Calcule
    ensuite les positions de chaque image dans un repere centre au coin bas
    gauche de l'ecran et reconverties dans le repere utilise par expyriment,
    c'est-a-dire dont l'origine est le centre de l'ecran. Convertit enfin ces
    images, pour lesquelles on precise les positions, en stimuli visuels.
    Retourne le stimulus audio et la liste des 4 stimuli visuels.

    Arguments :
        audio : chaine de caracteres (nom du fichier audio)
        images : liste de 4 chaines de caracteres (noms des fichiers images)

    Retourne :
        Un stimulus audio
        Une liste de 4 stimuli visuels
    """
    margin = round((screen_size[0]/100)*8)

    image1 = Image.open(images[0])
    image2 = Image.open(images[1])
    image3 = Image.open(images[2])
    image4 = Image.open(images[3])

    w, h = image1.size
    box_size = (screen_size[0]-2*margin,screen_size[1]-2*margin)
    rest = (box_size[0]-2*w, box_size[1]-2*h) #attention ici 2 et 2
    gap = round(rest[1]/1) #attention ici 1 et rest[1] !!

    stimuli = list()
    k = 0
    for i in [1, 0]:
        for j in [1, 0]:
            p = _conversion_origin((round(screen_size[0]/2 + (-1)**(j) * (gap/2 + w/2)), round(margin + i * (h+gap) + h/2)))
            print(p)
            stim = expyriment.stimuli.Picture(images[k], position = p)
            stimuli.append(stim)
            TRIAL.add_stimulus(stim)
            k+=1

    BOXES.append(expyriment.io.TouchScreenButtonBox(stimuli))


    p1 = _conversion_origin((round(screen_size[0]/2-gap/2-w/2), round(margin+(h+gap)+h/2)))
    p2 = _conversion_origin((round(screen_size[0]/2+gap/2+w/2), round(margin+(h+gap)+h/2)))
    p3 = _conversion_origin((round(screen_size[0]/2-gap/2-w/2), round(margin+h/2)))
    p4 = _conversion_origin((round(screen_size[0]/2+gap/2+w/2), round(margin+h/2)))

    print(p1, p2, p3, p4)
    """
    stim1 = expyriment.stimuli.Picture(images[0], position = p1)
    stim2 = expyriment.stimuli.Picture(images[1], position = p2)
    stim3 = expyriment.stimuli.Picture(images[2], position = p3)
    stim4 = expyriment.stimuli.Picture(images[3], position = p4)
    """

# One image on top, the others at the bottom

def display1top3bottom(images, TRIAL):
    """Cree les stimulus et informations necessaires a la creation d'un essai
    qui consiste en la presentation de 4 images tel que la premiere image est
    celle qui sera en haut de l'ecran (et ne sera pas cliquable) et les 3 autres
    sera disposees en dessous"

    Convertit le fichier audio en stimulus audio qui a pour but d'etre presente
    en meme temps que les 4 images. Utilise la classe Image pour avoir acces
    aux dimensions des images. A partir de ses dimensions et de marges decidees
    arbitrairement, calcule l'espace qui se trouvera entre chaque photo. Calcule
    ensuite les positions de chaque image dans un repere centre au coin bas
    gauche de l'ecran et reconverties dans le repere utilise par expyriment,
    c'est-a-dire dont l'origine est le centre de l'ecran. Convertit enfin ces
    images, pour lesquelles on precise les positions, en stimuli visuels.
    Retourne le stimulus audio, la liste des 4 stimuli visuels, le booleen False
    qui correspond a la presence d'une animation parmi ces stimulis (ici, ce
    n'est pas le cas, donc vaut False), le booleen True qui correspond a la
    presence d'une image au dessus des autres et qui ne sera pas cliquable (ici,
    c'est le cas, donc vaut True), l'entier 1 pour specifier que la presentation
    se fera en une seule fois.

    Arguments :
        audio : chaine de caracteres (nom du fichier audio)
        images : liste de 4 chaines de caracteres (noms des fichiers images)

    Retourne :
        Un stimulus audio
        Une liste de 4 stimuli visuels
        Un booleen (False : pas d'animation pour cet essai)
        Un booleen (True : une image au dessus des autres pour cet essai)
        Un entier (1 : une seule presentation pour cet essai)
    """
    [top, bottom] = images

    margin_w = round((screen_size[0]/100)*30)
    margin_h = round((screen_size[0]/100)*4)

    imageTop = Image.open(top)
    imageBot1 = Image.open(bottom[0])
    imageBot2 = Image.open(bottom[1])
    imageBot3 = Image.open(bottom[2])

    wTop, hTop = imageTop.size
    w, h = imageBot1.size
    box_size = (screen_size[0]-2*margin_w,screen_size[1]-2*margin_h)
    rest = (box_size[0]-3*w, box_size[1]-h-hTop) #attention ici 2 et 2
    gap_w = round(rest[0]/2) #attention ici 2
    gap_h = round(rest[1]/1)

    pTop = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    stimTop = expyriment.stimuli.Picture(top, position = pTop)
    TRIAL.add_stimulus(stimTop)

    stimuli = list()

    for i in range(3):
        p = _conversion_origin((round(screen_size[0]/2 + (i-1)*(gap_w/2 + w + w/2)), round(margin_h+h/2)))
        stim = expyriment.stimuli.Picture(bottom[i], position = p)
        stimuli.append(stim)
        TRIAL.add_stimulus(stim)

    BOXES.append(expyriment.io.TouchScreenButtonBox(stimuli, stimTop))

    CARACTERISTICS.append((False, True, 1))

    """
    p1 = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    p2 = _conversion_origin((round(screen_size[0]/2-gap_w/2-w-w/2), round(margin_h+h/2)))
    p3 = _conversion_origin((round(screen_size[0]/2), round(margin_h+h/2)))
    p4 = _conversion_origin((round(screen_size[0]/2+gap_w/2+w+w/2), round(margin_h+h/2)))

    stim1 = expyriment.stimuli.Picture(images[0], position = p1)
    stim2 = expyriment.stimuli.Picture(images[1], position = p2)
    stim3 = expyriment.stimuli.Picture(images[2], position = p3)
    stim4 = expyriment.stimuli.Picture(images[3], position = p4)
    """

def display1top4bottom(images, TRIAL):
    """Cree les stimulus et informations necessaires a la creation d'un essai
    qui consiste en la presentation de 5 images tel que la premiere image est
    celle qui sera en haut de l'ecran (et ne sera pas cliquable) et les 4 autres
    sera disposees en dessous"

    Convertit le fichier audio en stimulus audio qui a pour but d'etre presente
    en meme temps que les 5 images. Utilise la classe Image pour avoir acces
    aux dimensions des images. A partir de ses dimensions et de marges decidees
    arbitrairement, calcule l'espace qui se trouvera entre chaque photo. Calcule
    ensuite les positions de chaque image dans un repere centre au coin bas
    gauche de l'ecran et reconverties dans le repere utilise par expyriment,
    c'est-a-dire dont l'origine est le centre de l'ecran. Convertit enfin ces
    images, pour lesquelles on precise les positions, en stimuli visuels.
    Retourne le stimulus audio, la liste des 5 stimuli visuels, le booleen False
    qui correspond a la presence d'une animation parmi ces stimulis (ici, ce
    n'est pas le cas, donc vaut False), le booleen True qui correspond a la
    presence d'une image au dessus des autres et qui ne sera pas cliquable (ici,
    c'est le cas, donc vaut True), l'entier 1 pour specifier que la presentation
    se fera en une seule fois.

    Arguments :
        audio : chaine de caracteres (nom du fichier audio)
        images : liste de 5 chaines de caracteres (noms des fichiers images)

    Retourne :
        Un stimulus audio
        Une liste de 5 stimuli visuels
        Un booleen (False : pas d'animation pour cet essai)
        Un booleen (True : une image au dessus des autres pour cet essai)
        Un entier (1 : une seule presentation pour cet essai)
    """
    [top, bottom] = images

    margin_w = round((screen_size[0]/100)*5)
    margin_h = round((screen_size[0]/100)*4)

    imageTop = Image.open(top)
    imageBot1 = Image.open(bottom[0])
    imageBot2 = Image.open(bottom[1])
    imageBot3 = Image.open(bottom[2])
    imageBot4 = Image.open(bottom[3])

    wTop, hTop = imageTop.size
    w, h = imageBot1.size
    box_size = (screen_size[0]-2*margin_w,screen_size[1]-2*margin_h)
    rest = (box_size[0]-4*w, box_size[1]-h-hTop) #attention ici 3 et 1
    gap_w = round(rest[0]/3) #attention ici 3
    gap_h = round(rest[1]/1)

    pTop = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    stimTop = expyriment.stimuli.Picture(top[0], position = pTop)
    TRIAL.add_stimulus(stimTop)

    stimuli = list()

    for i in range(4):
        p = _conversion_origin((round(margin_w + i * (w+gap_w) + w/2), round(margin_h + h/2)))
        stim = expyriment.stimuli.Picture(bottom[i], position = p)
        stimuli.append(stim)
        TRIAL.add_stimulus(stim)

    BOXES.append(expyriment.io.TouchScreenButtonBox(stimuli, stimTop))

    CARACTERISTICS.append((False, True, 1))

    """
    p1 = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    p2 = _conversion_origin((round(margin_w+0*(w+gap_w)+w/2), round(margin_h+h/2)))
    p3 = _conversion_origin((round(margin_w+1*(w+gap_w)+w/2), round(margin_h+h/2)))
    p4 = _conversion_origin((round(margin_w+2*(w+gap_w)+w/2), round(margin_h+h/2)))
    p5 = _conversion_origin((round(margin_w+3*(w+gap_w)+w/2), round(margin_h+h/2)))

    stim1 = expyriment.stimuli.Picture(images[0], position = p1)
    stim2 = expyriment.stimuli.Picture(images[1], position = p2)
    stim3 = expyriment.stimuli.Picture(images[2], position = p3)
    stim4 = expyriment.stimuli.Picture(images[3], position = p4)
    stim5 = expyriment.stimuli.Picture(images[4], position = p5)
    """

## ---------- Images : two presentation per trial ----------

# With animation

def display1anim1image(images, TRIAL):
    [anim, image] = images
    stimAnim = expyriment.stimuli.Picture(anim)
    TRIAL.add_stimulus(stimAnim)
    stim = expyriment.stimuli.Picture(image)
    TRIAL.add_stimulus(stim)

    BOXES.append(expyriment.io.TouchScreenButtonBox(stim))

    CARACTERISTICS.append((True, False, 2))
    """
    stim1 = expyriment.stimuli.Picture(images[0])
    stim2 = expyriment.stimuli.Picture(images[1])
    return [stim1, stim2], True, False, 2"""

def display1anim1top3bottom(images, TRIAL):
    [anim, top, bottom] = images

    margin_w = round((screen_size[0]/100)*30)
    margin_h = round((screen_size[0]/100)*4)

    imageAnim = Image.open(anim)
    imageTop = Image.open(top)
    imageBot1 = Image.open(bottom[0])
    imageBot2 = Image.open(bottom[1])
    imageBot3 = Image.open(bottom[2])

    wTop, hTop = imageTop.size
    w, h = imageBot1.size
    box_size = (screen_size[0]-2*margin_w,screen_size[1]-2*margin_h)
    rest = (box_size[0]-3*w, box_size[1]-h-hTop) #attention ici 2 et 2
    gap_w = round(rest[0]/2) #attention ici 2
    gap_h = round(rest[1]/1)

    pAnim = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    stimAnim = expyriment.stimuli.Picture(anim, position = pAnim)
    TRIAL.add_stimulus(stimAnim)

    pTop = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    stimTop = expyriment.stimuli.Picture(top, position = pTop)
    TRIAL.add_stimulus(stimTop)

    stimuli = list()

    for i in range(3):
        p = _conversion_origin((round(screen_size[0]/2 + (i-1)*(gap_w/2 + w + w/2)), round(margin_h+h/2)))
        stim = expyriment.stimuli.Picture(bottom[i], position = p)
        stimuli.append(stim)
        TRIAL.add_stimulus(stim)

    BOXES.append(expyriment.io.TouchScreenButtonBox(stimuli, stimTop))

    CARACTERISTICS.append((True, True, 2))
    """
    pA = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    p1 = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    p2 = _conversion_origin((round(screen_size[0]/2-gap_w/2-w-w/2), round(margin_h+h/2)))
    p3 = _conversion_origin((round(screen_size[0]/2), round(margin_h+h/2)))
    p4 = _conversion_origin((round(screen_size[0]/2+gap_w/2+w+w/2), round(margin_h+h/2)))

    stimA = expyriment.stimuli.Picture(images[0], position = pA)
    stim1 = expyriment.stimuli.Picture(images[1], position = p1)
    stim2 = expyriment.stimuli.Picture(images[2], position = p2)
    stim3 = expyriment.stimuli.Picture(images[3], position = p3)
    stim4 = expyriment.stimuli.Picture(images[4], position = p4)

    return [stimA, stim1, stim2, stim3, stim4], True, True, 2"""

def display1anim1top4bottom(images, TRIAL):
    [anim, top, bottom] = images

    margin_w = round((screen_size[0]/100)*2)
    margin_h = round((screen_size[0]/100)*2)

    imageAnim = Image.open(anim)
    imageTop = Image.open(top)
    imageBot1 = Image.open(bottom[0])
    imageBot2 = Image.open(bottom[1])
    imageBot3 = Image.open(bottom[2])
    imageBot4 = Image.open(bottom[3])

    wTop, hTop = imageTop.size
    w, h = imageBot1.size
    box_size = (screen_size[0]-2*margin_w,screen_size[1]-2*margin_h)
    rest = (box_size[0]-4*w, box_size[1]-h-hTop) #attention ici 3 et 1
    gap_w = round(rest[0]/3) #attention ici 3
    gap_h = round(rest[1]/1)

    pAnim = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    stimAnim = expyriment.stimuli.Picture(anim, position = pAnim)
    TRIAL.add_stimulus(stimAnim)

    pTop = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    stimTop = expyriment.stimuli.Picture(top, position = pTop)
    TRIAL.add_stimulus(stimTop)

    stimuli = list()

    for i in range(4):
        p = _conversion_origin((round(margin_w + i * (w+gap_w) + w/2), round(margin_h + h/2)))
        stim = expyriment.stimuli.Picture(bottom[i], position = p)
        stimuli.append(stim)
        TRIAL.add_stimulus(stim)

    BOXES.append(expyriment.io.TouchScreenButtonBox(stimuli, stimTop))

    CARACTERISTICS.append((True, True, 2))
    """
    pA = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    p1 = _conversion_origin((round(screen_size[0]/2), round(margin_h+h+gap_h+hTop/2)))
    p2 = _conversion_origin((round(margin_w+0*(w+gap_w)+w/2), round(margin_h+h/2)))
    p3 = _conversion_origin((round(margin_w+1*(w+gap_w)+w/2), round(margin_h+h/2)))
    p4 = _conversion_origin((round(margin_w+2*(w+gap_w)+w/2), round(margin_h+h/2)))
    p5 = _conversion_origin((round(margin_w+3*(w+gap_w)+w/2), round(margin_h+h/2)))

    stimA = expyriment.stimuli.Picture(images[0], position = pA)
    stim1 = expyriment.stimuli.Picture(images[1], position = p1)
    stim2 = expyriment.stimuli.Picture(images[2], position = p2)
    stim3 = expyriment.stimuli.Picture(images[3], position = p3)
    stim4 = expyriment.stimuli.Picture(images[4], position = p4)
    stim5 = expyriment.stimuli.Picture(images[5], position = p5)

    return [stimA, stim1, stim2, stim3, stim4, stim5], True, True, 2"""

# Without animation

def displaySquareTwice(images, TRIAL):
    _displaySquare(images[0:4], TRIAL)
    _displaySquare(images[4:], TRIAL)
    CARACTERISTICS.append((False, False, 2))

def display1top3bottomTwice(images, TRIAL):
    display1top3bottom(images[0:2], TRIAL)
    display1top3bottom(images[2:], TRIAL)
    CARACTERISTICS.pop()
    CARACTERISTICS.pop()
    CARACTERISTICS.append((False, True, 2))


## ---------- Videos : transitions between blocks ----------

def displayVideo(video):
    video = expyriment.stimuli.Video(os.path.join("videos", video))
    video.preload()
    return video

## ---------- Audio : during the trials ----------

def displayAudio(audio, TRIAL):
    if isinstance(audio, list):
        for a in audio:
            stimAudio = expyriment.stimuli.Audio(os.path.join("sounds", a))
            TRIAL.add_stimulus(stimAudio)
    else:
        stimAudio = expyriment.stimuli.Audio(os.path.join("sounds", audio))
        TRIAL.add_stimulus(stimAudio)

### ----- VARIABLES -----

carre = 'degas-carre-petit.jpg'
rectangle = 'degas-rectangle.jpg'
portrait = 'degas-portrait.jpg'
son = '1.wav'
video = 'Flower.mp4'

CARACTERISTICS = list()
BOXES = list()
TRANSITIONS = list()

list_of_stimulus = list()

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

list_of_lengths = [3, 5, 4, 4, 3, 2, 4, 3, 5, 5, 5, 5, 3]

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
                        [carre, carre, carre, carre, carre, carre, carre, carre],
                        [portrait, portrait, portrait],
                        [carre, [carre, carre, carre], carre, [carre, carre, carre]],
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
                    [1, 1, 3]]

#----- TRAINING : BLOCK 0 -----

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

#----- TEST : BLOCK 1 TO 12 -----

for b in range(1,13):
    block = expyriment.design.Block(name=list_of_blocks[b])
    for t in range(list_of_lengths[b]):
        trial = expyriment.design.Trial()
        displayAudio(list_of_sounds[b], trial)
        list_of_functions[b](list_of_images[b], trial)
        block.add_trial(trial)
    exp.add_block(block)

#----- TRANSITIONS : VIDEO -----

for t in list_of_transitions:
    transition = displayVideo(t)
    TRANSITIONS.append(transition)

#----- ITERATORS -----
answers = iter(list_of_answers)
cara = iter(CARACTERISTICS)
box = iter(BOXES)
tran = iter(TRANSITIONS)


#---------- MAIN ----------
def save_data(block, trial, img, anim, top, nb, answer):
    a = next(answer)
    for i in range(len(trial.stimuli)):
        if img == trial.stimuli[i]:
            response = i - top - anim - nb + 1
            if response >= 5:
                response-=4
            exp.data.add([block.name, trial.id, response, a == response])

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
            trial.stimuli[0].play()
            b.show()
            expyriment.control.wait_end_audiosystem()
            img, resptime = b.wait()
            save_data(block, trial, img, anim, top, nb, answer)

        elif anim and nb == 2:
            trial.stimuli[0].play()
            trial.stimuli[2].present()
            expyriment.control.wait_end_audiosystem()
            exp.clock.wait(1000)
            exp.screen.clear()
            exp.screen.update()
            trial.stimuli[1].play()
            b.show()
            expyriment.control.wait_end_audiosystem()
            img, resptime = b.wait()
            save_data(block, trial, img, anim, top, nb, answer)

        else:
            trial.stimuli[0].play()
            b.show()
            expyriment.control.wait_end_audiosystem()
            img1, resptime = b.wait()
            exp.screen.clear()
            exp.screen.update()
            exp.clock.wait(1000)
            trial.stimuli[1].play()
            b = next(box)
            b.show()
            expyriment.control.wait_end_audiosystem()
            img2, resptime = b.wait()
            save_data(block, trial, img1, anim, top, nb, answer)
            save_data(block, trial, img2, anim, top, nb, answer)

        exp.screen.clear()
        exp.screen.update()
        exp.clock.wait(1000)

    exp.screen.clear()
    exp.screen.update()
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

expyriment.misc.data_preprocessing.write_concatenated_data(data_folder = 'data', file_name = 'VocabularyTest', output_file = 'results.csv' )
