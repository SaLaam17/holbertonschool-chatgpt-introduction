#!/usr/bin/python3
import sys

# Vérifier s'il y a des arguments de ligne de commande
if len(sys.argv) > 1:
    # Boucler à travers tous les arguments de la ligne de commande
    for i in range(len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")
else:
    print("Aucun argument de ligne de commande fourni.")
