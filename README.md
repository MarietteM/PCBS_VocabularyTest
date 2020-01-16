# PCBS_VocabularyTest
A test for assessing vocabulary skills among 3-years-old to 5-years-old french children

# Informations générales sur le projet

J'écris ce code dans le cadre de mon UE PCBS, enseignée par Christophe Pallier, que je suis suite à mon intégration du Cogmaster (M1). 

Ce code est aussi celui que je suis amenée à écrire lors de mon stage.

## But

### But du stage

Mons stage consiste créer un test de vocabulaire pour enfants de 3 à 5 ans en français. Plus précisément, cette démarche s'insipire d'un test pré-existant qui s'appelle le QUILS (Quick Interactive Language Screener). Il s'agit d'un test de vocabulaire anglo-saxons pour enfants de 3 à 5 ans qui a été développé par Roberta M. Golinkoff, Jill de Villiers, Kathy Hirsh-Pasek, Aquiles Iglesias et Mary S. Wilson en 2017. 

Le but de mon stage est de fournir l'équivalent de ce test en français. J'ai donc reproduit la structure du test QUILS pour faire une base au test que nous allons développer en français.

Pour plus d'informations sur le QUILS :
https://quilscreener.com/

### But du code

Le but de ce code est de fournir une première version du test, un prototype. C'est-à-dire que les stimulus utilisés seront toujours les mêmes.

Le principe est de présenter une bande audio pour poser une question et de choisir la réponse parmi plusieurs images. Une animation ou une image sera présente pendant la question. Il existe plusieurs dispositions d'images pour ce test, et mon but, dans ce projet, est de les créer afin de pouvoir intégrer les images 'réelles' (celles que nous allons utiliser pour rendre le test fonctionnel).


Pour cela, j'utilise le module expyriment : je scinde le test en plusieurs blocs (qui correspondront à différents types de vocabulaire, comme le vocabulaire des noms, le vocabulaire des verbes, etc). Dans cette version du code, j'utilise toujours la même image mais qui a différentes formes (carré, portrait, etc), en attendant l'intégration des images 'réelles'. 

## Objectifs

Selon mon avancement, je serai peut-être amenée à :
- utiliser une bande-son d'essai ;
- utiliser une animation d'essai ;
- intégrer des transitions entre les différents blocs sous forme d'une vidéo.

Encore une fois, mon but actuel est de créer les dispositions des différents essais et de les intégrer au test divisé en plusieurs blocs.

## Langage utilisé

Pour coder ce test, j'utiliserai Python.


# Informations générales sur le code

## Code

Le code qui permet de lancer le test est : VocabularyTest.py

Il suffit juste de l'exécuter dans la console, sans ajout d'arguments supplémentaires :

```
python VocabularyTest.py
```

## Interface

Ceci va provoquer l'affichage en plein écran du test.

Le sujet devra atteindre la fin de chaque bande son avant de répondre en cliquant sur l'une des images. Dans tous les cas, le clic de la souris n'aura aucun effet tant que la bande son n'est pas terminée.

Pour quitter le test à tout moment, il suffira d'appuyer sur la touche echap du clavier, puis sur la touche y pour confirmer que l'on veut mettre fin au test.

## Fichiers nécessaires

Pour pouvoir tourner, dans le dossier qui contient VocabularyTest.py, il doit y avoir nécessairement aussi :
- le dossier pictures, contenant les images
   - degas-carre-petit.jpg
   - degas-portrait.jpg
   - degas-rectangle.jpg
- le dossier sounds, contenant les bandes audios
   - 1.wav
- le dossier videos, contenant les transitions vidéos
   - Flower.mp4

## Fichiers créés

L'exécution du code va amener la création de :
- deux dossiers propres à l'utilisation du module expyriment, à savoir
   - un dossier data
   - un dossier event
- un fichier propres à la manière dont j'ai codé le test, à savoir
   - un fichier results.csv, contenant le récapitulatif des réponses fournies par le sujet

# Informations générales sur le test



Le test doit être affiché en plein écran, et la souris doit rester apparente.

## Blocs

Le test est composé d'un bloc d'entraînement et de 12 blocs de test. 

Chaque bloc a une thématique, et elles sont les suivantes (dans l'ordre) :
0. Entraînement (PRACTISE)
1. Questions (WH-QUESTIONS)
2. Passé (PAST TENSE)
3. Apprentissage des verbes (VERB LEARNING)
4. Phrases prépositionnelles (PREPOSITIONAL PHRASES)
5. Conversions actif-passif (CONVERTING ACTIVE TO PASSIVE)
6. Clauses enclavées (EMBEDED CLAUSES)
7. Noms (NOUNS)
8. Verbes (VERBS)
9. Apprentissage des noms (NOUN LEARNING)
10. Prépositions (PREPOSITIONS)
11. Apprentissage des adjectifs (ADJECTIVE LEARNING)
12. Conjonctions (CONJUNCTIONS)


