import numpy as np
import matplotlib.pyplot as plt

def box_muller(n):
    U1 = np.random.uniform(0, 1, n)
    U2 = np.random.uniform(0, 1, n)

    R = np.sqrt(-2 * np.log(np.where(U1 > 0, U1, 1e-10)))  # Replace 0 values with a small epsilon (1e-10)

    Theta = 2 * np.pi * U2
    Z = R * np.cos(Theta)

    return Z



#n = int(input("Éntrer le nombre d’échantillons à tester = "))
#alpha = float(input("Éntrer la valeur de alpha paramètre (comprise entre 0 et 1) = ")) 
#var = float(input("Éntrer la valeur attribuée à la variance (entre 0 et 1) = "))
#X = box_muller(n)
#Y = alpha * box_muller(n) + np.sqrt(var) * np.random.randn(n)




def visualize_histograms(X,Y,n, alpha, var):
    X = box_muller(n)
    Y = alpha * box_muller(n) + np.sqrt(var) * np.random.randn(n)
    
    # Affichage de l'histogramme
    plt.hist(Y, bins='auto', alpha=alpha, color='blue')
    
    # Affichage du texte indiquant le nombre d'échantillons
    plt.text(0.5, -0.2, f"Histogrammes des données massives générées correspondant à n = {n}",
             horizontalalignment='center', transform=plt.gca().transAxes)
    
    # Ajout des points sous forme de cercles vides
    plt.scatter(X, Y, marker='o', facecolors='none', edgecolors='red')
  
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f"Histogrammes des données massives générées correspondant à n = {n}")
    
    plt.grid(True)
    plt.show()
    
    
    
lst = [20,50,300,1000,7000]

alpha =0.7
var = 0.5

for n in lst:
    X = box_muller(n)
    Y = alpha * box_muller(n) + np.sqrt(var) * np.random.randn(n)
    visualize_histograms(X,Y,n, alpha, var)
    
    
