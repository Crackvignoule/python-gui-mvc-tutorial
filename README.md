[README in English](README_EN.md)

# Tutoriel Python GUI et MVC

Ce dépôt contient des exemples et des exercices pour créer des applications GUI en utilisant Python. Il inclut également une présentation en formats [PowerPoint](./presentation/todo.pptx) et [PDF](./presentation/todo.pdf).

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
<!-- TODO Google form at the end -->
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
   pip install pyside6
   ```

## Exemples

### Tkinter

- [Hello World](./examples/tkinter/helloworld.py) : Un exemple simple "Hello World" utilisant Tkinter.
- [Formulaire](./examples/tkinter/form.py) : Un exemple de formulaire simple utilisant Tkinter.
- [Formulaire avec ttk](./examples/tkinter/ttk_form.py) : Un exemple de formulaire simple utilisant `ttk`.

### PySide6

- [Hello World](./examples/pyside6/helloworld.py) : Un exemple simple "Hello World" utilisant PySide6.
- [Formulaire](./examples/pyside6/form.py) : Un exemple de formulaire simple utilisant PySide6.

### MVC

- [Hello World](./examples/mvc/helloworld.py) : Un exemple simple "Hello World" utilisant le modèle MVC.
- [Formulaire](./examples/mvc/form.py) : Un exemple de formulaire simple utilisant le modèle MVC.

## Exercices

- [Exercice 1](./exercises/1/README.md) : Ajouter un champ "email" au formulaire.
- [Exercice 2](./exercises/2/README.md) : Implémenter la validation du formulaire.
- [Exercice 3 (Avancé)](./exercises/3/README.md) : Calculatrice.

## Liens Utiles
- [PythonGUIs: Tkinter](https://www.pythonguis.com/tkinter/)
- [PythonGUIs: PySide6](https://www.pythonguis.com/pyside6/)
- [PythonGUIs Examples](https://github.com/pythonguis/pythonguis-examples)
- [Which Python GUI Library Should You Choose?](https://www.pythonguis.com/faq/which-python-gui-library/)
- [superqt - A collection of custom widgets for PySide6](https://pyapp-kit.github.io/superqt/)
- [PySide6 Examples](https://doc.qt.io/qtforpython-6/examples/index.html)

## Références
- [Javascript MVC lecture](https://github.com/PAJEAN/cours_javascript/blob/master/TP/MVC/README.md)