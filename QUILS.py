import pygame

window_resolution = (500, 500)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

list_of_blocks = ["PRACTISE", "WH-QUESTIONS", "PAST TENSE", "VERB LEARNING", "PREPOSITIONAL PHRASES", "CONVERTING ACTIVE TO PASSIVE", "EMBEDED CLAUSES", "NOUNS", "VERBS", "NOUN LEARNING", "PREPOSITIONS", "ADJECTIVE LEARNING", "CONJUNCTIONS"]
list_of_lengths = [3, 5, 4, 4, 3, 2, 4, 3, 5, 5, 5, 5, 3]
list_of_num = [["PR1", "PR2", "PR3"],
                [x for x in range(1,6)],
                [x for x in range(6, 10)],
                [x for x in range(10, 14)],
                [x for x in range(14,17)],
                [x for x in range(17,19)],
                [x for x in range(19,23)],
                [x for x in range(23,26)],
                [x for x in range(26,31)],
                [x for x in range(31,36)],
                [x for x in range(36,41)],
                [x for x in range(41,46)],
                [x for x in range(46,49)]]

class Block:
    def __init__(self, nom, position, longueur, liste_numeros, competence):
        self.nom = nom
        self.position = position
        self.longueur = longueur
        self.liste_numeros = liste_numeros
        self.competence = competence

practise_block = Block(list_of_blocks[0], 0, list_of_lengths[0], list_of_num[0], "")
wh_questions_block = Block(list_of_blocks[1], 1, list_of_lengths[1], list_of_num[1], "")
past_tense_block = Block(list_of_blocks[2], 2, list_of_lengths[2], list_of_num[2], "")
verb_learning_block = Block(list_of_blocks[3], 3, list_of_lengths[3], list_of_num[3], "")
prepositional_phrases_block = Block(list_of_blocks[4], 4, list_of_lengths[4], list_of_num[4], "")
converting_active_to_passive_block = Block(list_of_blocks[5], 5, list_of_lengths[5], list_of_num[5], "")
embeded_clauses_block = Block(list_of_blocks[6], 6, list_of_lengths[6], list_of_num[6], "")
nouns_block = Block(list_of_blocks[7], 7, list_of_lengths[7], list_of_num[7], "")
verbs_block = Block(list_of_blocks[8], 8, list_of_lengths[8], list_of_num[8], "")
noun_learning_block = Block(list_of_blocks[9], 9, list_of_lengths[9], list_of_num[9], "")
prepositions_block = Block(list_of_blocks[10], 10, list_of_lengths[10], list_of_num[10], "")
adjective_learning_block = Block(list_of_blocks[11], 11, list_of_lengths[11], list_of_num[11], "")
conjuctions_block = Block(list_of_blocks[12], 12, list_of_lengths[12], list_of_num[12], "")


def display4images():
    pass

def display3images():
    pass

def display1top3bottom():
    pass

def display1imagebig():
    pass

def display1imagetop():
    pass

def display1top4bottom():
    pass

def display4imagessquare():
    pass

def display3imagesbig():
    pass

def display1top3bottomlittle():
    pass

def display1top3bottomrectangle():
    pass

pygame.init()
pygame.display.set_caption("QUILS - Prototype")
window_surface = pygame.display.set_mode(window_resolution)

launched = True

while launched :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            launched = False
