[README en Français](README.md)

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

1. Open Command Prompt (cmd) on Windows:
   - Press `Win + R` to open the Run dialog.
   - Type `cmd` and press `Enter`.

2. Clone the repository:
   ```sh
   git clone https://github.com/Crackvignoule/python-gui-mvc-tutorial.git
   cd python-gui-mvc-tutorial
   ```

3. Create a virtual environment:
   ```sh
   python -m venv .venv
   ```

4. Activate the virtual environment:

   - On Windows:
     ```sh
     .\.venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source .venv/bin/activate
     ```

5. Install the dependencies:
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

- [Exercise 1](./exercises/1/README.md): Add an Email Field to the Form
- [Exercise 2](./exercises/2/README.md): Implement Form Validation
- [Exercise 3 (Advanced)](./exercises/3/README.md): Calculator


## Useful Links
- [PythonGUIs: Tkinter](https://www.pythonguis.com/tkinter/)
- [PythonGUIs: PySide6](https://www.pythonguis.com/pyside6/)
- [PythonGUIs Examples](https://github.com/pythonguis/pythonguis-examples)
- [Which Python GUI Library Should You Choose?](https://www.pythonguis.com/faq/which-python-gui-library/)
- [superqt - A collection of custom widgets for PySide6](https://pyapp-kit.github.io/superqt/)
- [PySide6 Examples](https://doc.qt.io/qtforpython-6/examples/index.html)

- [PySide6 Documentation](https://doc.qt.io/qtforpython-6/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

## References
- [Javascript MVC lecture](https://github.com/PAJEAN/cours_javascript/blob/master/TP/MVC/README.md)