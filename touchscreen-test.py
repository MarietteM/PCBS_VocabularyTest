#! /usr/bin/env python
# Time-stamp: <2019-11-19 13:02:26 christophe@pallier.org>

""" Touchscreen test """

import expyriment

NTRIALS = 1

exp = expyriment.design.Experiment(name="sentence picture matching task")  # create an Experiment object
expyriment.control.set_develop_mode(on=True)  ## Set develop mode. Comment for real experiment

expyriment.control.initialize(exp)

img1 =  expyriment.stimuli.Picture("no2.jpg", position=(-200, 100))  # NO
img2 =  expyriment.stimuli.Picture("yes2.jpg", position=(200, 100))  # YES
img3 = expyriment.stimuli.Picture("no2.jpg", position=(-200, -100))
img4 =  expyriment.stimuli.Picture("yes2.jpg", position=(200, -100))

BB = expyriment.io.TouchScreenButtonBox([img1, img2])
BB.create()

exp.add_data_variable_names(['resonse', 'rt'])

expyriment.control.start()

for i in range(NTRIALS):
    #BB.show()
    #img, resptime = BB.wait()
    img1.present()
    exp.clock.wait(1000)
    img2.present()
    exp.clock.wait(1000)
    img3.present()
    exp.clock.wait(1000)
    img4.present()
    exp.clock.wait(1000)

    #exp.data.add(["No" if img == img1 else "Yes" , resptime])

    exp.screen.clear()
    exp.screen.update()

    exp.clock.wait(2000)

expyriment.control.end()
