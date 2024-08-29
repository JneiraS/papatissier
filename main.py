#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.commis.batteur import BatteurOeufs
from src.commis.fondeur import FondeurChocolat
from src.ingredients.chocolat import Chocolat
from src.ingredients.oeuf import Oeuf
from src.recipients.cul_de_poule import CulDePoule


def main():
    # Recipients
    cul_de_poule_pour_les_oeufs = CulDePoule("Cul de poule")
    cul_de_poule_pour_le_chocolat = CulDePoule("Cul de poule")

    # Ingredients
    oeufs = Oeuf(6, "unite")
    chocolat = Chocolat(200, "g")

    batteur = BatteurOeufs(oeufs.quantite, cul_de_poule_pour_les_oeufs)
    fondeur = FondeurChocolat(chocolat.quantite, cul_de_poule_pour_le_chocolat)
    batteur.start()
    fondeur.start()
    batteur.join()
    fondeur.join()
    print("\nJe peux à présent incorporer le chocolat aux oeufs")


if __name__ == "__main__":
    main()
