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

    margin = round((screen_size[0]/100))

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

    box = expyriment.io.TouchScreenButtonBox([stim1, stim2, stim3, stim4])
    box.create()

    return box, sound

def displayLine3Images(images, audio, window_size = screen.window_size):
    sound = expyriment.stimuli.Audio(os.path.join("sounds", audio))

    margin = round((screen_size[0]/100)*10)

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

    box = expyriment.io.TouchScreenButtonBox([stim1, stim2, stim3]) #attention ici 3 stims
    box.create()

    return box, sound

#box, sound = displayLine4Images(["degas-portrait.jpg","degas-portrait.jpg","degas-portrait.jpg","degas-portrait.jpg"],"1.wav")
box, sound = displayLine3Images(["degas-portrait.jpg","degas-portrait.jpg","degas-portrait.jpg"],"1.wav")

expyriment.control.start()
sound.play()
box.show()
expyriment.control.wait_end_audiosystem()
img, resptime = box.wait()
expyriment.control.end()
