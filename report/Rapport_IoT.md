Lors de ce projet nous allons essayer de mettre en place un système d'ouverture de porte via un QRcode généré

##  1 - Analyse du marché (Yoan)

**analyse (rapide) du marché des produits commerciaux concurrents**
Le marché des serrures connectées est en croissance rapide. La demande pour les systèmes de sécurité de domicile augmente fortement. La fonctionnalité majeure est la possibilité de verrouiller et déverrouiller à distance à l'aide d'un smartphone. Les principaux acteurs sur ce marché sont August, Schlage et Yale. Le marché de ce secteur était estimé à 3,1 milliards de dollars en 2020 et pourrait atteindre 8 milliards en 2026. La croissance de ce marché devrait principalement se trouver en Asie et de manière plus modérée en Europe et en Amérique du Nord. Les prévisions de croissance à long terme pour ce marché sont positives. Les serrures connectées peuvent être connectées à des systèmes de domotique pour une intégration encore plus complète (Google Home, Amazon Alexa, etc).

L’essor de ce marché est notamment lié aux services de location de logement sur courte durée (notamment AirBnB) car il permet facilement de sécuriser son domicile à distance. De plus, ce type de dispositif peut également s’intégrer aux résidences étudiantes ayant un fort turn-over des locataires.

Les principales caractéristiques des serrures des fabricants cités sont :
- Un prix commençant autour de 150 – 200 €
- La possibilité de verrouiller et déverrouiller à distance à l'aide d'un smartphone via une application dédiée
- La possibilité de donner des accès temporaires à des invités
- Un historique des accès
- Le verrouillage automatique

## 2 - Architecture globale du système (Yoan)

**(ensemble d’objets, service en ligne (cloud))**
![Architecture envisagée](https://github.com/yyoan741/Projet_IoT_5A/blob/main/report/images/Archi_envisag%C3%A9e.png)
## 3 - Sécurité globale (Arnaud)

**(clé de chiffrage),**

## 4 - Vie privée du service (RGPD) (Arnaud)

**définir le respect de la vie privée du service ([RGPD](https://www.cnil.fr/fr/reglement-europeen-protection-donnees)) : lister les risques d’atteinte au respect de la vie privée**

## 6 - Bill of Materials (Yoan)

Une nomenclature, Bill of Materials ou BOM, est **une liste complète des matières premières, des pièces et des outils nécessaires pour fabriquer un produit donné**.

-   estimer le coût de la BOM de votre produit (composants, PCB et enclosure) pour 5000 unités produites

-   pour le boitier, vous pouvez rechercher des boitiers “standards” disponibles dans les catalogues fournisseurs

pour le PCB, vous pouvez fournir une estimation du prix de fabrication du PCB et du masque chez des fournisseurs comme [https://jlcpcb.com/](https://jlcpcb.com/) , [https://www.wedirekt.fr/fr/](https://www.wedirekt.fr/fr/) …

| Produit | Quantité par produit  | Prix (€) pour 5000 unités (HT) | Prix (€) unitaire (HT) |
|Raspberry Pi 3 B|1| 200000| 40 (estimé)|
|PiCamera  |1| 109100 | 21,82|
|Boite hermétique|1|10000|2|
|Wio Terminal|1|200000|40|


Prix total pour 5000 unités HT : 555835 €

Prix unitaire HT : 111,57 €

Ces prix ne sont pourtant pas réalistes car dans le cas de la création d’un produit, une Raspberry Pi avec une Pi Camera ne sont pas adaptées. Ces composant sont complets et l’utilisation qu’en fait notre produit est largement sous dimensionné par rapport à leurs capacités.

Une nette réduction des prix est possible en réalisant un PCB personnalisé en utilisant uniquement les composants nécessaires. Un PCB sur mesure couterait autour de 500 € pour 5000 unités, composants exclus. Cela reviendrait à 10 centimes par unités. De même, un écran et une caméra seuls permettraient aussi de baisser largement les coûts. Ainsi, on peut espérer baisser le coût de fabrication d’une unité à une cinquantaine d’euros.

## 7 - Coûts de certifications (Arnaud)
**estimer le coût de certification ETSI du produit, le coût de [certification LoRa Alliance](https://lora-alliance.org/lorawan-certification/) du produit ...**


## 10- Définition logiciel embarqué (Arnaud)

**définir le logiciel embarqué de l’objet.**
## 8- Implémentation logiciel embarqué (Arnaud)

**proposer une implémentation du logiciel embarqué de l’objet défini.**

## 9 - Format des messages (Arnaud)

**définir/documenter le format des messages uplink et downlink échangés (dans le cas des objets LoRaWAN, privilégiez le format LPP)**


## 11- Métrique du logiciel (on verra plus tard ensemble)

- **donner les métriques logiciel du logiciel embarqué (nombre de lignes de code, taille du binaire du firmware ie le fichier .bin)**

- **compter le nombre de lignes de code développé (coté objet, coté application) avec un outil comme [cloc](https://github.com/AlDanial/cloc). Précisez les langages et les outils utilisés (git, arduino-cli …)**

## 12 - Temps d'exécutions (on verra)

-   Instrumenter le logiciel embarqué pour mesurer les différents temps d’exécution des principales phases d’exécution (par exemple: durée d’une prise de photo, écriture sur carte SD, inférences avec un réseau de neurones …)
-   Prévoir de montrer la trace console de l’objet pendant la démonstration.

## 13 - Durée de vie (on verra)

**estimer la durée de vie de la batterie de l’objet (pour LoRaWAN en fonction du datarate comme avec l’outil [https://www.elsys.se/en/battery-life-calculator/](https://www.elsys.se/en/battery-life-calculator/)**

## 14 - Cycle de vie du produit (Yoan)

**réaliser une analyse (brève) du cycle de vie du produit “durable” et “[sobre](https://www.youtube.com/watch?v=aX_tzI7w7Qo)” ([ACV](https://fr.wikipedia.org/wiki/Analyse_du_cycle_de_vie))**

La récupération des matières de notre produit est très polluante. Nous utilisons des terres rares pour la fabrication du boitier (pétrole pour le plastique) ainsi que les composants électroniques (silicium, or, cuivre, etc.).

La fabrication et le transport de notre produit vers les points de vente serait là aussi polluant. Dans le cas où la production se ferait en Chine, la pollution associée serait plus grande qu’elle pourrait l’être en France.

A l’utilisation, notre serrure connectée consomme de l’électricité pour alimenter les composants et communiquer avec les réseaux. La pollution à ce niveau est alors faible (la consommation est faible compte-tenu du produit) et dépend du mode de production de l’électricité (nucléaire en France, au charbon en Allemagne, etc.).

La fin de vie de notre produit n’est malheureusement pas bien maitrisée. Certains composants électroniques ne sont aujourd’hui pas recyclables (écrans, circuits intégrés). Certaines parties comme les métaux et les plastiques (PCB et boitier) peuvent se recycler, limitant l’impact sur l’environnement de cette étape de vie.

## 15 - Comparaison contre la concurrence (Yoan)

-  rechercher et analyser (avantages/inconvénients sous la forme d’une grille) des produits concurrent

||Concurence|Notre produit|
|Prix (€ TTC en France)|175|75|
|Connectivité|Wifi, Bluetooth, ZigBee, Autres|Wifi|
|Invitations|Oui|Oui|
|Historique des accès|Oui|Oui|

Les fonctionnalités disponibles avec notre produit sont moindres que celles des produits actuellement sur le marché. Cependant, le prix que nous serions capables de proposer est largement inférieur. Ainsi, notre produit serait une opportunité d’entrée de gamme très crédible.

## 16 - Intégrations effectuées (Arnaud)

**montrer les intégrations effectuées (cayenne, influxdb, home assistant, jupyter notebook …)**

## Documentation / Sources
- https://www.serrure-connectee.fr/
- https://www.frandroid.com/guide-dachat/guide-dachat-maison-connectee/840576_quelles-sont-les-meilleures-serrures-connectees-en-2021
- https://www.infoprotection.fr/des-serrures-connectees-de-seconde-generation/
- https://www.mordorintelligence.com/fr/industry-reports/smart-lock-market
- https://fr.rs-online.com/web/c/raspberry-pi-arduino-outils-de-developpement/boutique-raspberry-pi/
- https://www.gotronic.fr/art-wio-terminal-31802.htm
- https://jlcpcb.com/



Pour les différents schémas : **[Plantuml](https://github.com/donsez/bd/tree/main/plantuml#readme)**

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTkwMDQ4OTc0MCwtMTk5MTc3MDY2NiwxMj
c0NDEyMzM0LC0zMDQ5Mzg5ODcsNzMwOTk4MTE2XX0=
-->
