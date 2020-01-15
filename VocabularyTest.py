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

def displayLine4Images(audio, images, window_size = screen.window_size):
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

    return sound, [stim1, stim2, stim3, stim4], False, False, 1

def displayLine3Images(audio, images, window_size = screen.window_size):
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

    return sound, [stim1, stim2, stim3], False, False, 1

def _displaySquare(audio, images, window_size = screen.window_size):
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

def display1top3bottom(audio, images, window_size = screen.window_size):
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

    return sound, [stim1, stim2, stim3, stim4], False, True, 1

def display1top4bottom(audio, images, window_size = screen.window_size):
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

    return sound, [stim1, stim2, stim3, stim4, stim5], False, True, 1

def display1anim1image(audio, images, window_size = screen.window_size):
    sound1 = expyriment.stimuli.Audio(os.path.join("sounds", audio[0]))
    sound2 = expyriment.stimuli.Audio(os.path.join("sounds", audio[1]))
    stim1 = expyriment.stimuli.Picture(images[0])
    stim2 = expyriment.stimuli.Picture(images[1])
    return [sound1, sound2], [stim1, stim2], True, False, 2

def display1anim1top3bottom(audio, images, window_size = screen.window_size):
    sound1 = expyriment.stimuli.Audio(os.path.join("sounds", audio[0]))
    sound2 = expyriment.stimuli.Audio(os.path.join("sounds", audio[1]))

    margin_w = round((window_size[0]/100)*30)
    margin_h = round((window_size[0]/100)*4)

    imageA = Image.open(images[0])
    image1 = Image.open(images[1])
    image2 = Image.open(images[2])
    image3 = Image.open(images[3])
    image4 = Image.open(images[4])

    w1, h1 = image1.size
    w, h = image2.size
    box_size = (window_size[0]-2*margin_w,window_size[1]-2*margin_h)
    rest = (box_size[0]-3*w, box_size[1]-h-h1) #attention ici 2 et 2
    gap_w = round(rest[0]/2) #attention ici 2
    gap_h = round(rest[1]/1)

    pA = _conversion_origin((round(window_size[0]/2), round(margin_h+h+gap_h+h1/2)))
    p1 = _conversion_origin((round(window_size[0]/2), round(margin_h+h+gap_h+h1/2)))
    p2 = _conversion_origin((round(window_size[0]/2-gap_w/2-w-w/2), round(margin_h+h/2)))
    p3 = _conversion_origin((round(window_size[0]/2), round(margin_h+h/2)))
    p4 = _conversion_origin((round(window_size[0]/2+gap_w/2+w+w/2), round(margin_h+h/2)))

    stimA = expyriment.stimuli.Picture(images[0], position = pA)
    stim1 = expyriment.stimuli.Picture(images[1], position = p1)
    stim2 = expyriment.stimuli.Picture(images[2], position = p2)
    stim3 = expyriment.stimuli.Picture(images[3], position = p3)
    stim4 = expyriment.stimuli.Picture(images[4], position = p4)

    return [sound1, sound2], [stimA, stim1, stim2, stim3, stim4], True, True, 2

def display1anim1top4bottom(audio, images, window_size = screen.window_size):
    sound1 = expyriment.stimuli.Audio(os.path.join("sounds", audio[0]))
    sound2 = expyriment.stimuli.Audio(os.path.join("sounds", audio[1]))

    margin_w = round((window_size[0]/100)*2)
    margin_h = round((window_size[0]/100)*2)

    imageA = Image.open(images[0])
    image1 = Image.open(images[1])
    image2 = Image.open(images[2])
    image3 = Image.open(images[3])
    image4 = Image.open(images[4])
    image5 = Image.open(images[5])

    w1, h1 = image1.size
    w, h = image2.size
    box_size = (window_size[0]-2*margin_w,window_size[1]-2*margin_h)
    rest = (box_size[0]-4*w, box_size[1]-h-h1) #attention ici 3 et 1
    gap_w = round(rest[0]/3) #attention ici 3
    gap_h = round(rest[1]/1)

    pA = _conversion_origin((round(window_size[0]/2), round(margin_h+h+gap_h+h1/2)))
    p1 = _conversion_origin((round(window_size[0]/2), round(margin_h+h+gap_h+h1/2)))
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

    return [sound1, sound2], [stimA, stim1, stim2, stim3, stim4, stim5], True, True, 2

def displaySquareTwice(audio, images, window_size = screen.window_size):
    sound1, [stim1, stim2, stim3, stim4] = _displaySquare(audio[0], images[0:4])
    sound2, [stim5, stim6, stim7, stim8] = _displaySquare(audio[1], images[4:])

    return [sound1, sound2], [stim1, stim2, stim3, stim4, stim5, stim6, stim7, stim8], False, False, 2

def display1top3bottomTwice(audio, images, window_size = screen.window_size):
    sound1, [stim1, stim2, stim3, stim4], anim, top, nb = display1top3bottom(audio[0], images[0:4])
    sound2, [stim5, stim6, stim7, stim8], anim, top, nb = display1top3bottom(audio[1], images[4:])

    return [sound1, sound2], [stim1, stim2, stim3, stim4, stim5, stim6, stim7, stim8], False, True, 2

def createBox(stims, anim, top, nb):

    if nb == 1:
        if top:
            box1 = expyriment.io.TouchScreenButtonBox(stims[1:], stims[0])
        else:
            box1 = expyriment.io.TouchScreenButtonBox(stims)
        box2 = None
    else:
        if anim:
            if top:
                box1 = expyriment.io.TouchScreenButtonBox(stims[2:], stims[1])
            else:
                box1 = expyriment.io.TouchScreenButtonBox(stims[1:], stims[0])
            box2 = None
        else:
            if top:
                box1 = expyriment.io.TouchScreenButtonBox(stims[1:4], stims[0])
                box2 = expyriment.io.TouchScreenButtonBox(stims[5:], stims[4])
            else:
                box1 = expyriment.io.TouchScreenButtonBox(stims[:4])
                box2 = expyriment.io.TouchScreenButtonBox(stims[4:])

    box1.create()
    if box2:
        box2.create()

    return anim, top, nb, box1, box2

def displayVideo(video, window_size = screen.window_size):
    video = expyriment.stimuli.Video(os.path.join("videos", video))
    video.preload()

    return video

carre = 'degas-carre-petit.jpg'
rectangle = 'degas-rectangle.jpg'
portrait = 'degas-portrait.jpg'
son = '1.wav'
video = 'Flower.mp4'
boxes = list()
transitions = list()

list_of_stimulus = list()

list_of_blocks = ["PRACTISE", "WH-QUESTIONS", "PAST TENSE", "VERB LEARNING", "PREPOSITIONAL PHRASES", "CONVERTING ACTIVE TO PASSIVE", "EMBEDED CLAUSES", "NOUNS", "VERBS", "NOUN LEARNING", "PREPOSITIONS", "ADJECTIVE LEARNING", "CONJUNCTIONS"]

list_of_lengths = [3, 5, 4, 4, 3, 2, 4, 3, 5, 5, 5, 5, 3]

list_of_fonctions = [[displayLine4Images, displayLine3Images, display1top3bottom],
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

list_of_images = [[[carre, carre, carre, carre], [carre, carre, carre], [rectangle, carre, carre, carre]],
                        [rectangle, carre, carre, carre],
                        [rectangle, rectangle],
                        [rectangle, rectangle, carre, carre, carre],
                        [carre, carre, carre],
                        [rectangle, rectangle, carre, carre, carre],
                        [rectangle, rectangle, carre, carre, carre, carre],
                        [carre, carre, carre, carre],
                        [carre, carre, carre],
                        [carre, carre, carre, carre, carre, carre, carre, carre],
                        [portrait, portrait, portrait],
                        [carre, carre, carre, carre, carre, carre, carre, carre],
                        [rectangle, carre, carre, carre]]

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
functions0 = list_of_fonctions[0]
images0 = list_of_images[0]
sounds0 = list_of_sounds[0]

block0 = expyriment.design.Block(name=name0)

for t in range(length0):
    trial0 = expyriment.design.Trial()
    audio0, stim0, anim0, top0, nb0 = functions0[t](sounds0[t], images0[t])
    trial0.add_stimulus(audio0)
    for stim in stim0:
        trial0.add_stimulus(stim)
    anim0, top0, nb0, box10, box20 = createBox(stim0, anim0, top0, nb0)
    block0.add_trial(trial0)
    boxes.append([anim0, top0, nb0, box10, box20])
exp.add_block(block0)

#----- TEST : BLOCK 1 TO 12 -----

for b in range(1,13):
    block = expyriment.design.Block(name=list_of_blocks[b])
    for t in range(list_of_lengths[b]):
        trial = expyriment.design.Trial()
        audio, stimulus, anim, top, nb = list_of_fonctions[b](list_of_sounds[b], list_of_images[b])
        if isinstance(audio, list):
            for a in audio:
                trial.add_stimulus(a)
        else:
            trial.add_stimulus(audio)
        for s in stimulus:
            trial.add_stimulus(s)
        anim, top, nb, box1, box2 = createBox(stimulus, anim, top, nb)
        block.add_trial(trial)
        boxes.append([anim, top, nb, box1, box2])
    exp.add_block(block)

#----- TRANSITIONS : VIDEO -----

for t in list_of_transitions:
    transition = displayVideo(t)
    transitions.append(transition)

#----- ITERATORS -----

box = iter(boxes)
tran = iter(transitions)


#---------- MAIN ----------
def save_data(block_name, trial_id, trial_stim, img, anim, top, nb):
    for i in range(len(trial_stim)):
        if img == trial_stim[i]:
            response = i - top - anim - nb + 1
            if response >= 5:
                response-=4
            exp.data.add([block_name, trial_id, response])

exp.add_data_variable_names(['block', 'trial', 'response'])

expyriment.control.start()

for block in exp.blocks:

    t = next(tran)

    for trial in block.trials:

        b = next(box)
        anim = b[0]
        top = b[1]
        nb = b[2]
        box1 = b[3]
        box2 = b[4]

        if not anim and not box2:
            trial.stimuli[0].play()
            box1.show()
            expyriment.control.wait_end_audiosystem()
            img, resptime = box1.wait()
            save_data(block.name, trial.id, trial.stimuli, img, anim, top, nb)

        elif anim and not box2:
            trial.stimuli[0].play()
            trial.stimuli[2].present()
            expyriment.control.wait_end_audiosystem()
            exp.clock.wait(1000)
            exp.screen.clear()
            exp.screen.update()
            trial.stimuli[1].play()
            box1.show()
            expyriment.control.wait_end_audiosystem()
            img, resptime = box1.wait()
            save_data(block.name, trial.id, trial.stimuli, img, anim, top, nb)

        else:
            trial.stimuli[0].play()
            box1.show()
            expyriment.control.wait_end_audiosystem()
            img1, resptime = box1.wait()
            exp.screen.clear()
            exp.screen.update()
            exp.clock.wait(1000)
            trial.stimuli[1].play()
            box2.show()
            expyriment.control.wait_end_audiosystem()
            img2, resptime = box2.wait()
            save_data(block.name, trial.id, trial.stimuli, img1, anim, top, nb)
            save_data(block.name, trial.id, trial.stimuli, img2, anim, top, nb)

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
