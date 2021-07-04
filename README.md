# Description

- Correction de l'[examen](./sujet.pdf)
- Projet python standard crée via [poetry](https://python-poetry.org/)
- Le script contenant les solutions est dans [correction](./correction/)
- Le fichier [pyproject.toml](./pyproject.toml) permet de garantir la portabilité des scripts en traçant les versions des paquets de manière automatique.
- Les tests de **toutes** les fonctions sont dans [tests](./tests/)
- On peut exécuter automatiquement les tests via [pytest](https://docs.pytest.org/).
On aura préalablement exécuté `poetry add --dev pytest` pour installer la ressource.
```shell
> poetry run pytest -vv
=================================== test session starts ===================================
platform linux -- Python 3.9.2, pytest-5.4.3, py-1.10.0, pluggy-0.13.1 -- /home/vincent/.cache/pypoetry/virtualenvs/correction-aLaf-vPV-py3.9/bin/python
cachedir: .pytest_cache
rootdir: /home/vincent/projets/COURS/foad/2020-2021/session1/examen1/correction
plugins: cov-2.11.1
collected 28 items

tests/test_correction.py::test_positifs_est_divisible PASSED                        [  3%]
tests/test_correction.py::test_negatifs PASSED                                      [  7%]
tests/test_correction.py::test_compte_nombres PASSED                                [ 10%]
tests/test_correction.py::test_genere_compteur PASSED                               [ 14%]
tests/test_correction.py::test_trie_par_apparition_puis_valeurs PASSED              [ 17%]
tests/test_correction.py::test_prend_les_premiers_positifs PASSED                   [ 21%]
tests/test_correction.py::test_prend_les_premiers_problematiques PASSED             [ 25%]
tests/test_correction.py::test_recupere_frequents PASSED                            [ 28%]
tests/test_correction.py::test_recupere_frequents_erreurs PASSED                    [ 32%]
tests/test_correction.py::test_genere_mots PASSED                                   [ 35%]
tests/test_correction.py::test_est_consonne PASSED                                  [ 39%]
tests/test_correction.py::test_est_consonne_problematique PASSED                    [ 42%]
tests/test_correction.py::test_a_double_consonne PASSED                             [ 46%]
tests/test_correction.py::test_Tranche PASSED                                       [ 50%]
tests/test_correction.py::test_Tranche_invalides PASSED                             [ 53%]
tests/test_correction.py::test_calcule_tranche PASSED                               [ 57%]
tests/test_correction.py::test_calcule_tranche_invalide PASSED                      [ 60%]
tests/test_correction.py::test_calcule_impots PASSED                                [ 64%]
tests/test_correction.py::test_calcule_impots_invalide PASSED                       [ 67%]
tests/test_correction.py::test_calcule_x PASSED                                     [ 71%]
tests/test_correction.py::test_calcule_x_invalide PASSED                            [ 75%]
tests/test_correction.py::test_genere_branches PASSED                               [ 78%]
tests/test_correction.py::test_genere_branches_invalides PASSED                     [ 82%]
tests/test_correction.py::test_genere_tronc PASSED                                  [ 85%]
tests/test_correction.py::test_genere_tronc_invalide PASSED                         [ 89%]
tests/test_correction.py::test_dessine_sapin_1 PASSED                               [ 92%]
tests/test_correction.py::test_dessine_sapin_2 PASSED                               [ 96%]
tests/test_correction.py::test_dessine_sapin_invalide PASSED                        [100%]

=================================== 28 passed in 0.07s ====================================
```
- On peut aussi s'assurer que les tests couvrent l'ensemble du projet grâce à [pytest-cov](https://pypi.org/project/pytest-cov/)
On aura préalablement exécuté `poetry add --dev pytest-cov` pour installer la ressource.
```shell
> poetry run pytest --cov=correction tests/
=================================== test session starts ===================================
platform linux -- Python 3.9.2, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
rootdir: /home/vincent/projets/COURS/foad/2020-2021/session1/examen1/correction
plugins: cov-2.11.1
collected 28 items

tests/test_correction.py ............................                               [100%]

----------- coverage: platform linux, python 3.9.2-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
correction/__init__.py        1      0   100%
correction/fonctions.py     107      2    98%
---------------------------------------------
TOTAL                       108      2    98%


=================================== 28 passed in 0.11s ====================================
```
- On peut aussi vérifier que le typage est consistant en utilisant [mypy](http://mypy-lang.org/)
On aura préalablement exécuté `poetry add --dev mypy` pour installer la ressource.
```shell
> poetry run mypy correction/
Success: no issues found in 2 source files
```
- On peut aussi utiliser un linter tel que [pylama](https://github.com/klen/pylama)
On aura préalablement exécuté `poetry add --dev pylama` pour installer la ressource.
```shell
> poetry run pylama -v correction/
File is reading: correction/fonctions.py
Run pycodestyle {}
Run pyflakes {}
Run mccabe {}
File is reading: correction/__init__.py
Run pycodestyle {}
Run pyflakes {}
Run mccabe {}
correction/fonctions.py:36:80: E501 line too long (106 > 79 characters) [pycodestyle]
correction/fonctions.py:78:80: E501 line too long (86 > 79 characters) [pycodestyle]
```
- On peut finalement utiliser un formatteur automatique de code tel que [black](https://github.com/psf/black)
On aura préalablement exécuté `poetry add --dev black` pour installer la ressource.
```shell
> poetry run black correction/
reformatted correction/__init__.py
reformatted correction/fonctions.py
All done! ✨ 🍰 ✨
2 files reformatted.
```
