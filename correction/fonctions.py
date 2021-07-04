#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Correction de l'examen de python session 1 2020-2021.
"""
from typing import Dict, List
from dataclasses import dataclass

# Question 1


def est_divisible(dividende: int, diviseur: int) -> bool:
    """Vérifie la divisibilité.

    Exemples
    >>> est_divisible(0, 0)
    True
    >>> est_divisible(6, 3)
    True
    >>> est_divisible(-15, -3)
    True
    >>> est_divisible(5, 0)
    False
    >>> est_divisible(11, 5)
    False
    >>> est_divisible(-6, 5)
    False
    """
    if diviseur == 0:
        return dividende == 0
    return dividende % diviseur == 0


def compte_nombres(a: int, b: int) -> int:
    """Renvoie la quantité de nombres entre a et b divisibles par exactement deux nombres dans (3, 5, 7).

    Exemples
    >>> compte_nombres(a=0, b=0)
    0
    >>> compte_nombres(a=5, b=0)
    0
    >>> compte_nombres(a=0, b=15)
    1
    >>> compte_nombres(a=10, b=50)
    6
    """
    DIVISEURS = (3, 5, 7)
    resultat = 0
    for candidat in range(a, b + 1):
        nombre_diviseurs = sum(
            1 for diviseur in DIVISEURS if est_divisible(candidat, diviseur)
        )
        if nombre_diviseurs == 2:
            resultat = resultat + 1
    return resultat


# Question 2


def genere_compteur(nombres: List[int]) -> Dict[int, int]:
    """Compte le nombre de fois où les élements de nombres apparaissent.

    Exemples
    >>> genere_compteur([])
    {}
    >>> genere_compteur([1, 2, 3, 2, 1, 1])
    {1: 3, 2: 2, 3: 1}
    """
    compteur: Dict[int, int] = dict()
    for nombre in nombres:
        compteur[nombre] = compteur.get(nombre, 0) + 1
    return compteur


def trie_par_apparition_puis_valeurs(compteur: Dict[int, int]) -> List[int]:
    """Renvoie les valeurs par nombre d'apparition décroissant et valeurs croissantes.

    Exemples
    >>> trie_par_apparition_puis_valeurs({})
    []
    >>> trie_par_apparition_puis_valeurs({1: 2, 2: 2, 3: 2, 4: 3})
    [4, 1, 2, 3]
    """
    triees = sorted([(-compte, valeur) for valeur, compte in compteur.items()])
    return [valeur for _, valeur in triees]


def prend_les_premiers(nbr: int, valeurs: List[int]) -> List[int]:
    """Prend les nbr premiers éléments de valeurs ou génère une erreur.

    Exemples
    >>> prend_les_premiers(nbr=0, valeurs=[])
    []
    >>> prend_les_premiers(nbr=2, valeurs=[1, 2, 3])
    [1, 2]
    >>> prend_les_premiers(1, [])
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    ValueError: Pas assez d'éléments.
    >>> prend_les_premiers(3, [1, 2])
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    ValueError: Pas assez d'éléments.
    """
    if nbr > len(valeurs):
        raise ValueError("Pas assez d'éléments.")
    return valeurs[:nbr]


def recupere_frequents(nombres: List[int], nbr: int) -> List[int]:
    """Recupere les nbr elements les plus frequents dans nombres.

    Exemples
    >>> recupere_frequents([1, 2, 1], 1)
    [1]
    >>> recupere_frequents([1, 1, 1, 2, 2, 4, 3], 3)
    [1, 2, 3]
    >>> recupere_frequents([], 1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Pas assez d'éléments.
    >>> recupere_frequents([1], 2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Pas assez d'éléments.
    """
    compteur = genere_compteur(nombres)
    triees = trie_par_apparition_puis_valeurs(compteur)
    return prend_les_premiers(nbr, triees)


# Question 3


def genere_mots(nombre_lettres: int, alphabet: List[str]) -> List[str]:
    """Genere les mots avec le nombre de lettres voulues dans l'alphabet.

    Exemples
    >>> genere_mots(nombre_lettres=0, alphabet=list("abc"))
    ['']
    >>> genere_mots(nombre_lettres=1, alphabet=list("abc"))
    ['a', 'b', 'c']
    >>> genere_mots(nombre_lettres=2, alphabet=["a", "b"])
    ['aa', 'ab', 'ba', 'bb']
    """
    if nombre_lettres == 0:
        return [""]
    resultat = list()
    for intermediaire in genere_mots(
        nombre_lettres=nombre_lettres - 1, alphabet=alphabet
    ):
        for lettre in alphabet:
            resultat.append(intermediaire + lettre)
    return resultat


def est_consonne(lettre: str) -> bool:
    """Décide si la lettre est une consonne.

    Exemples
    >>> est_consonne("a")
    False
    >>> est_consonne("b")
    True
    >>> est_consonne("c")
    True
    >>> est_consonne("y")
    False
    >>> est_consonne("z")
    True
    >>> est_consonne("")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Il faut passer UNE lettre.
    >>> est_consonne("aa")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Il faut passer UNE lettre.
    """
    if len(lettre) != 1:
        raise ValueError("Il faut passer UNE lettre.")
    return lettre in "bcdfghjklmnpqrstvwxz"


def a_double_consonne(mot: str) -> bool:
    """Décide si le mot a une double consonne.

    Exemples
    >>> a_double_consonne("")
    False
    >>> a_double_consonne("b")
    False
    >>> a_double_consonne("bb")
    True
    >>> a_double_consonne("abc")
    True
    >>> a_double_consonne("abac")
    False
    """
    for premiere, seconde in zip(mot[:-1], mot[1:]):
        if est_consonne(premiere) and est_consonne(seconde):
            return True
    return False


def compte_mots() -> int:
    """Renvoie le nombre de mots à 5 lettres ayant une double consonne.

    Exemple
    >>> compte_mots()
    10937600
    """
    ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
    return sum(
        1
        for mot in genere_mots(nombre_lettres=5, alphabet=ALPHABET)
        if a_double_consonne(mot)
    )


# Question 4


@dataclass(frozen=True)
class Tranche:
    """Représente une tranche d'imposition.

    Exemple
    >>> ma_tranche = Tranche(
    ...     limite_basse=10065,
    ...     limite_haute=25659,
    ...     taux_imposition=11,
    ... )
    >>> ma_tranche
    Tranche(limite_basse=10065, limite_haute=25659, taux_imposition=11)
    >>> Tranche(limite_basse=10, limite_haute=0, taux_imposition=10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: La limite basse doit être plus petite que la limite haute.
    >>> Tranche(limite_basse=10, limite_haute=20, taux_imposition=-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Le taux d'imposition est FORCEMENT positif.
    >>> Tranche(limite_basse=-10, limite_haute=10, taux_imposition=10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Les limites doivent être positives.
    """

    limite_basse: int
    limite_haute: int
    taux_imposition: int

    def __post_init__(self):
        """Vérifie que la tranche est valide."""
        if self.limite_basse > self.limite_haute:
            raise ValueError(
                "La limite basse doit être plus petite que la limite haute."
            )
        if self.taux_imposition < 0:
            raise ValueError("Le taux d'imposition est FORCEMENT positif.")
        if self.limite_basse < 0:
            raise ValueError("Les limites doivent être positives.")


def calcule_tranche(revenu: int, tranche: Tranche) -> int:
    """Calcule la quantité d'impot à payer pour le revenu et la tranche.

    Exemples
    >>> ma_tranche = Tranche(
    ...     limite_basse=100,
    ...     limite_haute=300,
    ...     taux_imposition=13,
    ... )
    >>> calcule_tranche(revenu=301, tranche=ma_tranche)
    26
    >>> calcule_tranche(revenu=200, tranche=ma_tranche)
    13
    >>> calcule_tranche(revenu=-100, tranche=ma_tranche)
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    ValueError: Le revenu doit être positif.
    """
    if revenu < 0:
        raise ValueError("Le revenu doit être positif.")
    version_float = (
        (min(revenu, tranche.limite_haute) - min(revenu, tranche.limite_basse))
        * tranche.taux_imposition
        / 100
    )
    return int(version_float)


def calcule_impots(revenu: int) -> int:
    """Calcule l'imposition.

            Les tranches sont les suivantes:
            0 - 10064 euros : 0%
            10065 euros - 25659 euros : 11%
            25660 euros - 73369 euros : 30%
            73370 euros - 157806 euros : 41%
            157807 euros - ... : 45%

    Exemples
    >>> calcule_impots(10_000)
    0
    >>> calcule_impots(20_000)
    1092
    >>> calcule_impots(30_000)
    3017
    >>> calcule_impots(80_000)
    18745
    >>> calcule_impots(-5000)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Le revenu doit être positif.
    """
    tranches = [
        Tranche(limite_basse=0, limite_haute=10_064, taux_imposition=0),
        Tranche(limite_basse=10_065, limite_haute=25_659, taux_imposition=11),
        Tranche(limite_basse=25_660, limite_haute=73_369, taux_imposition=30),
        Tranche(limite_basse=73_370, limite_haute=157_806, taux_imposition=41),
        Tranche(
            limite_basse=157_807,
            limite_haute=max(revenu, 157_807),
            taux_imposition=45,
        ),
    ]
    return sum(calcule_tranche(revenu=revenu, tranche=tranche) for tranche in tranches)


# Question 5


def calcule_x(n: int) -> List[int]:
    """Calcule le nombre de x par lignes.

    Exemples
    >>> calcule_x(1)
    [1, 3, 5]
    >>> calcule_x(2)
    [1, 3, 5, 3, 5, 7]
    >>> calcule_x(3)
    [1, 3, 5, 3, 5, 7, 5, 7, 9]
    >>> calcule_x(-1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: n doit être positif.
    """
    if n <= 0:
        raise ValueError("n doit être positif.")
    resultat = list()
    for i in range(n):
        for base in (1, 3, 5):
            resultat.append(2 * i + base)
    return resultat


def genere_branches(x_par_lignes: List[int]) -> List[str]:
    """Dessine les branches.

    Exemples
    >>> genere_branches([1, 3])
    [' x', 'xxx']
    >>> genere_branches([1, 3, -1])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Les entrée doivent être positives.
    >>> genere_branches([1, 3, 2])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Les entrées doivent être impaires.
    """
    resultat = list()
    largeur_max = max(x_par_lignes)
    for nombre_de_x in x_par_lignes:
        if nombre_de_x < 0:
            raise ValueError("Les entrée doivent être positives.")
        if nombre_de_x % 2 != 1:
            raise ValueError("Les entrées doivent être impaires.")
        rembourrage = (largeur_max - nombre_de_x) // 2
        resultat.append(" " * rembourrage + "x" * nombre_de_x)
    return resultat


def genere_tronc(taille: int, largeur_max: int) -> str:
    """Renvoie le tronc.

    Exemples
    >>> genere_tronc(taille=1, largeur_max=5)
    ' III'
    >>> genere_tronc(taille=2, largeur_max=7)
    '  III\n  III'
    >>> genere_tronc(taille=-1, largeur_max=1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: La taille doit être positive.
    >>> genere_tronc(taille=1, largeur_max=1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: La largeur max n'est pas suffisante.
    >>> genere_tronc(taille=1, largeur_max=4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: La largeur max doit être impaire.
    """
    if taille <= 0:
        raise ValueError("La taille doit être positive.")
    nombre_de_I = 3
    if largeur_max < nombre_de_I:
        raise ValueError("La largeur max n'est pas suffisante.")
    if largeur_max % 2 != 1:
        raise ValueError("La largeur max doit être impaire.")
    rembourrage = (largeur_max - nombre_de_I) // 2
    return "\n".join([rembourrage * " " + "I" * nombre_de_I for _ in range(taille)])


def dessine_sapin(n: int) -> str:
    """Renvoie un sapin en ascii.

    Exemples
    >>> dessine_sapin(1)
    '\n  x\n xxx\nxxxxx\n III\n'
    >>> print(dessine_sapin(1))

      x
     xxx
    xxxxx
     III

    >>> dessine_sapin(2)
    '\n   x\n  xxx\n xxxxx\n  xxx\n xxxxx\nxxxxxxx\n  III\n  III\n'
    >>> print(dessine_sapin(2))

       x
      xxx
     xxxxx
      xxx
     xxxxx
    xxxxxxx
      III
      III

    >>> dessine_sapin(-1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: L'argument doit être positif.
    """
    if n <= 0:
        raise ValueError("L'argument doit être positif.")
    x_par_lignes = calcule_x(n)
    branches = "\n".join(genere_branches(x_par_lignes))
    tronc = genere_tronc(taille=n, largeur_max=max(x_par_lignes))
    return "\n" + branches + "\n" + tronc + "\n"
