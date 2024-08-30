#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.commis.batteur import BatteurOeufs
from src.commis.fondeur import FondeurChocolat
from src.commis.verseurs import Verseurs
from src.ingredients.chocolat import Chocolat
from src.ingredients.oeuf import Oeuf
from src.recipients.concret_recipients import ConcretRecipient


def preparation() -> tuple:
    """
    Fonction qui permet de preparer les commis, les ingredients et les recipients
    """
    # Recipients ----------------
    cul_de_poule_pour_les_oeufs = ConcretRecipient("Cul de poule")
    bol_pour_le_chocolat_1 = ConcretRecipient("Bol")
    bol_pour_le_chocolat_2 = ConcretRecipient("Bol")
    # Ingredients ----------------
    oeufs = Oeuf(6, "unite")
    chocolat_1 = Chocolat(200, "g")
    chocolat_2 = Chocolat(200, "g")
    # Commis ----------------
    batteur = BatteurOeufs(oeufs, cul_de_poule_pour_les_oeufs)
    fondeurs = [FondeurChocolat(chocolat_1, bol_pour_le_chocolat_1),
                FondeurChocolat(chocolat_2, bol_pour_le_chocolat_2)]
    verseurs = [Verseurs(bol_pour_le_chocolat_1, cul_de_poule_pour_les_oeufs), Verseurs(
        bol_pour_le_chocolat_2, cul_de_poule_pour_les_oeufs)]

    return (batteur,
            cul_de_poule_pour_les_oeufs,
            fondeurs,
            verseurs,
            bol_pour_le_chocolat_1, bol_pour_le_chocolat_2)


def main():
    """
    Fonction principale
    """
    batteur, cul_de_poule_pour_les_oeufs, fondeurs, verseurs, bol_1, bol_2 = preparation()

    # Process ----------------
    batteur.start()

    for fondeur in fondeurs:
        fondeur.start()
    for fondeur in fondeurs:
        fondeur.join()

    batteur.join()

    print("\nJe peux à présent incorporer le chocolat aux oeufs\n")

    for verseur in verseurs:
        verseur.start()
    for verseur in verseurs:
        verseur.join()

    # Affichage du resultat ----------------
    print(f"\n On obtient, un {cul_de_poule_pour_les_oeufs}\n")
    print(f" il rest: {bol_1.contient} dans {bol_1.name}")
    print(f" il rest: {bol_2.contient} dans {bol_2.name}")


if __name__ == "__main__":
    main()
