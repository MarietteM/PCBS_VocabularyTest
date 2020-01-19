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

Pour coder ce test, j'utiliserai Python, et plus particulièrement le module expyriment.


# Informations générales sur le code

## Code

Le code qui permet de lancer le test est : VocabularyTest.py

Il suffit juste de l'exécuter dans la console, sans ajout d'arguments supplémentaires. 

## Interface

Ceci va provoquer l'affichage en plein écran du test.

Le sujet devra atteindre la fin de chaque bande son avant de répondre en cliquant sur l'une des images. Dans tous les cas, le clic de la souris n'aura aucun effet tant que la bande son n'est pas terminée.

Pour quitter le test à tout moment, il suffira d'appuyer sur la touche echap du clavier, puis sur la touche y pour confirmer que l'on veut mettre fin au test.

## Fichiers nécessaires

Pour pouvoir tourner, dans le dossier qui contient VocabularyTest.py, il doit y avoir nécessairement aussi :
- les images suivantes :
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

## Organisation du test

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

Chaque bloc est de longueur variables, c'est-à-dire qu'ils n'ont pas tous le même nombre d'essais.

Chaque bloc consiste en un type de présentation des stimuli, sauf le bloc d'entraînement qui est la succession de trois affichages différents.

Entre chaque bloc, une vidéo de transition est présentée.

## Fonctions d'affichage

Un affichage peut consister en l'affichage uniquement d'images cliquables, ou bien en l'affichage d'une image au dessus (qui sert à illustrer la question posée, et qui est non cliquable) et d'autres images en dessous (cliquables), ou encore en l'affichage d'une animation (qui est une image dans la version actuelle puisqu'il s'agit d'un prototype) d'abord (non cliquable) et d'un autre type d'affichage ensuite.

Chaque type d'affichage a une fonction dédiée :
   - displayLine4Images : 4 images en ligne
   - displayLine3Images : 3 images en ligne
   - display1top3bottom : 1 image au dessus, 3 en dessous
   - display1top4bottom : 1 image au dessus, 4 en dessous
   - display1anim1image : d'abord, 1 image, puis 1 autre image
   - display1anim1top3bottom : d'abord, 1 image, puis 1 image au dessus et 3 en dessous
   - display1anim1top4bottom : d'abord, 1 image, puis 1 image au dessus et 4 en dessous
   - _displaySquare : 4 images en carré
   - displaySquareTwice : deux fois l'affichage carré
   - dispay1top3bottomTwice : deux fois l'affichage de 1 image au dessus et 3 en dessous
   
Ainsi, on voit que certains essais peuvent avoir des "animations" (qui sont des images dans la version prototype) ou non, des images au dessus des autres (et qui ne doivent pas être cliquables) ou non et qu'il peut y avoir deux présentations ou non.

C'est pourquoi chaque fonction va créer un tuple pour rendre compte de ces informations. Ce tuple est de taille 3 et contient ainsi les informations suivantes, dans l'ordre : le booléen qui correspond à la preéence d'une animation (si oui : True, sinon : False), le booléen qui correspond à la présence d'une image au dessus des autres (si oui : True, sinon : False), l'entier qui specifie le nombre de presentations dans l'essai (1 : ni d'animation ni de deuxième affichage, ou 2 : animation ou deuxieme affichage ). L'appel de ces fonctions (sauf _displaySquare) va entraîner l'ajout de ce tuple dans la liste CARACTERISTICS. 

L'appel de ces fonctions va aussi résulter en la création d'une box qui permet de rendre des images cliquables et en l'ajout de cette box dans la liste BOXES. Ainsi, seules les images autres que les animations et images du haut ne le seront pas. 

## Fonctions utilitaires

Pour avoir un affichage harmonieux, j'ai procédé en plusieurs étapes. D'abord, j'ai cherché à voir quel écart je fixais entre les images :
   - je définis une marge arbitraire qui est relative à la taille de l'écran
   - je convertis les images en objet Image pour avoir accès à leurs dimensions
   - je récupère les dimensions des images
   - je calcule l'espace restant après avoir soustrait les dimensions de l'écran aux marges, j'appelle cet espace restant "la boîte"
   - je calcule l'espace restant après avoir soustrait les dimensions de la boîte au cumul des dimensions des images, j'appelle cet espace restant "le reste" (il va donc s'agir de la mesure de l'espace non occupé par les images)
   - je divise ce reste par le nombre d'écart entre les images (par exemple, pour les 3 images en lignes, il existe 2 écarts : entre la 1ère et la 2ème, et entre la 2ème et la 3ème). 
Ensuite, j'ai cherché à placer mes images en fonction de calcul d'écart, et je trouvais ça plus simple d'imaginer que le centre de mon image était un curseur et que je déplaçais ce curseur pour placer mon image (un peu de la même manière qu'avec Turtle). Pour reprendre l'exemple de la ligne de 3 images, ça donne :
   - Pour l'ordonnée : la hauteur de l'écran divisée par deux
   - Pour l'abscisse :
      - Pour la 1ère : marge + longueur de l'image divisée par deux
      - Pour la 2ème : marge + longueur de l'image + écart + longueur de l'image divisée par deux
      - Pour la 3ème : marge + longueur de l'image + écart + longueur de l'image + écart + longueur de l'image divisée par deux
En effet, la position d'une image est celle de son centre (d'où les longueurs d'image divisée par deux), et je pars du principe que chaque image aura les mêmes dimensions. 
Enfin, cette manière de calculer les positions n'est cependant pas celle de expyriment puisqu'il utilise comme origine le centre de l'écran. Alors j'ai créé une fonction _conversion_origin pour pouvoir faire la conversion entre la manière dont je réfléchissais pour placer mes images et la manière dont expyriment place les images. C'est ma première fonction utilitaire.

La deuxième est save_data qui me permet d'enregistrer les réponses fournies par l'utilisateur, c'est-à-dire les images sur lesquelles il aura cliqué. 
   - Je compare la référence de l'image cliquée avec les références de l'ensemble des stimuli de l'essai afin d'avoir accès à l'index de cette image dans cette liste des stimuli. Si on prend l'exemple de displaySquareTwice, le liste des stimuli est : stimulus audio 1, stimulus audio 2, stimulus visuel 1.1, stimulus visuel 1.2, stimulus visuel 1.3, stimulus visuel 1.4, stimulus visuel 2.1, stimulus visuel 2.2, stimulus visuel 2.3, stimulus visuel 2.4. Donc si l'utilisateur clique sur le 2.2, l'index sera 7. Or, en réalité, il s'agit de l'image 3 de la 2ème présentation. Il faut donc modifier cet index pour avoir une réelle visibilité de la réponse fournie. Ainsi :
   - Après avoir eu accès à l'index, je soustrais 1 s'il y a une image au dessus (qui n'est pas cliquable et ne fait donc pas partie des réponses), je soustrais 1 s'il y a une animation, je soustrais 1 s'il y a deux présentations (pour enlever la 'place' occupée dans la liste par le stimulus audio de la 2ème présentation, le stimulus audio de la 1ère présentation n'est pas gênant étant donné qu'il a l'index 0). En reprenant l'exemple, ça donne donc : 7 - 0 - 0 - 1 = 6. Il faut encore prendre maintenant en compte le fait qu'il s'agit une image de la 2ème présentation :
   - Les deux affichages qui consistent en 2 présentations comprennent le même nombre de stimulus (10), la différence est que pour displaySquareTwice, il n'y a pas d'image au dessus, contrairement à display1top3bottomTwice. Quoi qu'il en soit, si l'on clique sur la 1ère image de la 2ème présentation pour l'un ou l'autre de ces cas de figures, l'index qui en résultera (après modification) sera supérieur ou égal à 5. C'est donc la condition pour mon if. Ensuite, pour displaySquareTwice, il faut que j'enlève la 'place' occupée par les 4 images de la première présentation : je soustrais donc 4 (dans mon exemple, ça me donne donc 6 - 4 = 2, c'est-à-dire l'index désiré). Pour display1top3bottomTwice, il faut que j'enlève la 'place' occupée par les 3 images de la première présentation et la 'place' occupée par l'image du haut dans la 2ème présentation : je soustrais donc 3 + 1 = 4. D'où ma soustraction par 4 quelque soit la fonction utilisée. 
   - J'enregistre ensuite la réponse dans un tableau : nom du bloc, numéro de l'essai, réponse donnée, True ou False selon si la réponse correspond à celle qui était attendue.

# Bilan

J'ai réussi à mettre en place mon test, à intégrer les sons et les vidéos.

## Justifications des choix

   - Animations qui sont des images
Les animations sont des images dans cette version car nous ne savons pas encore si nous allons utiliser des vidéos ou alors une succession rapide d'images pour donner l'effet de mouvement. 
   - CARACTERISTICS, BOXES, TRANSITIONS non passées en argument
Ce sont mes variables globales et je préférais donc les mettre à jour au fur et à mesure plutôt que tu les entrer en argument et les modifier. Je trouvais ça plus intuitif de ne pas les passer en argument pour souligner leur caractère gloable et leur mise à jour au fur et à mesure des appels de fonctions.
   - TRIAL passé en argument
Mais j'ai décidé de passer TRIAL en argument parce que ce n'est pas toujours le même essai qui est concerné.
   - Vidéos non intégrées à des essais
Je n'ai pas voulu intégrer les vidéos aux essais parce qu'il s'agit de transitions entre blocs. Je pense que ça aurait été un peu bizarre de l'intégrer en stimulus du dernier essai du bloc par exemple. 
   - Audio intégrés aux essais
Pour que ça soit plus facile pour moi de répéré sur quelle image l'utilisateur a cliqué, j'aurais pu ne pas intégrer les audios aux essais et utiliser une liste que j'aurais transformé en itérateur. Mais, je trouvais ça plus cohérent de garder une unité dans les essais : l'audio a lieu pendant l'essai, c'est donc plus logique (selon moi) de l'y intégrer. Même réflexion pour les animations.
   - display1anim1image n'a pas tellement d'intérêt ?
Dans le QUILS, une image est présentée mais selon l'endroit où on clique sur l'image, ça donne une réponse différente. Ici, que l'on clique sur un endroit ou un autre de l'image ça ne change pas. Je pense rendre cet essai plus intéressant quand nous aurons les vraies images : je pourrais supperposer des images sur un fond, et rendre ces images cliquables pour donner le même effet que dans le QUILS.

## Améliorations possibles
   - Je pourrais faire en sorte de réutiliser, par exemple, display1top3bottom dans display1anim1top3bottom
   - Je pourrais mettre les images dans un dossier 'pictures', tout comme j'ai utilisé un son dans 'sounds' et une vidéo dans 'videos' (je ne l'ai pas fait pour des raisons de simplification du code, mais ce serait donc un point à modifier lorsque nous intégrerons les vraies images au test)
   - Je pourrais essayer de séparer mon code en plusieurs fichiers et d'importer ce dont j'ai besoin pour améliorer sa lisibilité
   - Je pourrais utiliser un 'if __main__' vers la fin, mais je ne maîtrise pas encore tellement cette pratique, il faudrait que je me renseigne pour savoir si c'est possible et pertinent
   - Je pourrais rendre possible plus facilement le choix d'une marge (en la passant en argument des fonctions par exemple ? ou en la définissant de manière globale ?)
   - Je pourrais simplifier mes étapes de conversion de positions de mes images en créant une autre fonction qui prendrait en arguments x et y, et qui retournerait : _conversion_origin(round(x), round(y))
   - Je pourrais essayer de modifier les affichages préalables au test, comme "Ready" par exemple (il faudrait que je regarde si c'est possible de le modifier et de le traduire par exemple).

## Niveau et progrès

J'ai plutôt un bon niveau en programmation Python.

J'ai aimé faire ce projet d'abord parce que j'ai programmer en Python (je peux passer des heures à programmer et à débeuguer sans m'en lasser). J'ai aussi aimé ce projet parce que j'ai pu apprendre à manipuler le module expyriment que je ne connaissais pas du tout avant. C'est un module assez pratique pour créer des expériences en psychologie. J'ai aussi pu mettre en place pour la première fois des itérateurs, que j'ai trouvé bien pratiques. J'ai pu me replonger un peu dans la création et manipulation de fichiers en python (notamment avec le module os). C'est un module très utile, mais dont j'oublie régulièrement les fonctions disponibles alors un petit rappel ne m'a pas fait de mal.

J'ai su mettre en oeuvre mon test en version prototype alors je suis très satisfaite. Je ne pensais pas aller aussi loin dans mes objectifs. J'ai sûrement encore des améliorations à faire que je n'ai pas détéctées, des maladresses ou un manque d'optimisation, mais avec les retours que j'aurai de ce projet, j'aurai une idée de ce qu'il m'a manqué. 

Cette UE a été une bonne expérience pour moi, j'ai aimé cette opportunité de développer un projet et d'avoir des conseils pendant sa réalisation.
