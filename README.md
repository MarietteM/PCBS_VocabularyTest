# PCBS_VocabularyTest
A test for assessing vocabulary skills among 3-years-old to 5-years-old french children

# Informations générales sur le projet

J'écris ce code dans le cadre de mon UE PCBS, enseignée par Christophe Pallier, que je suis suite à mon intégration du Cogmaster (M1). 

Ce code est aussi celui que je suis amenée à écrire lors de mon stage.

## But

Le but de ce code est de fournir une première version d'un test de vocabulaire pour des enfants âgés de 3 à 5 ans. Ce test doit être relativement court (15 voire 20min). Le principe est de présenter une bande audio pour poser une question et de choisir la réponse parmi plusieurs images. Une animation ou une image sera présente pendant la question. Il existe plusieurs dispositions d'images pour ce test, et mon but, dans ce projet, est de les créer afin de pouvoir intégrer les images 'réelles' (celles que nous allons utiliser pour rendre le test fonctionnel).
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

# Informations plus précises sur le code


