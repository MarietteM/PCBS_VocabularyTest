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

#sound, stim = displayLine4Images(["degas-portrait.jpg","degas-portrait.jpg","degas-portrait.jpg","degas-portrait.jpg"],"1.wav")
#sound, stim = displayLine3Images(["degas-portrait.jpg","degas-portrait.jpg","degas-portrait.jpg"],"1.wav")
#sound, stim = displaySquare(["degas-carre-petit.jpg","degas-carre-petit.jpg","degas-carre-petit.jpg","degas-carre-petit.jpg"],"1.wav")
#sound, stim = display1top3bottom(["degas-rectangle.jpg","degas-carre-petit.jpg","degas-carre-petit.jpg","degas-carre-petit.jpg"],"1.wav")
sound, stim = display1top4bottom(["degas-rectangle.jpg","degas-carre-petit.jpg","degas-carre-petit.jpg","degas-carre-petit.jpg","degas-carre-petit.jpg"],"1.wav")
#video = displayVideo('dog-in-farm.mpg')
box = createBox(stim, top=True)
expyriment.control.start()
sound.play()
box.show()
#video.play()
#video.present()
#video.wait_end()
#video.stop()
expyriment.control.wait_end_audiosystem()
img, resptime = box.wait()
expyriment.control.end()
