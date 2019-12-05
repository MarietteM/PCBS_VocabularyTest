import expyriment
import pandas as pd

exp = expyriment.design.Experiment(name="QUILS-Prototype")
expyriment.control.initialize(exp)
mouse = expyriment.io.Mouse(show_cursor=True)
design = pd.read_csv("design.csv")
size = expyriment.io.Screen.size
center_x = exp.screen.center_x
center_y = exp.screen.center_y

e = 1
for b in design.itertuples():
    bloc = expyriment.design.Block(name=design.loc[b, 'Nom'])
    liste_des_types = (design.loc[b, 'Types']).split(",")
    longueur = len(liste_des_types)
    for t in liste_des_types:
        essai = expyriment.design.Trial(name=str(e))
        if t == "L4":
            f = round(size[1]/100)
            marge = 5*f
            stim1 = expyriment.stimuli.Picture("degas-carre.jpg", position=(-200,center_y))
            surface_size = stim1.surface_size()
            stim2 = expyriment.stimuli.Picture("degas-carre.jpg", position=(-100,center_y))
            stim3= expyriment.stimuli.Picture("degas-carre.jpg", position=(-50,center_y))
            stim4 = expyriment.stimuli.Picture("degas-carre.jpg", position=(-25,center_y))
            stim1.preload()
            stim2.preload()
            stim3.preload()
            stim4.preload()
            pass
        elif t == "L3":
            pass
        elif t == "P3":
            pass
        elif t == "A2":
            pass
        elif t == "AP3":
            pass
        elif t == "AP4":
            pass
        elif t == "G" :
            pass
        elif t == "A3" :
            pass
        elif t == "PC" :
            pass
        elif t == "R3" :
            pass
        bloc.add_trial(essai)
        e += 1
    exp.add_block(bloc)


expyriment.control.start()


expyriment.control.end()
