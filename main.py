#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.commis.batteur import BatteurOeufs
from src.commis.fondeur import FondeurChocolat
from src.ingredients.chocolat import Chocolat
from src.ingredients.oeuf import Oeuf
from src.recipients.cul_de_poule import ConcretRecipient


class Verseur:
    pass


def main():
    # Recipients
    cul_de_poule_pour_les_oeufs = ConcretRecipient("Cul de poule")
    bol_pour_le_chocolat_1 = ConcretRecipient("Bol")
    bol_pour_le_chocolat_2 = ConcretRecipient("Bol")

    # Ingredients
    oeufs = Oeuf(6, "unite")
    chocolat = Chocolat(200, "g")

    # Commis
    batteur = BatteurOeufs(oeufs, cul_de_poule_pour_les_oeufs)
    fondeur_chocolat_1 = FondeurChocolat(chocolat, bol_pour_le_chocolat_1)
    fondeur_chocolat_2 = FondeurChocolat(chocolat, bol_pour_le_chocolat_2)
    verseur_1 = Verseur()
    verseur_1 = Verseur()

    # Process

    batteur.start()
    fondeur_chocolat_1.start()
    fondeur_chocolat_2.start()

    batteur.join()
    fondeur_chocolat_1.join()
    fondeur_chocolat_2.join()

    print("\nJe peux à présent incorporer le chocolat aux oeufs\n")

    print(bol_pour_le_chocolat_1)
    print(bol_pour_le_chocolat_2)
    print(cul_de_poule_pour_les_oeufs)


if __name__ == "__main__":
    main()
