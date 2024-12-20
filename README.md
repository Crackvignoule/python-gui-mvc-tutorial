[README in English](README_EN.md)

# Tutoriel Python GUI et MVC

Ce dépôt contient des exemples et des exercices pour créer des applications GUI en utilisant Python. Il inclut également une présentation en formats [PowerPoint](https://github.com/Crackvignoule/python-gui-mvc-tutorial/raw/refs/heads/main/presentation/Atelier%20Python%20GUI%20&%20MVC.pptx) et [PDF](./presentation/Atelier%20Python%20GUI%20&%20MVC.pdf). J'ai aussi créé un [formulaire Google](https://forms.gle/85zxmsa3xaf7VwH77) pour recueillir votre avis.

<!-- ## Notebooks

1. [Hello World](https://colab.research.google.com/github/Crackvignoule/python-gui-mvc-tutorial/blob/main/test.ipynb) -->

## Table des Matières

- [Commencer](#commencer)
- [Exemples](#exemples)
  - [Tkinter](#tkinter)
  - [PySide6](#pyside6)
  - [MVC](#mvc)
- [Exercices](#exercices)
- [Liens Utiles](#liens-utiles)
- [Références](#références)

## Commencer

1. Ouvrir l'invite de commande (cmd) sur Windows:
   - Appuyez sur `Win + R` pour ouvrir la boîte de dialogue Exécuter.
   - Tapez `cmd` et appuyez sur `Entrée`.

1. Cloner le dépôt :
   ```sh
   git clone https://github.com/Crackvignoule/python-gui-mvc-tutorial.git
   cd python-gui-mvc-tutorial
   ```

2. Créer un environnement virtuel :
   ```sh
   python -m venv .venv
   ```

3. Activer l'environnement virtuel :
   
      - Sur Windows :
      ```sh
      .\.venv\Scripts\activate
      ```
      - Sur macOS et Linux :
      ```sh
      source .venv/bin/activate
      ```

4. Installer les dépendances :
   ```sh
   pip install -r requirements.txt
   ```

   Parfait, vous êtes prêt à commencer !

## Exemples

### Tkinter

- [Hello World](./examples/tkinter/helloworld.py) : Un exemple simple "Hello World" utilisant Tkinter.
- [Formulaire](./examples/tkinter/form.py) : Un exemple de formulaire simple utilisant Tkinter.
- [Formulaire avec ttk](./examples/tkinter/ttk_form.py) : Un exemple de formulaire simple utilisant `ttk`.

### PySide6

- [Hello World](./examples/pyside6/helloworld.py) : Un exemple simple "Hello World" utilisant PySide6.
- [Formulaire](./examples/pyside6/form.py) : Un exemple de formulaire simple utilisant PySide6.

### MVC

- [Hello World](./examples/mvc/simple/helloworld.py) : Un exemple simple "Hello World" utilisant le modèle MVC dans un seul fichier. Aucune interaction avec l'utilisateur.
- [Compteur](./examples/mvc/simple/count.py) : Un compteur simple utilisant le modèle MVC dans un seul fichier.
- [Compteur](./examples/mvc/full/) : Un compteur simple utilisant le modèle MVC réparti sur plusieurs fichiers.


## Exercices

- [Exercice 1](./exercises/1/README.md) : Ajouter un champ "email" au formulaire.
- [Exercice 2](./exercises/2/README.md) : Implémenter la validation du formulaire.
- [Exercice 3](./exercises/3/README.md) : Ajouter un menu et une barre de statut.

## Lancer QT Designer

Pour lancer Qt Designer, vous pouvez utiliser la commande suivante :

```sh
python -c "import os, site, subprocess; subprocess.run([os.path.join(site.getsitepackages()[1], 'PySide6', 'designer')])"
```

## Liens Utiles
- [PythonGUIs: Tkinter](https://www.pythonguis.com/tkinter/)
- [PythonGUIs: PySide6](https://www.pythonguis.com/pyside6/)
- [PythonGUIs Examples](https://github.com/pythonguis/pythonguis-examples)
- [Which Python GUI Library Should You Choose?](https://www.pythonguis.com/faq/which-python-gui-library/)
- [superqt - A collection of custom widgets for PySide6](https://pyapp-kit.github.io/superqt/)
- [PySide6 Examples](https://doc.qt.io/qtforpython-6/examples/index.html)
- [PySide6 Documentation](https://doc.qt.io/qtforpython-6#documentation)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Formation Studio (Designer Alternative)](https://github.com/ObaraEmmanuel/Formation)

## Références
- [Javascript MVC lecture](https://github.com/PAJEAN/cours_javascript/blob/master/TP/MVC/README.md)