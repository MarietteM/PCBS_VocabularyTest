# PCBS_VocabularyTest
A test for assessing vocabulary skills among 3-years-old to 5-years-old french children

# Informations générales sur le projet

J'écris ce code dans le cadre de mon UE PCBS, enseignée par Christophe Pallier, que je suis lors du premier semestre de l'année scolaire 2019/2020 alors que je suis étudiante en première année au Cogmaster (Paris). 

Ce code est aussi celui que je suis amenée à écrire lors de mon stage.

## But du stage

Mons stage consiste à créer un test de vocabulaire pour enfants de 3 à 5 ans en français. Plus précisément, cette démarche s'insipire d'un test pré-existant qui s'appelle le QUILS (Quick Interactive Language Screener). Il s'agit d'un test de vocabulaire anglo-saxon pour enfants de 3 à 5 ans qui a été développé par Roberta M. Golinkoff, Jill de Villiers, Kathy Hirsh-Pasek, Aquiles Iglesias et Mary S. Wilson. 

Le but de mon stage est de fournir l'équivalent de ce test en français, et l'idée est de reproduire la structure du test QUILS pour faire une base au test que nous allons développer en français.

Pour plus d'informations sur le QUILS :
https://quilscreener.com/

## Fonctionnement du test

Le principe est de présenter une bande audio pour poser une question et de choisir la réponse parmi plusieurs images. Une animation ou une image est éventuellement présente pendant la question pour l'illustrer. 

Le test doit être affiché en plein écran, et la souris doit rester apparente. Les réponses doivent pouvoir être enregistrées et vérifiées (être capable de dire si la réponse est vraie ou fausse).

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

Chaque bloc est de longueur variable, c'est-à-dire qu'ils n'ont pas tous le même nombre d'essais.

Chaque bloc consiste en un type de présentation des stimuli, sauf le bloc d'entraînement qui est la succession de trois affichages différents.

Entre chaque bloc, une vidéo de transition est présentée.

# Informations générales sur le code

## But du code

Le but de ce code est de fournir une première version du test, un prototype. C'est-à-dire que les stimuli utilisés sont toujours les mêmes et ne sont pas ceux qui seront utilisés pour faire passer ce test. En l'occurence, j'utilise toujours la même bande son, la même vidéo et des images du même tableau mais qui ont chacune une forme différente (carré, portrait, etc), en attendant l'intégration des sons, vidéos et images 'réels'.

## Langage utilisé

Pour coder ce test, j'ai utilisé Python, et plus particulièrement le module expyriment.

## Fonctionnement du code

# Exécution

Le code qui permet de lancer le test est : TestVocabulaire.py

Il suffit juste de l'exécuter dans la console, sans ajout d'arguments supplémentaires. 

# Interface

Ceci va provoquer l'affichage en plein écran du test.

Le sujet devra attendre la fin de chaque bande son avant de répondre en cliquant sur l'une des images. Dans tous les cas, le clic de la souris n'aura aucun effet tant que la bande son n'est pas terminée.

Pour quitter le test à tout moment, il suffira d'appuyer sur la touche 'echap' du clavier, puis sur la touche 'y' pour confirmer que l'on veut mettre fin au test.

# Fichiers nécessaires

Pour pouvoir tourner, dans le dossier qui contient TestVocabulaire.py, il doit y avoir nécessairement :
- les images suivantes :
   - degas-carre-petit.jpg
   - degas-portrait.jpg
   - degas-rectangle.jpg
- le dossier sounds, contenant les bandes audios
   - 1.wav
- le dossier videos, contenant les transitions vidéos
   - Flower.mp4

# Fichiers créés

L'exécution du code va amener la création de :
- deux dossiers propres à l'utilisation du module expyriment, à savoir
   - un dossier data
   - un dossier event
- un fichier propre à la manière dont j'ai codé le test, à savoir
   - un fichier results.csv, contenant le récapitulatif des réponses fournies par le sujet

## Organisation du code

# Fonctions d'affichage

Un affichage peut consister en l'affichage uniquement d'images cliquables, ou bien en l'affichage d'une image au dessus (qui sert à illustrer la question posée, et qui est non cliquable) et d'autres images en dessous (cliquables), ou encore en l'affichage d'une animation (qui est une image dans la version actuelle) d'abord (non cliquable) et d'un autre type d'affichage ensuite.

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
   
Ainsi, certains essais peuvent avoir des "animations" (qui sont des images dans la version prototype) ou non, des images au dessus des autres (et qui ne doivent pas être cliquables) ou non et qu'il peut y avoir deux présentations ou une seule.

C'est pourquoi chaque fonction va créer un tuple pour rendre compte de ces informations. Ce tuple est de taille 3 et contient ainsi les informations suivantes, dans l'ordre : le booléen qui correspond à la présence d'une animation (si oui : True, sinon : False), le booléen qui correspond à la présence d'une image au dessus des autres (si oui : True, sinon : False), l'entier qui spécifie le nombre de presentations dans l'essai (1 : ni d'animation ni de deuxième affichage, ou 2 : animation ou deuxieme affichage). L'appel de ces fonctions (sauf _displaySquare) va entraîner l'ajout de ce tuple dans la liste CARACTERISTICS. 

L'appel de ces fonctions va aussi résulter en la création d'une box qui permet de rendre des images cliquables et en l'ajout de cette box dans la liste BOXES. 

# Fonctions utilitaires

Pour avoir un affichage harmonieux, j'ai procédé en plusieurs étapes. D'abord, j'ai cherché à voir quel écart je fixais entre les images :
   - je définis une marge arbitraire qui est relative à la taille de l'écran
   - je convertis les images en objet Image pour avoir accès à leurs dimensions
   - je récupère les dimensions des images
   - je calcule l'espace restant après avoir soustrait les dimensions de l'écran aux marges, j'appelle cet espace restant "la boîte"
   - je calcule l'espace restant après avoir soustrait les dimensions de la boîte au cumul des dimensions des images, j'appelle cet espace restant "le reste" (il va donc s'agir de la mesure de l'espace non occupé par les images)
   - je divise ce reste par le nombre d'écart entre les images (par exemple, pour les 3 images en lignes, il existe 2 écarts : entre la 1ère et la 2ème, et entre la 2ème et la 3ème). 

Ensuite, j'ai cherché à placer mes images en fonction du calcul d'écart, et je trouvais ça plus simple d'imaginer :
   - d'une part, que l'origine du repère des coordonnées était situé au niveau du coin en bas à gauche de l'écran,
   - et d'autre part, que le centre de mon image était un curseur et que je déplaçais ce curseur pour placer mon image (un peu de la même manière qu'avec Turtle). 
   
Pour reprendre l'exemple de la ligne de 3 images, ça donne :
   - Pour l'ordonnée : la hauteur de l'écran divisée par deux
   - Pour l'abscisse :
      - Pour la 1ère : marge + longueur de l'image divisée par deux
      - Pour la 2ème : marge + longueur de l'image + écart + longueur de l'image divisée par deux
      - Pour la 3ème : marge + longueur de l'image + écart + longueur de l'image + écart + longueur de l'image divisée par deux

En effet, la position d'une image est celle de son centre (d'où les longueurs d'images divisées par deux), et je pars du principe que toutes les images cliquables auront les mêmes dimensions. 

Enfin, cette manière de calculer les positions n'est cependant pas celle de expyriment puisqu'il utilise comme origine le centre de l'écran. Alors j'ai créé une fonction _conversion_origin pour pouvoir faire la conversion entre la manière dont je réfléchissais pour placer mes images et la manière dont expyriment place les images. C'est ma première fonction utilitaire.

La deuxième est save_data qui me permet d'enregistrer les réponses fournies par l'utilisateur, c'est-à-dire les images sur lesquelles il aura cliqué. 
   - Je compare la référence de l'image cliquée avec les références de l'ensemble des stimuli de l'essai afin d'avoir accès à l'index de cette image dans cette liste des stimuli. Si on prend l'exemple de displaySquareTwice, le liste des stimuli est : stimulus audio 1, stimulus audio 2, stimulus visuel 1.1, stimulus visuel 1.2, stimulus visuel 1.3, stimulus visuel 1.4, stimulus visuel 2.1, stimulus visuel 2.2, stimulus visuel 2.3, stimulus visuel 2.4 (car il consiste en l'affichage d'un carré deux fois de suite). Donc si l'utilisateur clique sur le 2.2, l'index sera 7. Or, en réalité, il s'agit de l'image 2 de la 2ème présentation. Il faut donc modifier cet index pour avoir une réelle visibilité de la réponse fournie. Ainsi :
   - Après avoir eu accès à l'index, je soustrais 1 s'il y a une image au dessus (qui n'est pas cliquable et ne fait donc pas partie des réponses), je soustrais 1 s'il y a une animation, je soustrais 1 s'il y a deux présentations (pour enlever la 'place' occupée dans la liste par le stimulus audio de la 2ème présentation, le stimulus audio de la 1ère présentation n'est pas gênant étant donné qu'il a l'index 0). En reprenant l'exemple, ça donne donc : 7 - 0 - 0 - 1 = 6. Il faut encore prendre en compte le fait qu'il s'agit une image de la 2ème présentation :
   - Les deux affichages qui consistent en 2 présentations comprennent le même nombre de stimulus (10), la différence est que pour displaySquareTwice, il n'y a pas d'image au dessus, contrairement à display1top3bottomTwice. Quoi qu'il en soit, si l'on clique sur la 1ère image de la 2ème présentation pour l'un ou l'autre de ces cas de figures, l'index qui en résultera (après modification) sera supérieur ou égal à 5. En effet, pour displaySquareTwice, la première image cliquable de la 2ème présentation a l'index 6. Et la modification donne : 6 - 0 - 0 - 1 = 5. Et, pour display1top3bottomTwice, la première image cliquable de la 2ème présentation a l'index 7 (l'index 6 est celui de l'image du haut, non cliquable). Et la modification donne : 7 - 1 - 0 - 1 = 5. C'est donc la condition pour mon if. 
   - Ensuite, pour displaySquareTwice, il faut que j'enlève la 'place' occupée par les 4 images de la première présentation : je soustrais donc 4 (dans mon exemple, ça me donne donc 6 - 4 = 2, c'est-à-dire l'index désiré). Pour display1top3bottomTwice, il faut que j'enlève la 'place' occupée par les 3 images de la première présentation et la 'place' occupée par l'image du haut dans la 2ème présentation : je soustrais donc 3 + 1 = 4. D'où ma soustraction par 4 quelque soit la fonction utilisée. 
   - J'enregistre ensuite la réponse dans un tableau : nom du bloc, numéro de l'essai, réponse donnée, True ou False selon si la réponse correspond à celle qui était attendue.

## Justifications des choix

   - Animations qui sont des images
Les animations sont des images dans cette version car nous ne savons pas encore si nous allons utiliser des vidéos ou alors une succession rapide d'images pour donner l'effet de mouvement. 
   - CARACTERISTICS, BOXES, TRANSITIONS non passées en argument
Ce sont mes variables globales et je préférais donc les mettre à jour au fur et à mesure plutôt que de les passer en argument et les modifier. Je trouvais ça plus intuitif de ne pas les passer en argument pour souligner leur caractère gloable et leur mise à jour au fur et à mesure des appels de fonctions.
   - TRIAL passé en argument
Mais j'ai décidé de passer TRIAL en argument parce que ce n'est pas toujours le même essai qui est concerné.
   - Vidéos non intégrées à des essais
Je n'ai pas voulu intégrer les vidéos aux essais parce qu'il s'agit de transitions entre blocs. Je pense que ça aurait été un peu bizarre de l'intégrer en stimulus du dernier essai du bloc par exemple. 
   - Audio intégrés aux essais
Pour que ça soit plus facile pour moi de répérer sur quelle image l'utilisateur a cliqué, j'aurais pu ne pas intégrer les audios aux essais et utiliser une liste que j'aurais transformée en itérateur. Mais, je trouvais ça plus cohérent de garder une unité dans les essais : l'audio a lieu pendant l'essai, c'est donc plus logique (selon moi) de l'y intégrer. Même réflexion pour les animations.
   - display1anim1image n'a pas tellement d'intérêt ?
Dans le QUILS, une image est présentée mais selon l'endroit où on clique sur l'image, ça donne une réponse différente. Ici, que l'on clique sur un endroit ou un autre de l'image, ça ne change pas. Je pense rendre cet essai plus intéressant quand nous aurons les vraies images : je pourrais supperposer des images sur un fond, et rendre ces images cliquables pour donner le même effet que dans le QUILS.

### Bilan

J'ai su mettre en oeuvre mon test en version prototype donc je suis très satisfaite. Je ne pensais pas aller aussi loin dans mes objectifs (intégrer les audios, intégrer les transitions vidéos, enregistrer les données). 

J'ai su appréhender plusieurs fonctionnalités du module expyriment mais je n'ai pas tout découvert et il est tout à fait possible que j'aie trouvé des moyens détournés pour arriver à mes fins (je pense au placement de mes images et à l'enregistrement des réponses, notamment) alors qu'il existait des fonctions toutes faites du module que je n'ai pas trouvées. Et il est sûr que j'ai encore des améliorations à faire (dont certaines que je n'ai pas détéctées), des maladresses à corriger et de l'optimisation à apporter. Cependant, j'ai déjà essayé de mettre le doigt sur les points à améliorer :

## Améliorations possibles

   - Je pourrais faire en sorte de réutiliser, par exemple, display1top3bottom dans display1anim1top3bottom
   - Je pourrais mettre les images dans un dossier 'pictures', tout comme j'ai utilisé un son dans 'sounds' et une vidéo dans 'videos' (je ne l'ai pas fait pour des raisons de simplification du code, mais ce serait donc un point à modifier lorsque nous intégrerons les vraies images au test)
   - Je pourrais essayer de séparer mon code en plusieurs fichiers et d'importer ce dont j'ai besoin pour améliorer sa lisibilité
   - Je pourrais utiliser un 'if main' vers la fin, mais je ne maîtrise pas encore tellement cette pratique, il faudrait que je me renseigne pour savoir si c'est possible et pertinent
   - Je pourrais rendre possible plus facilement le choix d'une marge (en la passant en argument des fonctions par exemple ? ou en la définissant de manière globale ?)
   - Je pourrais simplifier mes étapes de conversion de positions de mes images en créant une autre fonction qui prendrait en arguments x et y, et qui retournerait : _conversion_origin(round(x), round(y))
   - Je pourrais essayer de modifier les affichages préalables au test, comme "Ready" par exemple (il faudrait que je regarde si c'est possible de le modifier et de le traduire)
   - Je pourrais essayer de trouver un moyen pour que mon test supporte l'affichage de vidéos aux dimensions plus élevées : dans cette version, les vidéos n'ont pas été présentées en plein écran pour éviter d'avoir une image saccadée (que j'avais sur mon ordinateur dès que j'augmentais les dimensions de la video). Celle que j'ai décidée d'utiliser est donc une 640x360. J'ai quand meme gardé les versions en 960x540, 1280x720 et 1920x1080 donc vous pouvez essayer ces autres versions sur votre ordinateur s'il est plus puissant que le mien.
   - Je pourrais faire en sorte de vérifier que les dimensions des images cliquables soient identiques lors d'un essai, et si ce n'est pas le cas, soit renvoyer un message d'erreur, soit de redimensionner. Dans cette version, je pars du principe que toutes les images sont déjà dimensionnées correctement et de manière identique. De la même manière, je pourrais aussi vérifier que toutes les images sont capables de tenir dans la fenêtre.
   - Je pourrais pré-charger les images et les audios (ici je ne l'ai fait que pour les vidéos)

## Niveau en python

J'ai plutôt un bon niveau en programmation Python.

## Ce que ce projet m'a apporté

J'ai aimé faire ce projet d'abord parce que j'ai programmer en Python (je peux passer des heures à programmer et à débeuguer sans m'en lasser). J'ai aussi aimé ce projet parce que j'ai pu apprendre à manipuler le module expyriment que je ne connaissais pas du tout avant. C'est un module assez pratique pour créer des expériences en psychologie. J'ai aussi pu mettre en place pour la première fois des itérateurs, que j'ai trouvé bien pratiques. J'ai pu me replonger un peu dans la création et manipulation de fichiers en python (notamment avec le module os). C'est un module très utile, mais dont j'oublie régulièrement les fonctions disponibles alors un petit rappel ne m'a pas fait de mal. Mais aussi, et surtout, ce projet m'a donné de l'intérêt pour la manière de bien rédiger un code en Python. Il existe une multitude de règles et de normes que j'ai envie de connaître pour fournir des scripts plus agréables à lire et plus facilement compris par des experts et non-experts. Je pense notamment au PEP-8, à l'utilisation de Assert, de Raise, etc. Ce projet m'a donné envie d'en savoir plus sur les bonnes pratiques de programmation.

## Ce que l'UE m'a apporté

Cette UE a été plutôt une bonne expérience pour moi, j'ai aimé cette opportunité de développer un projet et d'avoir des conseils pendant sa réalisation. J'ai aussi pu apprendre à me servir un peu de GitHub (et de Slack aussi !), et ré-utiliser le module Pygame. J'aime bien utiliser la programmation pour coder des choses un peu ludiques comme des petits jeux ou des illusions d'optiques. Je trouve que c'est un bon moyen de donner de l'intérêt et de l'envie de programmer.

## Ce qu'il m'a manqué dans cette UE

Je trouve que ça aurait été mieux de faire des groupes de niveaux pour que chacun eut l'occasion de développer au mieux ses compétences en programmation. Moi, je suis plutôt à l'aise en python, tandis que d'autres camarades n'en avait jamais fait. Les deux groupes auraient pu être décidés de cette manière. Ainsi, les débutants auraient pu commencer à programmer des choses simples et utiliser Pygame pour avoir le côté ludique, tandis que ceux qui sont le plus à l'aise auraient pu perfectionner leur pratique, notamment en (re)découvrant les bonnes pratiques en python ou des manières d'optimiser son code et de le vérifier, ou encore en allant plus loin avec l'utilisation des dataframe ou la gestion de fichiers, par exemple. 

Mais, cette UE a quand même été globalement une bonne expérience pour moi, j'ai aimé faire ce projet et j'ai apprécié l'utilisation de Slack pour avoir des conseils personnalisés.
