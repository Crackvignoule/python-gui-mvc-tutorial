# Python GUI and MVC Tutorial

This repository contains examples and exercises for creating GUI applications using Python. It also includes a presentation in both [PowerPoint](./presentation/todo.pptx) and [PDF](./presentation/todo.pdf) formats.

<!-- ## Notebooks

1. [Hello World](https://colab.research.google.com/github/Crackvignoule/python-gui-mvc-tutorial/blob/main/test.ipynb) -->

## Table of Contents

- [Getting Started](#getting-started)
- [Examples](#examples)
  - [Tkinter](#tkinter)
  - [PySide6](#pyside6)
  - [MVC](#mvc)
- [Exercises](#interactive-exercises)
- [Useful Links](#useful-links)
- [References](#references)


## Getting Started

1. Clone the repository:
   ```sh
   git clone https://github.com/Crackvignoule/python-gui-mvc-tutorial.git
   cd python-gui-mvc-tutorial
   ```

2. Create a virtual environment:
   ```sh
   python -m venv .venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```sh
     .\.venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source .venv/bin/activate
     ```

4. Install the dependencies:
   ```sh
   pip install pyside6
   ```

## Examples

### Tkinter

- [Hello World](./examples/tkinter/helloworld.py): A simple "Hello World" example using Tkinter.
- [Form](./examples/tkinter/form.py): A simple form example using Tkinter.
- [Form with ttk](./examples/tkinter/ttk_form.py): A simple form example using `ttk`.

### PySide6

- [Hello World](./examples/pyside6/helloworld.py): A simple "Hello World" example using PySide6.
- [Form](./examples/pyside6/form.py): A simple form example using PySide6.

### MVC

- [Simple MVC](./examples/mvc/simple/helloworld.py): A simple MVC example in a single file.
- [Full MVC](./examples/mvc/full/): A more complex MVC example with proper folder structure.

## Exercises

- [Exercise 1](./exercises/1/README.md): Create a simple form with a button that prints the form data.
- [Exercise 2](./exercises/2/README.md): TODO
- [Exercise 3 (Advanced)](./exercises/3/README.md): Calculator


## Useful Links
- [Python GUI Tutorials: Tkinter](https://www.pythonguis.com/tkinter/)
- [Python GUI Tutorials: PySide6](https://www.pythonguis.com/pyside6/)
- [Which Python GUI Library Should You Choose?](https://www.pythonguis.com/faq/which-python-gui-library/)

## References
- [Javascript MVC lecture](https://github.com/PAJEAN/cours_javascript/blob/master/TP/MVC/README.md)