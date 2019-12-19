import expyriment
from PIL import Image
import os.path

exp = expyriment.design.Experiment(name="QUILS-Prototype")
expyriment.control.set_develop_mode(on=True) #permet de ne pas enregistrer les donnees pour le moment, parce que je suis encore en train de faire des modifications
expyriment.control.defaults.window_mode = False #empeche d'etre en petite fenetre, je veux que ce soit en plein ecran

expyriment.control.initialize(exp)
mouse = expyriment.io.Mouse(show_cursor=True)
screen = exp.screen
window_size = screen.window_size
screen_size = screen.size
center_x = exp.screen.center_x
center_y = exp.screen.center_y

def _conversion_origin(position, window_size = screen.window_size):
    x = position[0]-round(window_size[0]/2)
    y = position[1]-round(window_size[1]/2)
    return (x,y)

def displayLine4Images(images, audio, window_size = screen.window_size):
    sound = expyriment.stimuli.Audio(os.path.join("sounds", audio))

    margin = round((window_size[0]/100))

    image1 = Image.open(images[0])
    image2 = Image.open(images[1])
    image3 = Image.open(images[2])
    image4 = Image.open(images[3])

    w, h = image1.size
    box_size = (window_size[0]-2*margin,window_size[1])
    rest = (box_size[0]-4*w, box_size[1]-1*h) #attention ici 4
    gap = round(rest[0]/3) #attention ici 3

    p1 = _conversion_origin((round(margin+0*(w+gap)+w/2), round(window_size[1]/2)))
    p2 = _conversion_origin((round(margin+1*(w+gap)+w/2), round(window_size[1]/2)))
    p3 = _conversion_origin((round(margin+2*(w+gap)+w/2), round(window_size[1]/2)))
    p4 = _conversion_origin((round(margin+3*(w+gap)+w/2), round(window_size[1]/2)))

    stim1 = expyriment.stimuli.Picture(images[0], position = p1)
    stim2 = expyriment.stimuli.Picture(images[1], position = p2)
    stim3 = expyriment.stimuli.Picture(images[2], position = p3)
    stim4 = expyriment.stimuli.Picture(images[3], position = p4)

    return sound, [stim1, stim2, stim3, stim4]

def displayLine3Images(images, audio, window_size = screen.window_size):
    sound = expyriment.stimuli.Audio(os.path.join("sounds", audio))

    margin = round((window_size[0]/100)*10)

    image1 = Image.open(images[0])
    image2 = Image.open(images[1])
    image3 = Image.open(images[2])

    w, h = image1.size
    box_size = (window_size[0]-2*margin,window_size[1])
    rest = (box_size[0]-3*w, box_size[1]-1*h) #attention ici 3
    gap = round(rest[0]/2) #attention ici 2

    p1 = _conversion_origin((round(margin+0*(w+gap)+w/2), round(window_size[1]/2)))
    p2 = _conversion_origin((round(margin+1*(w+gap)+w/2), round(window_size[1]/2)))
    p3 = _conversion_origin((round(margin+2*(w+gap)+w/2), round(window_size[1]/2)))

    stim1 = expyriment.stimuli.Picture(images[0], position = p1)
    stim2 = expyriment.stimuli.Picture(images[1], position = p2)
    stim3 = expyriment.stimuli.Picture(images[2], position = p3)

    return sound, [stim1, stim2, stim3]

def displaySquare(images, audio, window_size = screen.window_size):
    sound = expyriment.stimuli.Audio(os.path.join("sounds", audio))

    margin = round((window_size[0]/100)*8)

    image1 = Image.open(images[0])
    image2 = Image.open(images[1])
    image3 = Image.open(images[2])
    image4 = Image.open(images[3])

    w, h = image1.size
    box_size = (window_size[0]-2*margin,window_size[1]-2*margin)
    rest = (box_size[0]-2*w, box_size[1]-2*h) #attention ici 2 et 2
    gap = round(rest[1]/1) #attention ici 1 et rest[1] !!

    p1 = _conversion_origin((round(window_size[0]/2-gap/2-w/2), round(margin+(h+gap)+h/2)))
    p2 = _conversion_origin((round(window_size[0]/2+gap/2+w/2), round(margin+(h+gap)+h/2)))
    p3 = _conversion_origin((round(window_size[0]/2-gap/2-w/2), round(margin+h/2)))
    p4 = _conversion_origin((round(window_size[0]/2+gap/2+w/2), round(margin+h/2)))

    stim1 = expyriment.stimuli.Picture(images[0], position = p1)
    stim2 = expyriment.stimuli.Picture(images[1], position = p2)
    stim3 = expyriment.stimuli.Picture(images[2], position = p3)
    stim4 = expyriment.stimuli.Picture(images[3], position = p4)

    return sound, [stim1, stim2, stim3, stim4]

def display1top3bottom(images, audio, window_size = screen.window_size):
    sound = expyriment.stimuli.Audio(os.path.join("sounds", audio))

    margin_w = round((window_size[0]/100)*30)
    margin_h = round((window_size[0]/100)*4)

    image1 = Image.open(images[0])
    image2 = Image.open(images[1])
    image3 = Image.open(images[2])
    image4 = Image.open(images[3])

    w1, h1 = image1.size
    w, h = image2.size
    box_size = (window_size[0]-2*margin_w,window_size[1]-2*margin_h)
    rest = (box_size[0]-3*w, box_size[1]-h-h1) #attention ici 2 et 2
    gap_w = round(rest[0]/2) #attention ici 2
    gap_h = round(rest[1]/1)

    p1 = _conversion_origin((round(window_size[0]/2), round(margin_h+h+gap_h+h1/2)))
    p2 = _conversion_origin((round(window_size[0]/2-gap_w/2-w-w/2), round(margin_h+h/2)))
    p3 = _conversion_origin((round(window_size[0]/2), round(margin_h+h/2)))
    p4 = _conversion_origin((round(window_size[0]/2+gap_w/2+w+w/2), round(margin_h+h/2)))

    stim1 = expyriment.stimuli.Picture(images[0], position = p1)
    stim2 = expyriment.stimuli.Picture(images[1], position = p2)
    stim3 = expyriment.stimuli.Picture(images[2], position = p3)
    stim4 = expyriment.stimuli.Picture(images[3], position = p4)

    return sound, [stim1, stim2, stim3, stim4]

def display1top4bottom(images, audio, window_size = screen.window_size):
    sound = expyriment.stimuli.Audio(os.path.join("sounds", audio))

    margin_w = round((window_size[0]/100)*5)
    margin_h = round((window_size[0]/100)*4)

    image1 = Image.open(images[0])
    image2 = Image.open(images[1])
    image3 = Image.open(images[2])
    image4 = Image.open(images[3])
    image5 = Image.open(images[4])

    w1, h1 = image1.size
    w, h = image2.size
    box_size = (window_size[0]-2*margin_w,window_size[1]-2*margin_h)
    rest = (box_size[0]-4*w, box_size[1]-h-h1) #attention ici 3 et 1
    gap_w = round(rest[0]/3) #attention ici 3
    gap_h = round(rest[1]/1)

    p1 = _conversion_origin((round(window_size[0]/2), round(margin_h+h+gap_h+h1/2)))
    p2 = _conversion_origin((round(margin_w+0*(w+gap_w)+w/2), round(margin_h+h/2)))
    p3 = _conversion_origin((round(margin_w+1*(w+gap_w)+w/2), round(margin_h+h/2)))
    p4 = _conversion_origin((round(margin_w+2*(w+gap_w)+w/2), round(margin_h+h/2)))
    p5 = _conversion_origin((round(margin_w+3*(w+gap_w)+w/2), round(margin_h+h/2)))

    stim1 = expyriment.stimuli.Picture(images[0], position = p1)
    stim2 = expyriment.stimuli.Picture(images[1], position = p2)
    stim3 = expyriment.stimuli.Picture(images[2], position = p3)
    stim4 = expyriment.stimuli.Picture(images[3], position = p4)
    stim5 = expyriment.stimuli.Picture(images[4], position = p5)

    return sound, [stim1, stim2, stim3, stim4, stim5]

def createBox(stims, top=False):
    if not top:
        box = expyriment.io.TouchScreenButtonBox(stims)
    else:
        box = expyriment.io.TouchScreenButtonBox(stims[1:], stims[0])
    box.create()
    return box

def displayVideo(video, window_size = screen.window_size):
    video = expyriment.stimuli.Video(os.path.join("videos", video))
    video.preload()

    return video

carre = 'degas-carre-petit.jpg'
rectangle = 'degas-rectangle.jpg'
portrait = 'degas-portrait.jpg'
son = '1.wav'
boxes = list()

bloc_0 = expyriment.design.Block(name="Entraînement")

essai_0_1 = expyriment.design.Trial()
audio_0_1, stim_0_1= displayLine4Images([carre, carre, carre,carre],son)
essai_0_1.add_stimulus(audio_0_1)
for stim in stim_0_1:
    essai_0_1.add_stimulus(stim)
box_0_1 = createBox(stim_0_1)
bloc_0.add_trial(essai_0_1)

essai_0_2 = expyriment.design.Trial()
audio_0_2, stim_0_2 = displayLine3Images([carre, carre, carre],son)
essai_0_2.add_stimulus(audio_0_2)
for stim in stim_0_2:
    essai_0_2.add_stimulus(stim)
box_0_2 = createBox(stim_0_2)
bloc_0.add_trial(essai_0_2)

essai_0_3 = expyriment.design.Trial()
audio_0_3, stim_0_3 = display1top3bottom([rectangle, carre, carre, carre],son)
essai_0_3.add_stimulus(audio_0_3)
for stim in stim_0_3:
    essai_0_3.add_stimulus(stim)
box_0_3 = createBox(stim_0_3, top=True)
bloc_0.add_trial(essai_0_3)

boxes.append(box_0_1)
boxes.append(box_0_2)
boxes.append(box_0_3)

box = iter(boxes)

exp.add_block(bloc_0)
"""
bloc_1 = expyriment.design.Block(name="Questions")
essai_1_1 = expyriment.design.Trial()
bloc_1.add_trial(essai_1_1)
essai_1_2 = expyriment.design.Trial()
bloc_1.add_trial(essai_1_2)
essai_1_3 = expyriment.design.Trial()
bloc_1.add_trial(essai_1_3)
essai_1_4 = expyriment.design.Trial()
bloc_1.add_trial(essai_1_4)
essai_1_5 = expyriment.design.Trial()
bloc_1.add_trial(essai_1_5)
exp.add_block(bloc_1)

bloc_2 = expyriment.design.Block(name="Passé")
essai_2_1 = expyriment.design.Trial()
bloc_2.add_trial(essai_2_1)
essai_2_2 = expyriment.design.Trial()
bloc_2.add_trial(essai_2_2)
essai_2_3 = expyriment.design.Trial()
bloc_2.add_trial(essai_2_3)
essai_2_4 = expyriment.design.Trial()
bloc_2.add_trial(essai_2_4)
exp.add_block(bloc_2)

bloc_3 = expyriment.design.Block(name="Apprentissage de verbes")
essai_3_1 = expyriment.design.Trial()
bloc_3.add_trial(essai_3_1)
essai_3_2 = expyriment.design.Trial()
bloc_3.add_trial(essai_3_2)
essai_3_3 = expyriment.design.Trial()
bloc_3.add_trial(essai_3_3)
essai_3_4 = expyriment.design.Trial()
bloc_3.add_trial(essai_3_4)
exp.add_block(bloc_3)

bloc_4 = expyriment.design.Block(name="Prépositions")
essai_4_1 = expyriment.design.Trial()
bloc_4.add_trial(essai_4_1)
essai_4_2 = expyriment.design.Trial()
bloc_4.add_trial(essai_4_2)
essai_4_3 = expyriment.design.Trial()
bloc_4.add_trial(essai_4_3)
exp.add_block(bloc_4)

bloc_5 = expyriment.design.Block(name="Conversion Actif-Passif")
essai_5_1 = expyriment.design.Trial()
bloc_5.add_trial(essai_5_1)
essai_5_2 = expyriment.design.Trial()
bloc_5.add_trial(essai_5_2)
exp.add_block(bloc_5)

bloc_6 = expyriment.design.Block(name="Clauses enclavées")
essai_6_1 = expyriment.design.Trial()
bloc_6.add_trial(essai_6_1)
essai_6_2 = expyriment.design.Trial()
bloc_6.add_trial(essai_6_2)
essai_6_3 = expyriment.design.Trial()
bloc_6.add_trial(essai_6_3)
essai_6_4 = expyriment.design.Trial()
bloc_6.add_trial(essai_6_4)
exp.add_block(bloc_6)

bloc_7 = expyriment.design.Block(name="Noms")
essai_7_1 = expyriment.design.Trial()
bloc_7.add_trial(essai_7_1)
essai_7_2 = expyriment.design.Trial()
bloc_7.add_trial(essai_7_2)
essai_7_3 = expyriment.design.Trial()
bloc_7.add_trial(essai_7_3)
exp.add_block(bloc_7)

bloc_8 = expyriment.design.Block(name="Verbes")
essai_8_1 = expyriment.design.Trial()
bloc_8.add_trial(essai_8_1)
essai_8_2 = expyriment.design.Trial()
bloc_8.add_trial(essai_8_2)
essai_8_3 = expyriment.design.Trial()
bloc_8.add_trial(essai_8_3)
essai_8_4 = expyriment.design.Trial()
bloc_8.add_trial(essai_8_4)
essai_8_5 = expyriment.design.Trial()
bloc_8.add_trial(essai_8_5)
exp.add_block(bloc_8)

bloc_9 = expyriment.design.Block(name="Apprentissage de noms")
essai_9_1 = expyriment.design.Trial()
bloc_9.add_trial(essai_9_1)
essai_9_2 = expyriment.design.Trial()
bloc_9.add_trial(essai_9_2)
essai_9_3 = expyriment.design.Trial()
bloc_9.add_trial(essai_9_3)
essai_9_4 = expyriment.design.Trial()
bloc_9.add_trial(essai_9_4)
essai_9_5 = expyriment.design.Trial()
bloc_9.add_trial(essai_9_5)
exp.add_block(bloc_9)

bloc_10 = expyriment.design.Block(name="Prépositions")
essai_10_1 = expyriment.design.Trial()
bloc_10.add_trial(essai_10_1)
essai_10_2 = expyriment.design.Trial()
bloc_10.add_trial(essai_10_2)
essai_10_3 = expyriment.design.Trial()
bloc_10.add_trial(essai_10_3)
essai_10_4 = expyriment.design.Trial()
bloc_10.add_trial(essai_10_4)
essai_10_5 = expyriment.design.Trial()
bloc_10.add_trial(essai_10_5)
exp.add_block(bloc_10)

bloc_11 = expyriment.design.Block(name="Apprentissage d'adjectifs")
essai_11_1 = expyriment.design.Trial()
bloc_11.add_trial(essai_11_1)
essai_11_2 = expyriment.design.Trial()
bloc_11.add_trial(essai_11_2)
essai_11_3 = expyriment.design.Trial()
bloc_11.add_trial(essai_11_3)
essai_11_4 = expyriment.design.Trial()
bloc_11.add_trial(essai_11_4)
essai_11_5 = expyriment.design.Trial()
bloc_11.add_trial(essai_11_5)
exp.add_block(bloc_11)

bloc_12 = expyriment.design.Block(name="Conjonctions")
essai_12_1 = expyriment.design.Trial()
bloc_12.add_trial(essai_12_1)
essai_12_2 = expyriment.design.Trial()
bloc_12.add_trial(essai_12_2)
essai_12_3 = expyriment.design.Trial()
bloc_12.add_trial(essai_12_3)
exp.add_block(bloc_12)
"""
expyriment.control.start()

for block in exp.blocks:
    for trial in block.trials:
        trial.stimuli[0].play()
        b = next(box)
        b.show()
        expyriment.control.wait_end_audiosystem()
        img, resptime = b.wait()
        exp.screen.clear()
        exp.screen.update()
        exp.clock.wait(1000)
expyriment.control.end()
