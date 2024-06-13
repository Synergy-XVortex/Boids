# Projet Boids Simulation
Le projet Boids Simulation est une application Python utilisant la bibliothèque Pygame pour simuler le comportement de vol d'un groupe de boids, inspiré par le modèle de comportement de Craig Reynolds. Les boids sont des objets autonomes qui suivent des règles simples pour se déplacer collectivement de manière réaliste dans un environnement 2D.

# Fichiers Principaux
1. main.py
    - Description : Point d'entrée de l'application. Gère l'initialisation de Pygame, crée la fenêtre de simulation, et gère les événements utilisateur et l'interface graphique.
    - Fonctionnalités Clés :
        - Initialisation de la fenêtre Pygame en plein écran.
        - Gestion des événements (clavier, souris) pour contrôler la simulation et l'interface utilisateur.
        - Affichage des boids à l'écran et mise à jour de leur comportement en fonction des règles définies.

2. boids.py
    - Description : Contient la définition de la classe Boid, qui représente un boid individuel dans la simulation.
    - Fonctionnalités Clés :
        - Définition des propriétés du boid telles que position, vitesse, accélération, couleur, etc.
        - Implémentation des comportements de séparation, alignement et cohésion pour les boids.
        - Limitation des déplacements des boids à l'intérieur des limites de la fenêtre de simulation.
        - Calcul et mise à jour de la position et de la vitesse du boid en fonction de son comportement.

3. constants.py
    - Description : Fichier contenant les constantes utilisées dans le projet.
    - Fonctionnalités Clés :
        - Définition des dimensions de la fenêtre de simulation (Width, Height).
        - Définition des couleurs utilisées (white, black).
        - Définition de la taille de la fenêtre de simulation (size).

4. matrix.py
    - Description : Implémente les opérations matricielles nécessaires pour la projection 3D des boids dans la simulation 2D.
    - Fonctionnalités Clés :
        - Multiplication de matrices pour les transformations 3D à 2D.
        - Rotation des vecteurs selon les axes X, Y et Z pour la projection.

5. tools.py
    - Description : Contient des fonctions utilitaires et la définition de la classe Vector pour les opérations vectorielles.
    - Fonctionnalités Clés :
        - Définition de la classe Vector pour manipuler les coordonnées et effectuer des opérations vectorielles.
        - Fonctions pour calculer la distance entre deux vecteurs, additionner, soustraire et normaliser des vecteurs.

6. ui.py
    - Description : Implémente l'interface utilisateur (UI) pour la simulation des boids.
    - Fonctionnalités Clés :
        - Définition des boutons, des panneaux et des éléments d'interface utilisateur pour contrôler les paramètres de la simulation.
        - Gestion des événements de souris pour interagir avec les éléments d'interface utilisateur et modifier les paramètres des boids.

7. uiParameters.py
    - Description : Définit les paramètres et les éléments d'interface utilisateur spécifiques utilisés dans la simulation.
    - Fonctionnalités Clés :
        - Définition des valeurs par défaut et des plages pour les paramètres tels que la séparation, l'alignement, la cohésion et le nombre de boids.
        - Définition des curseurs, des entrées de chiffres et des boutons de basculement pour ajuster les paramètres de simulation.

# Fonctionnement de la Simulation
    - Initialisation : La simulation démarre en initialisant un nombre défini de boids à des positions aléatoires à l'intérieur des limites de la fenêtre.
    - Comportements des Boids : Chaque boid suit trois règles simples :
        - Séparation : Éviter la collision avec les autres boids en ajustant sa direction.
        - Alignement : Ajuster sa vitesse pour correspondre à celle des boids voisins.
        - Cohésion : Se regrouper vers le centre de masse des boids voisins.
    - Mise à Jour : À chaque itération de la boucle principale, les positions et les comportements des boids sont mis à jour en fonction des règles définies.
    - Interface Utilisateur : L'interface utilisateur permet à l'utilisateur d'ajuster les paramètres de simulation en temps réel, tels que le nombre de boids, la taille du rayon de voisinage, et les poids des comportements.

# Conclusion
Le projet Boids Simulation démontre l'application du modèle de simulation de comportement de Craig Reynolds à travers une interface graphique interactive, permettant aux utilisateurs d'observer et de contrôler le comportement collectif de boids virtuels dans un environnement simulé.

# Auteur
Ce projet a été développé par Clément Vongsanga. Pour toute question, suggestion ou contribution, n'hésitez pas à ouvrir une issue ou à proposer une pull request sur GitHub.
