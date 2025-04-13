import numpy as np

# 1. Création d'un tableau NumPy (array)

# Création d'un tableau 1D à partir d'une liste Python
liste_1d = [1, 2, 3, 4, 5]
tableau_1d = np.array(liste_1d)
print("Tableau 1D:")
print(tableau_1d)
print(f"Type du tableau: {type(tableau_1d)}")
print(f"Forme du tableau (shape): {tableau_1d.shape}")
print(f"Type des éléments du tableau (dtype): {tableau_1d.dtype}\n")

# Création d'un tableau 2D à partir d'une liste de listes
liste_2d = [[1, 2, 3], [4, 5, 6]]
tableau_2d = np.array(liste_2d)
print("Tableau 2D:")
print(tableau_2d)
print(f"Forme du tableau (shape): {tableau_2d.shape} (2 lignes, 3 colonnes)")
print(f"Nombre de dimensions (ndim): {tableau_2d.ndim}\n")

# Création de tableaux spéciaux
zeros_array = np.zeros((3, 2))  # Tableau de zéros de forme (3, 2)
print("Tableau de zéros:")
print(zeros_array)

ones_array = np.ones((2, 3), dtype=int)  # Tableau de uns de forme (2, 3) avec type entier
print("\nTableau de uns (entiers):")
print(ones_array)

range_array = np.arange(0, 10, 2)  # Tableau de nombres dans une plage (début, fin (exclu), pas)
print("\nTableau avec arange:")
print(range_array)

linspace_array = np.linspace(0, 1, 5)  # Tableau de nombres espacés linéairement (début, fin, nombre d'éléments)
print("\nTableau avec linspace:")
print(linspace_array)

# 2. Opérations sur les tableaux

# Opérations élément par élément
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

addition = a + b
soustraction = b - a
multiplication = a * b
division = b / a
print("\nOpérations élément par élément:")
print(f"Addition: {addition}")
print(f"Soustraction: {soustraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

# Opérations scalaires
scalaire = 2
produit_scalaire = a * scalaire
puissance = a ** scalaire
print("\nOpérations scalaires:")
print(f"Produit scalaire: {produit_scalaire}")
print(f"Puissance: {puissance}")

# Fonctions universelles (ufuncs)
racine_carree = np.sqrt(b)
exponentielle = np.exp(a)
sinus = np.sin(a)
print("\nFonctions universelles:")
print(f"Racine carrée de b: {racine_carree}")
print(f"Exponentielle de a: {exponentielle}")
print(f"Sinus de a: {sinus}")

# 3. Indexation et découpage (slicing)

tableau_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\nTableau 3D:")
print(tableau_3d)
print(f"Forme du tableau 3D: {tableau_3d.shape} (2 plans, 2 lignes, 2 colonnes)")

# Accéder à un élément spécifique
element = tableau_3d[0, 1, 0]  # Premier plan, deuxième ligne, premier élément
print(f"\nÉlément à l'index [0, 1, 0]: {element}")

# Découpage (slicing)
sous_tableau_2d = tableau_3d[0, :, :]  # Premier plan, toutes les lignes et colonnes
print(f"Sous-tableau 2D (premier plan):")
print(sous_tableau_2d)

premiere_colonne = tableau_2d[:, 0]  # Toutes les lignes, première colonne
print(f"\nPremière colonne du tableau 2D: {premiere_colonne}")

# 4. Fonctions d'agrégation

data = np.array([[1, 5, 2], [8, 3, 6]])

somme_totale = np.sum(data)
somme_par_colonne = np.sum(data, axis=0)  # Somme le long des colonnes (axe 0)
somme_par_ligne = np.sum(data, axis=1)    # Somme le long des lignes (axe 1)
moyenne = np.mean(data)
maximum = np.max(data)
minimum = np.min(data)

print("\nFonctions d'agrégation:")
print(f"Somme totale: {somme_totale}")
print(f"Somme par colonne: {somme_par_colonne}")
print(f"Somme par ligne: {somme_par_ligne}")
print(f"Moyenne: {moyenne}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")

# 5. Manipulation de la forme (shape)

tableau_original = np.array([1, 2, 3, 4, 5, 6])
reshaped_array = tableau_original.reshape((2, 3))  # Redimensionner en une matrice 2x3
print("\nManipulation de la forme:")
print(f"Tableau original: {tableau_original}")
print(f"Tableau redimensionné (2x3):\n{reshaped_array}")

flattened_array = reshaped_array.flatten()  # Aplatir le tableau en 1D
print(f"\nTableau aplati: {flattened_array}")