# Structure d'un Projet Python et Bonnes Pratiques

*Python* est un langage de programmation très polyvalent, utilisé dans divers domaines allant du développement web aux sciences de données en passant par l'automatisation. La structure d'un projet Python peut varier en fonction de son objectif, mais il existe des pratiques courantes qui facilitent l'organisation, la réutilisabilité, et la maintenance du code.

## <u>Objectifs</u>

- Comprendre la structure basique d'un projet *Python*
- Maîtriser l'indentation Python et son importance
- Identifier les différents types de fichiers (standalone, Jupyter notebooks, modules, etc.)
- Apprendre à travailler avec les environnements virtuels
- Explorer l'organisation des modules et des namespaces
- Installer et utiliser Poetry efficacementƒ

## 1. L'indentation en Python

L'indentation en Python n'est pas qu'une question de style - c'est une partie fondamentale de la syntaxe du langage qui définit les blocs de code.

### Règles d'indentation

1. **Consistance** : Utilisez toujours la même indentation dans tout votre code
   - 4 espaces (recommandé par PEP 8)
   - OU des tabulations (déconseillé)
   - JAMAIS un mélange des deux

2. **Structure des blocs** :
```python
def ma_fonction():    # Début du bloc fonction
    x = 1            # Indenté avec 4 espaces
    if x > 0:        # Début du bloc if
        print(x)     # Indenté avec 8 espaces
    return x         # Retour au niveau fonction

class MaClasse:      # Début du bloc classe
    def __init__(self):  # Méthode indentée
        self.x = 1       # Corps de méthode indenté
```

3. **Erreurs courantes à éviter** :
```python
# INCORRECT - Mélange d'espaces et de tabulations
def fonction():
    print("4 espaces")
	print("1 tabulation")  # Erreur!

# INCORRECT - Indentation incohérente
if True:
   print("3 espaces")  # Erreur!
    print("4 espaces")

# CORRECT
def fonction():
    print("4 espaces")
    print("4 espaces")
```

### Configuration de l'éditeur

Pour maintenir une indentation cohérente :
1. Dans VS Code :
   - Allez dans Settings (Ctrl/Cmd + ,)
   - Recherchez "Python Formatting"
   - Activez "Format On Save"
   - Définissez l'indentation à 4 espaces

2. Dans PyCharm :
   - Settings → Editor → Code Style → Python
   - Use tab character : désactivé
   - Tab size : 4
   - Indent size : 4

## 2. Structure Générale d'un Projet Python

Voici un exemple de structure typique d'un projet Python :

```bash
my_project/
│
├── my_project/               # Dossier principal contenant les modules et packages
│   ├── __init__.py           # Indique que ce dossier est un package Python
│   ├── package1/             # Package1
│   │   ├── __init__.py       # Indique que le dossier package1 est un package Python
│   │   ├── module1.py        # Module 1 du package 1
│   │   └── module2.py        # Module 2 du package 1
│   └── module3.py            # Module 3
│
├── tests/                    # Dossier contenant les tests unitaires
│   ├── __init__.py           # Indique que tests est un package Python
│   ├── test_package1/        # Dossier dédié aux tests du package1
│   │   ├── __init__.py       # Indique que test_package1 est un package Python
│   │   ├── test_module1.py   # Tests pour module1 dans package1
│   │   └── test_module2.py   # Tests pour module2 dans package1
│   └── test_module3.py       # Tests pour module3
│
├── scripts/                  # Fichiers exécutables (standalone)
│   ├── script1.py            # Premier script standalone
│   └── script2.py            # Deuxième script standalone
│
├── notebooks/                # Notebooks Jupyter
│   └── analysis.ipynb        # Fichier Notebook Jupyter pour l'analyse exploratoire
│
├── data/                     # (Optionnel) Données pour intégration ou analyse scientifique
│   ├── raw/                  # Données brutes
│   └── processed/            # Données transformées
│
├── docs/                     # (Optionnel) Documentation du projet en Markdown
│   ├── index.md              # Documentation principale
│   └── api_reference.md      # Documentation sur l'API
│
├── requirements.txt          # Liste des dépendances du projet
├── .gitignore                # Fichier listant les fichiers à ignorer par Git
├── README.md                 # Documentation principale du projet
└── pyproject.toml            # Fichier de configuration pour Poetry ou autres outils modernes
```

## 3. Types de Fichiers et Utilisations

### a) Fichiers Python autonomes (standalone):

Ce sont des fichiers `.py` qui peuvent être exécutés directement depuis la ligne de commande.
<u>Exemple :</u>
```bash
> python script1.py
```
Ces scripts contiennent souvent une instruction `if __name__ == '__main__':` pour préciser ce qu'il faut exécuter lorsque le fichier est lancé en standalone.

### b) Jupyter Notebooks (`.ipynb`):
Très populaire en science des données, ils permettent de combiner code Python, visualisations et texte dans un même document. Ils sont pratiques pour les projets exploratoires et les analyses :
```bash
> jupyter notebook
```

### c) Modules:
Un module est un fichier `.py` contenant des fonctions, classes ou variables que l'on peut importer dans d'autres fichiers. Cela permet de structurer le code pour qu'il soit réutilisable :
```python
import module1
from module2 import some_function

variable1, (variable2, variable3) = module1.get_data_with_this_fonction()

print(f"Var 2 : {variable2:.3f}, Result={some_function(variable1, yz=variable3)}")
```

### d) Exécution de serveurs
En Python, il est également possible de construire des serveurs avec des frameworks comme `Flask` ou `FastAPI`. Un fichier de serveur typique pourrait ressembler à ceci :
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
```

### e) Namespaces et organisation des modules :
Les modules sont souvent regroupés dans des packages pour une meilleure organisation. Un package est un dossier contenant un fichier `__init__.py`. Ce fichier peut être vide ou contenir du code pour initialiser le package :
```python
# Exemple de package my_project avec deux modules
from my_project import module1
module1.some_function()
```

## 4. Environnements Virtuels

Les environnements virtuels permettent de gérer les dépendances de façon isolée pour chaque projet. Cela évite les conflits entre les versions des bibliothèques utilisés par différents projets.

<u><strong>Création d'un environnement virtuel : </strong></u>

### a) Avec `venv` (intégré dans Python) :

```bash
>python -m venv <env> #<env> représentant le nom de l'environnement
>source <env>/bin/activate # Commande pour activer l'environnement sur Linux/Mac
><env>\Scripts\activate # Commande pour activer l'environnement sur Windows
```

### b) Avec `virtualenv` (un outil externe) :

```bash
>pip install virtualenv
>virtualenv env
>source env/bin/activate
```

### c) Avec `conda` (très utilisé en science des données):

```bash
>conda create --name <my_env> python=3.x #3.x étant la version de python qu'on utilise
>conda activate <my_env>
```

Une fois acitivé, l'environnement virtuel permet d'installer les dépendances localement, en les répertoriant dans un fichier `requirements.txt` :
```bash
>pip install -r requirements.txt
```

### d) Avec `Poetry` (gestionnaire de dépendances et d'environnements)

`Poetry` est un outil moderne pour gérer les dépendances et les environnements virtuels. Il est particulièrement recommandé pour des projets Python professionnels.

- Installation avec `pipx`:
```bash
>pip install pipx
>pipx install poetry
```
- Initialisation d'un projet :
- - Crée un nouveau projet avec une structure standard
```bash
>poetry new <project_name>
```
- - Installe les dépendances dans un environnement virtuel dédié (Nouveau projet ou cloner avec git)
```bash
>poetry install
```
- Activation de l'environnement vituel géré par Poetry :
```bash
>poetry shell
```
`Poetry` gère automatiquement les dépendances dans le fichier `pyproject.toml`. Pour ajouter une nouvelle bibliothèque :
```bash
>poetry add <package_name>
```
Pour produire un fichier compatible avec `pip install -r`:
```bash
>poetry export -f requirements.txt --output requirements.txt
```
Poetry simplifie la gestion des projets Python tout en intégrant la création d'environnements virtuels isolés.

## 5. Installation et Configuration de Poetry

### Installation de Poetry

1. **Via pip (méthode recommandée)** :
```bash
pip install poetry
```

2. **Via pipx (méthode alternative)** :
```bash
# D'abord installer pipx
pip install pipx

# Ensuite installer poetry avec pipx
pipx install poetry
```

### Configuration initiale

1. **Vérifier l'installation** :
```bash
poetry --version
```

2. **Configurer l'environnement virtuel** :
```bash
# Créer les environnements virtuels dans le projet
poetry config virtualenvs.in-project true

# Afficher la configuration actuelle
poetry config --list
```

### Utilisation basique

1. **Initialiser un nouveau projet** :
```bash
poetry new mon-projet
cd mon-projet
```

2. **Structure créée par Poetry** :
```
mon-projet/
├── pyproject.toml
├── README.md
├── mon_projet/
│   └── __init__.py
└── tests/
    └── __init__.py
```

3. **Ajouter des dépendances** :
```bash
# Ajouter une dépendance de production
poetry add requests

# Ajouter une dépendance de développement
poetry add --dev pytest

# Installer toutes les dépendances
poetry install
```

4. **Gérer les versions Python** :
```bash
# Spécifier la version Python dans pyproject.toml
[tool.poetry.dependencies]
python = "^3.8"  # Compatible avec Python 3.8 et supérieur
```

### Bonnes pratiques avec Poetry

1. **Versionnage** :
   - Toujours commiter `pyproject.toml` et `poetry.lock`
   - Ne pas commiter l'environnement virtuel (`.venv/`)

2. **Documentation** :
   - Maintenir les métadonnées du projet dans `pyproject.toml`
   - Documenter les commandes personnalisées dans README.md

3. **Scripts personnalisés** :
```toml
[tool.poetry.scripts]
start = "mon_projet.main:main"
test = "pytest tests/"
```

4. **Export des dépendances** :
```bash
poetry export -f requirements.txt --output requirements.txt
```

## 6. Commentaires et Documentation

La documentation est cruciale pour maintenir un code lisible et maintenable. Python offre plusieurs façons de documenter votre code, en suivant les conventions définies dans [PEP 8](https://peps.python.org/pep-0008/).

### Types de Commentaires

1. **Commentaires simples** :
```python
# Ceci est un commentaire sur une ligne
x = 1  # Commentaire en fin de ligne
```

2. **Docstrings sur une ligne** :
```python
def calculer_moyenne(nombres):
    """Calcule la moyenne d'une liste de nombres"""
    return sum(nombres) / len(nombres)
```

3. **Docstrings détaillés** :
```python
def calculer_statistiques(donnees, poids=None):
    """
    Calcule les statistiques descriptives d'un ensemble de données

    :param donnees: Liste des valeurs à analyser
    :param poids: Liste optionnelle des poids à appliquer
    :return: Dictionnaire contenant moyenne, médiane et écart-type
    """
    resultats = {}
    # ... code ...
    return resultats
```

### Bonnes Pratiques de Documentation

1. **Documentation de Classe** :
```python
class GestionnaireClient:
    """
    Gère les interactions avec les clients

    Cette classe fournit les méthodes nécessaires pour :
    - Créer un nouveau client
    - Modifier les informations client
    - Supprimer un client
    """
    def creer_client(self, nom, email):
        """Crée un nouveau client dans la base de données"""
        pass
```

2. **Documentation de Module** :
```python
"""
Module de gestion des utilisateurs

Ce module contient toutes les fonctionnalités liées à :
- L'authentification
- La gestion des profils
- Les permissions
"""

from typing import List, Optional
```

3. **Documentation de Package** :
Dans `__init__.py` :
```python
"""
Package principal de l'application

Ce package contient tous les modules nécessaires pour :
- La gestion des données
- L'interface utilisateur
- Les utilitaires
"""
```

### Utilisation des Type Hints

Combinez la documentation avec les type hints pour plus de clarté :
```python
from typing import List, Dict, Optional

def traiter_donnees(
    valeurs: List[float],
    parametres: Optional[Dict[str, any]] = None
) -> Dict[str, float]:
    """
    Traite une série de valeurs selon des paramètres spécifiés

    :param valeurs: Liste des valeurs à traiter
    :param parametres: Dictionnaire optionnel de paramètres
    :return: Dictionnaire des résultats
    """
    resultats = {}
    # ... traitement ...
    return resultats
```

### Outils de Documentation

1. **Sphinx** : Générateur de documentation
   ```bash
   pip install sphinx
   sphinx-quickstart
   ```

2. **pydoc** : Outil intégré à Python
   ```bash
   python -m pydoc mon_module
   ```

3. **VS Code** : Configuration recommandée
   ```json
   {
       "python.linting.enabled": true,
       "python.linting.pylintEnabled": true,
       "editor.rulers": [88],  // Pour respecter PEP 8
   }
   ```

## <u>Conclusion</u>

Un projet Python bien structuré repose sur plusieurs piliers fondamentaux :
- Une indentation correcte et consistante
- Une organisation claire des fichiers et modules
- Une gestion propre des dépendances avec Poetry
- Des tests unitaires bien organisés
- Une documentation claire et maintenue

En respectant ces principes et en utilisant les outils modernes comme Poetry, vous serez en mesure de développer et maintenir des projets Python professionnels et évolutifs.