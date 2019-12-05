import expyriment
from PIL import Image

exp = expyriment.design.Experiment(name="QUILS-Prototype")
expyriment.control.initialize(exp)
mouse = expyriment.io.Mouse(show_cursor=True)
screen = exp.screen
window_size = screen.window_size
screen_size = screen.size
center_x = exp.screen.center_x
center_y = exp.screen.center_y

margin = round(screen_size[0]/100)
stim1 = None
stim2 = None
stim3 = None
stim4 = None


def _conversion_origin(position, window_size = screen.window_size):
    x = position[0]-round(window_size[0]/2)
    y = position[1]-round(window_size[1]/2)
    return (x,y)

def affichage(images, window_size = screen.window_size):
    global stim1
    global stim2
    global stim3
    global stim4
    #verifier que l'arguement est une liste
    #verifier que les elements de la liste sont des chaines de cara
    #verifier que ca correpond a des images
    #verifier que la longueur de la liste est de 4
    nb = len(images)
    image1 = Image.open(images[0])
    #image1 = image1.resize((20,100))
    path1 = "image1.png"
    image1.save(path1)
    w1, h1 = image1.size
    image2 = Image.open(images[1])
    #image2 = image2.resize((20,100))
    path2 = "image2.png"
    image2.save(path2)
    w2, h2 = image2.size
    image3 = Image.open(images[2])
    #image3 = image3.resize((20,100))
    path3 = "image3.png"
    image3.save(path3)
    w3, h3 = image3.size
    image4 = Image.open(images[3])
    #image4 = image4.resize((20,100))
    path4 = "image4.png"
    image4.save(path4)
    w4, h4 = image4.size
    images = [path1, path2, path3, path4]
    #verifier que les images ont les memes dimensions
    #redimensionner les images a la taille de l'image la plus petite avec Image.resize(size) size est un tuple
    w, h = image1.size #ici je mets image1 mais ca doit etre l'image la plus petite!
    box_size = (window_size[0]-2*margin,window_size[1]) #verifier que les images ne sont pas trop grandes et depassent du cadre
    rest = (box_size[0]-4*w, box_size[1]-1*h) #pourquoi pas mettre ce 4 et 1 en argument et faire des if pour voir quelle est la disposition souhaitee ?
    gap = round(rest[0]/3)
    p1 = _conversion_origin((round(margin+0*(w+gap)+w/2), round(window_size[1]/2)))
    p2 = _conversion_origin((round(margin+1*(w+gap)+w/2), round(window_size[1]/2)))
    p3 = _conversion_origin((round(margin+2*(w+gap)+w/2), round(window_size[1]/2)))
    p4 = _conversion_origin((round(margin+3*(w+gap)+w/2), round(window_size[1]/2)))
    stim1 = expyriment.stimuli.Picture(images[0], position = p1)
    stim2 = expyriment.stimuli.Picture(images[1], position = p2)
    stim3 = expyriment.stimuli.Picture(images[2], position = p3)
    stim4 = expyriment.stimuli.Picture(images[3], position = p4)

affichage(["degas-portrait.jpg","degas-portrait.jpg","degas-portrait.jpg","degas-portrait.jpg"])

expyriment.control.start()
stim1.present()
exp.clock.wait(1000)
stim2.present(clear=False)
exp.clock.wait(1000)
stim3.present(clear=False)
exp.clock.wait(1000)
#stim4.present(clear=False)
#exp.clock.wait(1000)
expyriment.control.end()
#clear=False, update=True
#"degas-portrait.jpg","degas-portrait.jpg","degas-portrait.jpg","degas-portrait.jpg"
