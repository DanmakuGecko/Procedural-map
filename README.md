Générateur d'île, se base sur une superposition de matrices et leur somme et un système de seed (graines) .
![image](https://github.com/DanmakuGecko/Procedural-map/assets/72706524/0e8b9108-eb41-4cca-8d3d-12b0fa9d8699)


Générateur de labyrinthe:
![image](https://github.com/DanmakuGecko/Procedural-map/assets/72706524/bd14cd6e-5434-4e5f-801b-65ac32ecffee)

Pas vraiment fonctionel mais c'est joli


La partie un peu innovant dans mon programme, c'est que le chemin fonctionne avec une liste de probabilité
si il tourne a droite au début, il sera plus susceptible de tourner a droite au prochain tour aussi

mais il faut réequilibrer les probabilité pour que leur somme soit égale à 1 a chaque tour (sinon plantage)
grâce a cet algorithme, ca rend le chemin plus "stable et droit"
pour accentuer cet effet ,il faut juste changer les  P[2] += 0.05 en valeur plus elevée dans les conditions de dirr
si on l'augmente, le chemin va s'adapter plus raipidement, et risque d'être droit 
si on met P[i] += 0 ca sera completement aléatoire.
