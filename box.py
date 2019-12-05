import expyriment
import pandas

#summary = pandas.read_csv("summary.csv")

NTRIALS = 5

exp = expyriment.design.Experiment(name="QUILS-Prototype")
expyriment.control.initialize(exp)
mouse = expyriment.io.Mouse(show_cursor=True)

stim1 = expyriment.stimuli.Picture("degas-portrait.jpg", position=(-200,100))
stim2 = expyriment.stimuli.Picture("degas-portrait.jpg", position=(200,100))
#stim1.preload()
#stim2.preload()
box = expyriment.io.TouchScreenButtonBox([stim1, stim2])
box.create()
exp.add_data_variable_names(['response', 'rt'])

expyriment.control.start()

id = experiment.subject
nbCorrectResponses = 0

for _ in range(NTRIALS):
    #stim1.present(clear=True, update=False)
    #stim2.present(clear=False, update=True)
    box.show()
    #button, rt = box.wait(duration=5000)
    button, rt = box.wait(duration=5000)
    exp.data.add(['Stim1' if button == stim1 else 'Stim2', rt])
    #if button == stim1 :
    #   exp.data.add(1, rt)
    #   nbCorrectResponses += 1
    #else :
    #   exp.data.add(0, rt)
    exp.screen.clear()
    exp.screen.update()
    exp.clock.wait(2000)
expyriment.control.end()

expyriment.misc.data_preprocessing.write_concatenated_data(data_folder = 'data', file_name = 'box', output_file = 'resultats-test-box.csv' )
#expyriemnt.misc.data_preprocessing.write_csv_file('resulat', file)
