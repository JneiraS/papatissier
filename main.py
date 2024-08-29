#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.batteur import BatteurOeufs
from src.fondeur import FondeurChocolat
from src.ingredients.chocolat import Chocolat
from src.ingredients.oeuf import Oeuf


def main():
    oeufs = Oeuf(6, "unite")
    chocolat = Chocolat(200, "g")
    batteur = BatteurOeufs(oeufs.quantite)
    fondeur = FondeurChocolat(chocolat.quantite)
    batteur.start()
    fondeur.start()
    batteur.join()
    fondeur.join()
    print("\nJe peux à présent incorporer le chocolat aux oeufs")


if __name__ == "__main__":
    main()
