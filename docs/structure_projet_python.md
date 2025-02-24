# Structure d'un Projet Python et Bonnes Pratiques

*Python* est un langage de programmation très polyvalent, utilisé dans divers domaines allant du développement web aux sciences de données en passant par l'automatisation. La structure d'un projet Python peut varier en fonction de son objectif, mais il existe des pratiques courantes qui facilitent l'organisation, la réutilisabilité, et la maintenance du code.

## <u>Objectifs</u>

- Comprendre la structure basique d'un projet *Python*
- Maîtriser l'indentation Python et son importance
- Identifier les différents types de fichiers (standalone, Jupyter notebooks, modules, etc.)
- Apprendre à travailler avec les environnements virtuels
- Explorer l'organisation des modules et des namespaces
- Installer et utiliser Poetry efficacement

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

[Le reste du contenu original sur la structure...]

## 5. Installation et Configuration de Poetry

Poetry est un outil moderne de gestion de dépendances qui simplifie considérablement la gestion des projets Python. Voici un guide détaillé pour son installation et son utilisation.

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
def process_average(number):
    """Calcule la moyenne d'une liste de nombres"""
    return sum(number) / len(number)
```

3. **Docstrings détaillés** :
```python
def process_statistic(data, weight=None):
    """
    Calcule les statistiques descriptives d'un ensemble de données

    :param data: Liste des valeurs à analyser
    :param weight: Liste optionnelle des poids à appliquer
    :return: Dictionnaire contenant moyenne, médiane et écart-type
    """
    results = {}
    # ... code ...
    return results
```

### Bonnes Pratiques de Documentation

1. **Documentation de Classe** :
```python
class ClientManager:
    """
    Gère les interactions avec les clients

    Cette classe fournit les méthodes nécessaires pour :
    - Créer un nouveau client
    - Modifier les informations client
    - Supprimer un client
    """
    def create_client(self, nom, email):
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
from typing import Optional

def process_data(
    value: list[float],
    parameter: Optional[dict[str, any]] = None
) -> dict[str, float]:
    """
    Traite une série de valeurs selon des paramètres spécifiés

    :param value: Liste des valeurs à traiter
    :param parameter: Dictionnaire optionnel de paramètres
    :return: Dictionnaire des résultats
    """
    results = {}
    # ... traitement ...
    return results
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