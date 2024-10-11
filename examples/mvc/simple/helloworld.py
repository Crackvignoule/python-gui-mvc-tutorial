from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class Model:
    def __init__(self):
        self.data = "Hello MVC"

class View(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello MVC App")

        self.layout = QVBoxLayout()
        self.label = QLabel("")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def display(self, data):
        self.label.setText(data)

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.update_view()

    def update_view(self):
        data = self.model.data
        self.view.display(data)

if __name__ == "__main__":
    app = QApplication([])

    model = Model()
    view = View()
    controller = Controller(model, view)

    view.show()
    app.exec()