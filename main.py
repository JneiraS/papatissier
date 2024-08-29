#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.commis.batteur import BatteurOeufs
from src.commis.fondeur import FondeurChocolat
from src.commis.verseurs import Verseurs
from src.ingredients.chocolat import Chocolat
from src.ingredients.oeuf import Oeuf
from src.recipients.concret_recipients import ConcretRecipient



def main():
    # Recipients
    cul_de_poule_pour_les_oeufs = ConcretRecipient("Cul de poule")
    bol_pour_le_chocolat_1 = ConcretRecipient("Bol")
    bol_pour_le_chocolat_2 = ConcretRecipient("Bol")

    # Ingredients
    oeufs = Oeuf(6, "unite")
    chocolat_1 = Chocolat(200, "g")
    chocolat_2 = Chocolat(200, "g")

    # Commis
    batteur = BatteurOeufs(oeufs, cul_de_poule_pour_les_oeufs)
    fondeur_chocolat_1 = FondeurChocolat(chocolat_1, bol_pour_le_chocolat_1)
    fondeur_chocolat_2 = FondeurChocolat(chocolat_2, bol_pour_le_chocolat_2)
    verseur_1 = Verseurs(bol_pour_le_chocolat_1, cul_de_poule_pour_les_oeufs)
    verseur_2 = Verseurs(bol_pour_le_chocolat_2, cul_de_poule_pour_les_oeufs)

    # Process
    batteur.start()
    fondeur_chocolat_1.start()
    fondeur_chocolat_2.start()

    batteur.join()
    fondeur_chocolat_1.join()
    fondeur_chocolat_2.join()

    print("\nJe peux à présent incorporer le chocolat aux oeufs\n")

    verseur_1.start()
    verseur_2.start()

    verseur_1.join()
    verseur_2.join()

    print(cul_de_poule_pour_les_oeufs.sum_of_quantite())


if __name__ == "__main__":
    main()
