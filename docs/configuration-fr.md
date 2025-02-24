# Guide d'installation et configuration de l'environnement Python pour la formation

Ce guide détaillé vous aidera à configurer votre environnement de développement Python, en prenant en compte les cas particuliers et difficultés couramment rencontrés.

## 1. Installation de Python 3.12

### Sur Windows

1. **Téléchargement de Python 3.12** :
   - Rendez-vous sur [python.org/downloads/windows/](https://python.org/downloads/windows/)
   - **Important** : Bien que Python 3.13 soit disponible, nous utiliserons Python 3.12 pour une meilleure compatibilité avec les bibliothèques
   - Faites défiler jusqu'à Python 3.12 et choisissez :
     - Windows 64 bits : `python-3.12.9-amd64.exe` ou `python-3.12.9-arm64.exe` (si vous avez un PC Intel Core)
     - Windows 32 bits : `python-3.12.9.exe`, voir section "Cas particuliers" en cas de problème.

2. **Installation** :
   - Exécutez le fichier téléchargé
   - **Crucial** : Cochez "Add Python 3.12 to PATH"
   - **Recommandé** : Cochez "Install for all users"
   - Cliquez sur "Install Now"
   - Patientez jusqu'à la fin de l'installation

### Sur Linux

1. **Pour Debian/Ubuntu** :
   ```bash
   sudo apt update
   sudo apt install python3.12 python3.12-venv python3-pip
   ```

2. **Pour Fedora** :
   ```bash
   sudo dnf install python3.12 python3.12-devel python3-pip
   ```

3. **Pour openSUSE** :
   ```bash
   sudo zypper install python312 python312-devel python312-pip
   ```

## 2. Vérification de l'installation

1. Ouvrez un terminal/cmd :
   - Windows : Touche Windows + R, tapez "cmd", Entrée
   - Linux : Ctrl + Alt + T

2. Vérifiez la version :
   ```bash
   python --version
   # ou si nécessaire :
   python3 --version
   ```
   Vous devriez voir : `Python 3.12.x`

3. Vérifiez pip :
   ```bash
   pip --version
   # ou si nécessaire :
   pip3 --version
   ```

4. Si la commande n'est pas reconnue :
   - Vérifiez que vous avez bien coché "Add to PATH"
   - Redémarrez votre terminal
   - Redémarrez votre ordinateur si le problème persiste

## 3. Installation de VS Code

1. **Téléchargement** :
   - Visitez [code.visualstudio.com/Download](https://code.visualstudio.com/Download)
   - Choisissez la version correspondant à votre système

2. **Installation** :
   - Windows :
     - Cochez "Add to PATH"
     - Cochez "Add 'Open with Code'"
     - Suivez l'assistant d'installation
   - Linux Debian/Ubuntu :
     ```bash
     sudo dpkg -i code_*.deb
     sudo apt-get install -f
     ```
   - Linux Fedora :
     ```bash
     sudo rpm -i code_*.rpm
     ```

3. **Configuration essentielle** :
   - Installez les extensions :
     - Python (Microsoft)
     - Jupyter
   - Activez le thème sombre (recommandé) :
     - Ctrl/Cmd + Shift + P
     - "Preferences: Color Theme"
     - Sélectionnez "Dark Modern"

## 4. Installation de Jupyter Notebook

1. Mettez à jour pip :
   ```bash
   python -m pip install --upgrade pip
   ```

2. Installez Jupyter :
   ```bash
   pip install notebook
   ```

3. En cas d'erreur :
   - Vérifiez votre connexion internet
   - Essayez avec les droits administrateur
   - Sur Windows : Lancez cmd en administrateur
   - Sur Linux : Utilisez `sudo`

## 5. Cas particuliers

### Windows 32 bits
Si vous avez Windows 32 bits :
1. Utilisez [Google Colab](https://colab.research.google.com) pour les notebooks
2. Pour les scripts Python, installez VS Code 32 bits
3. Créez vos scripts avec l'extension `.py`

### Problèmes courants
1. **Python non reconnu** :
   - Vérifiez le PATH
   - Réinstallez en cochant "Add to PATH"
   - Redémarrez votre ordinateur

2. **Pip ne fonctionne pas** :
   ```bash
   python -m ensurepip --upgrade
   ```

3. **Erreurs d'installation des packages** :
   - Vérifiez votre connexion internet
   - Utilisez un environnement virtuel :
     ```bash
     python -m venv env
     # Windows
     env\Scripts\activate
     # Linux/Mac
     source env/bin/activate
     ```

## 6. Désinstallation de Python (si nécessaire)

1. **Windows** :
   - Paramètres → Applications
   - Recherchez Python 3.12
   - Désinstallez
   - Supprimez les dossiers :
     - `C:\Users\<User>\AppData\Local\Programs\Python\Python312`
     - `C:\Python312`
   - Nettoyez le PATH

2. **Linux** :
   ```bash
   # Debian/Ubuntu
   sudo apt remove python3.12
   # Fedora
   sudo dnf remove python3.12
   # openSUSE
   sudo zypper remove python312
   ```

## 7. Premier projet : Interface graphique avec Tkinter

1. Créez un fichier `votre_nom_devoir_1.py` :

```python
import tkinter as tk
from tkinter import messagebox

# Votre nom
NAME = "Votre Nom"  # À modifier

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello World")
        self.root.geometry("300x200")
        
        # Message de bienvenue
        self.label = tk.Label(root, text=f"Bienvenue {NAME} !!!", font=('Arial', 12))
        self.label.pack(pady=30)
        
        # Bouton Quitter
        self.quit_button = tk.Button(root, text="Quitter", command=self.confirm_quit)
        self.quit_button.pack()
    
    def confirm_quit(self):
        if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()
```

2. **Pour rendre votre devoir** :
   - Le fichier Python (`.py`)
   - Une capture d'écran de VS Code avec votre code
   - Une capture d'écran de votre application en fonctionnement

Note : Nous utilisons Tkinter car c'est la bibliothèque standard de Python pour les interfaces graphiques, garantissant une compatibilité maximale sur tous les systèmes.