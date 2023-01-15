<div align="left">
Arnaud Huguenot-Noël

Yoan Moreau

IESE5

17/01/2023
</div>

## Introduction

Lors de notre 5ème année à Polytech Grenoble, il nous a été demandé de travailler sur une durée de 16h en présentiel au FabLab de Grenoble, sur des projets permettant de mettre en place des systèmes connectés.

Lors de ce projet nous allons essayer de mettre en place un système d'ouverture de porte via un QRcode généré par un script python et de le décoder à l'aide d'une caméra permettant sa reconnaissance, le tout, sur une Raspberry PI.

##  1 - Analyse du marché

Le marché des serrures connectées est en croissance rapide. La demande pour les systèmes de sécurité de domicile augmente fortement. La fonctionnalité majeure est la possibilité de verrouiller et déverrouiller à distance à l'aide d'un smartphone. Les principaux acteurs sur ce marché sont August, Schlage et Yale. Le marché de ce secteur était estimé à 3,1 milliards de dollars en 2020 et pourrait atteindre 8 milliards en 2026. La croissance de ce marché devrait principalement se trouver en Asie et de manière plus modérée en Europe et en Amérique du Nord. Les prévisions de croissance à long terme pour ce marché sont positives. Les serrures connectées peuvent être connectées à des systèmes de domotique pour une intégration encore plus complète (Google Home, Amazon Alexa, etc).

L’essor de ce marché est notamment lié aux services de location de logement sur courte durée (notamment AirBnB) car il permet facilement de sécuriser son domicile à distance. De plus, ce type de dispositif peut également s’intégrer aux résidences étudiantes ayant un fort turn-over des locataires.

Les principales caractéristiques des serrures des fabricants cités sont :
- Un prix commençant autour de 150 – 200 €
- La possibilité de verrouiller et déverrouiller à distance à l'aide d'un smartphone via une application dédiée
- La possibilité de donner des accès temporaires à des invités
- Un historique des accès
- Le verrouillage automatique

## 2 - Architecture globale du système

![Architecture idéale](https://github.com/yyoan741/Projet_IoT_5A/blob/main/report/images/Archi_idéale.png)

Le scénario d'utilisation idéal est le suivant :
1. Appui du bouton poussoir sur le Wio Terminal. Cela déclenche la génération et l'envoi du QR code au serveur Home Assistant.
2. L'utilisateur se connecte au serveur Home Assistant sur son smartphone pour récupérer le QR code.
3. La caméra détecte le QR code affiché sur le smartphone. Il est décodé, décrypté. L'utilisateur peut suivre l'avancement du protocole sur l'écran du Wio Terminal.
4. Si le QR code est valide, la Raspberry Pi déclenche l'ouverture.

## 3 - Définition logiciel embarqué
Pour ce qui est de la partie embarqué de notre système, celui repose principalement sur l'utilisation de Home Assistant OS.

### 3-1 - Mise en place Proof of Concept

Dans un premier temps, nous avons décidé de simuler le cas où un serveur Home Assistant était déjà implanté chez l'utilisateur pour y ajouter notre solution et le connecter à celui-ci.

Notre Proof of Concept est donc actuellement composé de 2 Raspberry PI, l'une hébergeant le serveur Home Assistant à l'aide de son OS dédié et l'autre hébergeant nos scripts python à exécuter dans un fichier Bash, ainsi que la partie Hardware, les logiciels complémentaires à ceux-ci et leurs bibliothèques associées afin d'assurer leur bon fonctionnement :

![Architecture Proof of Concept](https://github.com/yyoan741/Projet_IoT_5A/blob/main/report/images/schema_archi_embarque_1.png)

Nous avons cependant pu rencontrer des problèmes lors de la réalisation de celle-ci. En effet, nous avions décidé de créer un API au serveur en générant son token afin de communiquer avec le serveur home assistant. Mais le codage de QRcode étant impossible à cause de soucis de compatibilité sur Home Assistant, nous avons du abandonner cette solution et repenser à une nouvelle architecture fonctionnelle.

### 3-2 - Mise en place Idéale

Nous avons donc pensé à une autre architecture qui devrait être fonctionnelle mais nous n'avons malheureusement pas eu le temps de la mettre en place à cause de changement de matériel au dernier moment et de la durée de nos essais sur l'architecture précédente.

Cette architecture étant composé cette fois-ci d'une seule Raspberry sous un OS Debian, contenant un docker hébergeant  Home Assistant. Contrairement à une Raspberry utilisant l'OS d'home assistant, il nous est désormais possible d'y exécuter des commandes bash et d'y intégrer nos différents scripts.

![Architecture Solution Idéale](https://github.com/yyoan741/Projet_IoT_5A/blob/main/report/images/schema_archi_embarque_2.png)

## 4- Implémentation logiciel embarqué

### 4-1 - Implémentation Proof of Concept

Après avoir vu son architecture, nous allons désormais étudier le fonctionnement de l'implémentation de notre première Proof of Concept.
Notre objectif était d'effectuer le protocole suivant :

A partir de l'appui sur le bouton branché sur les ports adaptés de la Raspberry, lancer notre script bash comprenant l'exécution de nos deux scripts python. Le premier génère une chaine de caractère aléatoire de 1000 caractères, la crypte à l'aide d'une fonction de hachage et est envoyée au serveur Home Assistant via une requête Python. Cette requête est envoyée à l'API du serveur qui a été généré au préalable.

Le premier script ayant été lancé le second va ensuite être lancé à son tour. Celui-ci va demander à la caméra d'analyser l'image pendant une trentaine de secondes afin de laisser l'utilisateur sortir le QRcode et le montrer.

Celle-ci va ensuite comparer le QRcode repéré et le QR code disponible sur le serveur qui aura été généré via une automatisation sur Home Assistant et ouvrir le portail en fonction du résultat de cette comparaison.

![Implementation Proof of Concept](https://github.com/yyoan741/Projet_IoT_5A/blob/main/report/images/schema_fonction%20embarque_1.png)

Nous avons cependant rencontré un problème de compatibilité entre notre serveur Home Assistant et la fonction permettant de générer des QRcodes sur celui-ci, rendant la réalisation de ce protocole impossible.

Nous avons donc chercher un autre solution afin de générer le QR code directement dans le script Python et de directement l'envoyer à Home Assistant.

### 4-2 - Implémentation Idéale

Pour implémenter nos programmes sur une seule carte contenant aussi le serveur nous avons donc penser à une nouvelle architecture que nous n'avons malheureusement pas eu le temps de mettre place.
Celle-ci consistait à flasher la carte Raspberry avec un OS fonctionnant sous Debian cette fois-ci, et y héberger le serveur home assistant sur un docker.

Le fonctionnement du protocole de cette architecture serait donc semblable au premier mais avec quelques différences tout de mêmes. Le bouton activera toujours le script bash lançant toujours les deux scripts python avec les mêmes timings mais avec un envoi du QR code totalement différent. En effet celui-ci sera cette fois-ci enregistré directement dans le fichier config/www/ contenu dans le docker du home assistant contenant les différents médias, à l'aide des add-ons "file editor" et "samba share".

L'affichage se fera donc directement sur home assistant en cherchant le fichier dans ses fichiers locaux. Le reste du protocole d'effectuera de la même manière que l'architecture précédente.

![Implementation Idéale](https://github.com/yyoan741/Projet_IoT_5A/blob/main/report/images/schema_fonction%20embarque_2.png)

Nous avons eu le temps de tester cette démarche sur l'OS d'Home Assistant implanté sur une des RaspberryPI de notre première Proof of Concept, à la différence que le code pour l'enregistrement du QR code en format jpg s'effectue en local et est transféré à la main dans le fichier config/www/ d'home assistant contenant les médias. Mais celui-ci s'affiche bien dans le Dashboard principal du serveur et donc sur le téléphone avec l'application reliée comme ci-dessous :

![Screenshot_Telephone](https://github.com/yyoan741/Projet_IoT_5A/blob/main/report/images/Screeshot_smartphone.jpg)

## 5 - Format des messages

Nous avons dans un premier temps utilisé des formats Json composés de headers contenant l'url de la requête, l'api_token pour être autorisé a communiquer avec l'API du serveur, ainsi que le payload a envoyer contenant la data.

Etant passé sur un script Python, l'envoi du QR code s'effectue en enregistrant directement l'image jpg de celui-ci dans le fichier media de Home Assistant (fichier config/www/) qui sera donc récupérer directement dans ce répertoire.

En ce qui concerne la caméra, la communication s'effectue en filaire et envoi des trames spécifiques en liaison série.

## 6 - Sécurité globale

### 6-1 - Menaces identifiées

Ces architectures et ces connexions sont très utiles mais représentent aussi des failles dans la sécurité de notre système. Nous allons dans un premier temps y identifier les menaces potentielles.

L'un des principaux problèmes se trouve dans l'utilisations de nos services tiers. En effet toute leur failles respectives se répercuterons directement sur notre système devenant instable à son tour.

Un menace se trouve aussi lors de la connexion au serveur de home assistant, si une personne malveillante arrive à se connecter à notre serveur en contournant les protections afin de l'utiliser pour un usage malveillant. Ce même danger peut se répercuter sur le réseau Wifi qui pourrait être accessible au malfaiteur.

De nombreux danger se trouvent aussi dans les échanges de QR codes. En effet, celui-ci pourrait être reproduit ou rediriger vers une autre entité afin de rentrer dans l'habitat à la place de l'utilisateur. Ce QR code pourrait aussi être soumis à des attaques de types Man in the Middle afin d'être intercepté lors de l'échange. Un QR code malveillant redirigeant vers un site web frauduleux peut aussi devenir un problème si cette possibilité n'est pas traité dans le programme de reconnaissance.

Un autre danger serait l'obtention des logs contenant des informations sur l'utilisateur et les lieux et date d'entrée dans l'habitat.

### 6-2 - Solutions possibles

Après avoir observer les différentes failles, nous allons désormais observer comment se protéger contre celles-ci.
Afin de protéger notre QR_code contre de potentielles reproductions, celui-ci est codé par une chaine de 1000 caractères générée aléatoirement puis cryptée par une fonction de hachage avant d'être encodée (solution mise en place lors de notre test). Nous pourrions mettre en place à long terme d'autres algorithmes de cryptages plus puissants comme l'ED25519.

Afin d'éviter aux utilisateurs ou a des personnes malveillantes d'accéder aux appareils connectés de l'utilisateur principale, un compte invité peut être mis en place ne donnant accès qu'au QR code avec des identifiants et un mot de passe changeant régulièrement.
Nous pourrions voir d'autres méthodes pour renforcer la sécurité lors de l'échange comme la mise en place de clés privées et public ou encore de QR code temporaires.

Des méthodes pouvant sembler évidentes mais très efficaces et à ne pas oublier comme l'utilisation d'identifiants et de mots de passe fiables et sécurisés pour le serveur, la mise à jour régulière des logiciels afin de lutter contre les diverses vulnérabilités de logiciels tierces ou encore d'utiliser des méthodes de sécurité pour le WIFI comme le WPA2, WPA3, l'installation d'un pare-feu ou d'une connexion SSL.

## 7 - Bill of Materials
<div align="center">

| Produit | Quantité par produit  | Prix (€) pour 5000 unités (HT) | Prix (€) unitaire (HT) |
|--|--|--|--|
| Raspberry Pi 3 B | 1 | 200000 | 40 (estimé) |
| PiCamera  | 1 | 109100 | 21,82 |
| PiCamera  | 1 | 82900 | 16,58 |
| Boite hermétique | 1 | 10000 | 2 |
| Wio Terminal | 1 | 200000 | 40 |

</div>

Prix total pour 5000 unités HT : 602000 €

Prix unitaire HT : 120,40 €

Ces prix ne sont pourtant pas réalistes car dans le cas de la création d’un produit, une Raspberry Pi avec une Pi Camera et un Wio Terminal ne sont pas adaptées. Ces composant sont complets et l’utilisation qu’en fait notre produit est largement sous dimensionné par rapport à leurs capacités.

Une nette réduction des prix est possible en réalisant un PCB personnalisé en utilisant uniquement les composants nécessaires. Un PCB sur mesure couterait autour de 500 € pour 5000 unités, composants exclus. Cela reviendrait à 10 centimes par unités. De même, un écran et une caméra seuls permettraient aussi de baisser largement les coûts. Ainsi, on peut espérer baisser le coût de fabrication d’une unité à une cinquantaine d’euros.

## 8 - Vie privée du service (RGPD)

Après avoir observé la protection de notre logiciel, il est aussi import de vérifier la protection des données utilisateurs et donc respecter les lois du RGPD (Règlement Général sur la Protection des Données).

Dans les cadre de notre système, certaines données peuvent être enregistrées par l'utilisateur comme son image enregistrée par la caméra en attendant la reconnaissance du QR code, les logs indiquant quel utilisateur est rentré dans l'habitat et à quelle heure, ou encore les identifiants et mots de passe de l'utilisateur pour son compte potentiel.

Dans ce cas, il est important d'assurer :
La transparence à propos de l'utilisation des données enregistrées  et la bonne gestion de celles-ci.
Il est important aussi de préciser que es données de la caméra ne seront pas enregistrées mais seulement traitées par notre programme de reconnaissance de QR code et que les logs ainsi que les identifiants et mots de passe seront correctement protégés et non utilisés ou vendus à un tierce.

## 9 - Coûts de certifications

- Notre produit utilisant uniquement des connexions WIFI privées, des certifications ne seront pas nécessaires à ce niveau.

- Au niveau des différentes certifications ETSI, nous n'avons utilisés que des composants déjà certifiés et fiables (comme les RaspberryPI) et n'en avons développé aucun nécessitant une expertise à ce niveau non plus.

## 10- Métrique du logiciel (on verra plus tard ensemble)

Notre code est majoritairement fait de python. Nous utilisons principalement des librairies. Notre produit instancie à côté Home Assisstant OS,

Nombre de lignes de code :
- Capture_decode.py : **23**
- genere_QR.py : **18**
- Script Bash : **3**
- Total : **44 lignes de codes**

## 11 - Temps d'exécutions

Nous allons désormais calculer le temps d'exécution de notre processus à l'aide de la librairie time de python nous permettant de mesurer le temps :
- script bash :
	- programme genere_QR.py : **0,049s**
	- programme capture_decode.py : **12,18s** + **30s** pour que l'utilisateur ai le temps de monter le QR code.

- mise à jour du QR code sur le serveur comprise dans le genere_QR.py car enregistrement du fichier dans base de donnée locale.

- Durée totale du protocole : **42,68 secondes**

## 12 - Durée de vie

On suppose que l'on intègre un système de mise en veille de notre dispositif, durant lequel la consommation peut être négligée.

En considérant une utilisation journalière d'une durée de 4 minutes et une consommation de la Raspberry Pi avec la caméra à 600mA, sur 1 mois (31 jours) on aurait : **600 * (4/60) * 31 = 1240 mAh/mois**

En choisissant une batterie de **5000mAh**, le produit peut ainsi être alimenté convenablement durant **4 mois**. Cette autonomie est tout à fait satisfaisante pour une utilisation quotidienne.

## 13 - Cycle de vie du produit

La récupération des matières de notre produit est très polluante. Nous utilisons du **plastique** pour la fabrication du boitier (extraction et raffinage de pétrole) ainsi que des **terres rares** et des métaux issus du minage pour les composants électroniques (silicium, or, cuivre, etc.).

La fabrication et le transport de notre produit vers les points de vente serait là aussi polluant. Dans le cas où la production se ferait en Chine, la pollution associée serait plus grande qu’elle pourrait l’être en France.

A l’utilisation, notre serrure connectée consomme de l’électricité pour alimenter les composants et communiquer avec les réseaux. La pollution à ce niveau est alors faible (la consommation est faible compte-tenu du produit) et dépend du **mode de production de l’électricité** (nucléaire en France, au charbon en Allemagne, etc.).

La fin de vie de notre produit n’est malheureusement pas bien maitrisée. Certains composants électroniques ne sont aujourd’hui **pas recyclables** (écrans, circuits intégrés). Certaines parties comme les métaux et les plastiques (PCB et boitier) peuvent se recycler, limitant l’impact sur l’environnement de cette étape de vie.

## 14 - Comparaison contre la concurrence
<div align="center">

|  | Concurence|Notre produit |
|--|--|--|
| Prix (€ TTC en France) | 175 | 75 |
| Connectivité | Wifi, Bluetooth, ZigBee, Autres | Wifi |
| Verrouillage à distance | Oui | Non |
| Invitations | Oui | Oui |
| Historique des accès | Oui | Oui |

</div>

Les fonctionnalités disponibles avec notre produit sont moindres que celles des produits actuellement sur le marché. Cependant, le prix que nous serions capables de proposer est largement inférieur. Ainsi, notre produit serait une opportunité d’**entrée de gamme** très crédible.

## 15 - Intégrations effectuées

- stack editor (markdown editor)
- github pour le répertoire du projet
- home assistant OS : 9.4
	-  file editor : 5.4.2
	- samba share : 10.0.0
	- studio code server : 5.5.1
- Python : 3.10.6
	- qrcode
	- requests
	- json
	- Pillow
	- random
	- time
	- string
	- PiCamera
	- cv2

## Documentation et Sources
- Etude de marché
	- https://www.serrure-connectee.fr/
	- https://www.frandroid.com/guide-dachat/guide-dachat-maison-connectee/840576_quelles-sont-les-meilleures-serrures-connectees-en-2021
	- https://www.infoprotection.fr/des-serrures-connectees-de-seconde-generation/
	- https://www.mordorintelligence.com/fr/industry-reports/smart-lock-market
	- Bill Of Materials
	- https://fr.rs-online.com/web/p/cameras-pour-raspberry-pi/9132664
	- https://www.gotronic.fr/art-wio-terminal-31802.htm
	- https://www.gotronic.fr/art-batterie-externe-usb-57975-35475.htm
	- https://jlcpcb.com/
- Durée de Vie
	- https://www.raspberryme.com/donnees-de-consommation-electrique-du-raspberry-pi/
	- Forums divers
- Analyse du cycle de Vie
	- https://www.geo.fr/environnement/definition-terres-rares-scandium-yttrium-et-lanthanides-124433
	- https://www.insu.cnrs.fr/fr/cnrsinfo/les-terres-rares-le-paradoxe-environnemental
	- https://bpsuperfioul.fr/plastique-fabrication/
	- https://www.ecologie.gouv.fr/transition-energetique-en-france
	- https://www.hellocarbo.com/blog/reduire/recyclage-plastique/
	- https://fr.rs-online.com/web/generalDisplay.html?id=i/dechets-electriques-et-electroniques
- Vulnérabilités :
	 - https://itsocial.fr/enjeux-it/enjeux-tech/iot-edgecomputing/top-5-vulnerabilites-objets-connectes/
	- Cours IESE-5 - Cybersécurité

- Certifications :
	- https://fr.wikipedia.org/wiki/European_Telecommunications_Standards_Institute
	- https://www.lembarque.com/produits/outil-de-developpement-de-fonctions-de-securite-sur-des-microcontroleurs-de-nxp

- RGPD :
	- https://www.cnil.fr/fr/reglement-europeen-protection-donnees
	- https://donnees-rgpd.fr/traitement-donnees/securisation-iot-rgpd/
