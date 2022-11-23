# Python-M2-ISF-2022
Cours de Python pour l'Université Paris-Dauphine, Master 280, promotion 2022-2023.

## Séance 1
* **Estimation** : estimation de l'espérance de gain d'un jeu. Travaille les notions de listes, opérations arithmétiques et boucles. Le cas récursif n'est pas traité. Le but de l'exercice est d'insister sur la modularité et la lisibilité du code.
* **PrimeDecomposition** : décomposition en facteurs premiers d'un nombre renseigné par l'utilisateur. Le code n'est pas voulu optimal mais il doit être très lisible et très modulaire. L'optimisation en temps est laissée en exercice.


## Séance 2
* **Brownian Motion** : génération de mouvement brownien. Travail autour de la librairie numpy en surface, librairie matplotlib également. Le but de l'exercice est de fournir un code propre pour être réutilisé pour d'autres usage. On y définie les fonctions modélisant le payoff d'un call et d'un put pour en suite estimer le prix sur une *action* qui aurait comme modélisation un mouvement brownien.
* **Gradient Descent** : programmation d'une descente de gradient avec ou sans momentum en travaillant à nouveau la programmation fonctionnelle et les graphiques.



## Séance 3
* **Suite Logistique et chaos** : représentation de la suite logistique. Travail autour des listes, des librairies numpy et matplotlib. A nouveau on travaille l'autonomie dans la recherche et la créativité, toujours servie par un code modulaire et très lisible.


## Séance 4
* **Payoff** : permet de visualiser à partir d'une liste d'opérations le profil de gain/perte d'une stratégie d'option. Les données sont prise à partir de données réelle via YahooFinance. Un exemple du rendu est disponible dans le fichier *Résultats visuel*. Le but de la séance est de maîtriser pleinement les librairies de visualisation et de commencer la compréhension visuelle et sensible des stratégies d'options pour les futurs cours du master.


## Séance 5
* **Decorator** : utilisation d'un décorateur pour exploiter le cache lors de l'appel d'une fonction Python. Le but de l'exercice est de découvrir la notion de décoration et d'exploiter d'autres manières de travailler en programmation fonctionnelle.
* **Args et Kwargs** : *(à venir)* 


## Séance 6
* **CryptoPortofolio** : définition d'un portefeuille de crypto monnaie dont la valeur est actualisée en temps réel. Travail avec une API, découverte de la notion de classe et bonne pratique entre programmation orientée objet et fonctionnelle.



### Bonus
Notions intéressantes que nous aurions pu traiter en cours si nous avions plus de temps, par défaut et pour un travail personnel :
* **Arithmetic_Progression_Prime** : on s'inspire du théorème de Green-Tao pour traiter des progressions arithmétique à l'intérieur de l'ensemble des nombres premiers. L'exercice fait travailler la compréhension d'un sujet a priori compliqué ainsi que la qualité de code (modularité, libisilité).
* **Mertens Conjecture** : travail autour de la conjecture de Mertens. L'exercice est de comprendre les notions et y associé un code lisible. La visualisation est peu challengente, mais la culture mathématiques sur cet exemple est intéressante. Le code est en **Julia** pour des raisons de performance, l'exercice n'est donc pas résolu en Python, c'est laissé à l'étudiant.
