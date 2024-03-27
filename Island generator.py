import numpy as np
import matplotlib.pyplot as plt

            
def addmontagne():
    taille = 200
    matrice = np.zeros((taille,taille))
    print(matrice)

    graines = []
    for l in range(0,1):
        x = np.random.randint(0,taille)
        y = np.random.randint(0,taille)
        z = np.random.randint(300,500)
        matrice[x, y] = z
        graines.append([x,y])
   
    i = [i for i in range(0,taille)]
    j = [j for j in range(0,taille)]


    largeur = np.random.rand(1)
    for ii in i:
        for jj in j:
            if ii == graines[0][0] and jj == graines[0][1]:
                pass
            else:
                dist = np.sqrt( (-graines[0][0]+ii)**2 + (-graines[0][1]+jj)**2)
                matrice[ii][jj] = matrice[graines[0][0]][graines[0][1]]/(dist**largeur)
    return(matrice)

matrice_f = np.zeros((200,200))


nb_sommet = 15
for i in range(0,nb_sommet):
    e = addmontagne()
    matrice_f += e 

           
plt.imshow(matrice_f, cmap='terrain', interpolation='nearest')
plt.colorbar()
plt.grid(True)
plt.show()


