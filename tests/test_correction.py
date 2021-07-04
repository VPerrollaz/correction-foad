#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Tests automatique des fonctions de la correction.
"""
from correction.fonctions import (
    est_divisible,
    compte_nombres,
    genere_compteur,
    trie_par_apparition_puis_valeurs,
    prend_les_premiers,
    recupere_frequents,
    genere_mots,
    est_consonne,
    a_double_consonne,
    Tranche,
    calcule_tranche,
    calcule_impots,
    calcule_x,
    genere_branches,
    genere_tronc,
    dessine_sapin,
)
import pytest

# Question 1


def test_positifs_est_divisible():
    """Tests concluant à la divisibilité."""
    assert est_divisible(0, 0)
    assert est_divisible(6, 3)
    assert est_divisible(-15, -3)


def test_negatifs():
    """Tests concluant à la non divisibilité."""
    assert not est_divisible(5, 0)
    assert not est_divisible(11, 5)
    assert not est_divisible(-6, 5)


def test_compte_nombres():
    """Vérifie sur quatre cas."""
    assert compte_nombres(a=0, b=0) == 0
    assert compte_nombres(a=5, b=0) == 0
    assert compte_nombres(a=0, b=15) == 1
    assert compte_nombres(a=10, b=50) == len([15, 21, 30, 35, 42, 45])


# Question 2


def test_genere_compteur():
    """Sur deux cas."""
    assert genere_compteur([]) == dict()
    assert genere_compteur([1, 2, 3, 2, 1, 1]) == {1: 3, 2: 2, 3: 1}


def test_trie_par_apparition_puis_valeurs():
    """Sur deux cas."""
    assert trie_par_apparition_puis_valeurs({}) == []
    assert trie_par_apparition_puis_valeurs({1: 2, 2: 2, 3: 2, 4: 3}) == [
        4,
        1,
        2,
        3,
    ]


def test_prend_les_premiers_positifs():
    """Quand tout se passe bien."""
    assert prend_les_premiers(nbr=0, valeurs=[]) == []
    assert prend_les_premiers(nbr=2, valeurs=[1, 2, 3]) == [1, 2]


def test_prend_les_premiers_problematiques():
    """Lorsqu'il y a incompatibilité."""
    with pytest.raises(ValueError):
        prend_les_premiers(1, [])
    with pytest.raises(ValueError):
        prend_les_premiers(3, [1, 2])


def test_recupere_frequents():
    """Sur quelques cas où tout se passe bien."""
    assert recupere_frequents([1, 2, 1], 1) == [1]
    assert recupere_frequents([1, 1, 1, 2, 2, 4, 3], 3) == [1, 2, 3]


def test_recupere_frequents_erreurs():
    """Dans le cas d'une incompatibilité des arguments."""
    with pytest.raises(ValueError):
        recupere_frequents([], 1)
    with pytest.raises(ValueError):
        recupere_frequents([1], 2)


# Question 3


def test_genere_mots():
    """Quelques cas avec un alphabet restreint."""
    assert genere_mots(nombre_lettres=0, alphabet=list("abc")) == [""]
    assert genere_mots(nombre_lettres=1, alphabet=list("abc")) == list("abc")
    assert genere_mots(nombre_lettres=2, alphabet=["a", "b"]) == [
        "aa",
        "ab",
        "ba",
        "bb",
    ]


def test_est_consonne():
    """Cas d'entrée valide."""
    assert not est_consonne("a")
    assert est_consonne("b")
    assert est_consonne("c")
    assert not est_consonne("y")
    assert est_consonne("z")


def test_est_consonne_problematique():
    """Cas d'entrée respectant la signature mais n'étant pas une seule lettre."""
    with pytest.raises(ValueError):
        est_consonne("")
    with pytest.raises(ValueError):
        est_consonne("aa")


def test_a_double_consonne():
    """Sur quelques cas."""
    assert not a_double_consonne("")
    assert not a_double_consonne("b")
    assert a_double_consonne("bb")
    assert a_double_consonne("abc")
    assert not a_double_consonne("abac")


# Question 4


def test_Tranche():
    """Cas raisonnables."""
    tranche = Tranche(
        limite_basse=10065,
        limite_haute=25659,
        taux_imposition=11,
    )
    assert isinstance(tranche, Tranche)


def test_Tranche_invalides():
    """Teste les cas de figure problématiques."""
    with pytest.raises(ValueError):
        Tranche(limite_basse=10, limite_haute=0, taux_imposition=10)
    with pytest.raises(ValueError):
        Tranche(limite_basse=10, limite_haute=20, taux_imposition=-10)
    with pytest.raises(ValueError):
        Tranche(limite_basse=-10, limite_haute=10, taux_imposition=10)


def test_calcule_tranche():
    """Teste sans arrondi."""
    ma_tranche = Tranche(
        limite_basse=100,
        limite_haute=300,
        taux_imposition=13,
    )
    assert calcule_tranche(revenu=301, tranche=ma_tranche) == 26
    assert calcule_tranche(revenu=200, tranche=ma_tranche) == 13


def test_calcule_tranche_invalide():
    """Argument invalide mais respectant la signature."""
    ma_tranche = Tranche(
        limite_basse=100,
        limite_haute=300,
        taux_imposition=13,
    )
    with pytest.raises(ValueError):
        calcule_tranche(revenu=-100, tranche=ma_tranche)


def test_calcule_impots():
    """Cas raisonnables."""
    assert calcule_impots(10_000) == 0
    assert calcule_impots(20_000) == 1092
    assert calcule_impots(30_000) == 3017
    assert calcule_impots(80_000) == 18745


def test_calcule_impots_invalide():
    """Entrée respectant la signature mais invalide."""
    with pytest.raises(ValueError):
        calcule_impots(-5000)


# Question 5


def test_calcule_x():
    """Vérifie le nombre de x."""
    assert calcule_x(1) == [1, 3, 5]
    assert calcule_x(2) == [1, 3, 5, 3, 5, 7]
    assert calcule_x(3) == [1, 3, 5, 3, 5, 7, 5, 7, 9]


def test_calcule_x_invalide():
    """Teste les valeurs respectant la signature mais invalides."""
    with pytest.raises(ValueError):
        calcule_x(-1)


def test_genere_branches():
    """Cas raisonnables."""
    assert genere_branches([1, 3]) == [" x", "xxx"]


def test_genere_branches_invalides():
    """Teste des valeurs problèmatiques respectant la signature"""
    with pytest.raises(ValueError):
        genere_branches([1, 3, -1])
    with pytest.raises(ValueError):
        genere_branches([1, 3, 2])


def test_genere_tronc():
    """Cas raisonnable."""
    assert genere_tronc(taille=1, largeur_max=5) == " III"
    assert genere_tronc(taille=2, largeur_max=7) == ("  III\n  III")


def test_genere_tronc_invalide():
    """Cas problématique mais respectant la signature."""
    with pytest.raises(ValueError):
        genere_tronc(taille=-1, largeur_max=1)
    with pytest.raises(ValueError):
        genere_tronc(taille=1, largeur_max=1)
    with pytest.raises(ValueError):
        genere_tronc(taille=1, largeur_max=4)


def test_dessine_sapin_1():
    """Pour n=1."""
    assert (
        dessine_sapin(1)
        == """
  x
 xxx
xxxxx
 III
"""
    )


def test_dessine_sapin_2():
    """Pour n=2."""
    assert (
        dessine_sapin(2)
        == """
   x
  xxx
 xxxxx
  xxx
 xxxxx
xxxxxxx
  III
  III
"""
    )


def test_dessine_sapin_invalide():
    """Vérifie les entrées invalides"""
    with pytest.raises(ValueError):
        dessine_sapin(-1)
