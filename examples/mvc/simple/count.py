from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class Model:
    def __init__(self):
        self.count = 0

    def increment_count(self):
        self.count += 1

class View(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Counter App")

        self.layout = QVBoxLayout()

        self.label = QLabel("Count: 0")
        self.layout.addWidget(self.label)

        self.button = QPushButton("Increment")
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def update_label(self, count):
        self.label.setText(f"Count: {count}")

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.button.clicked.connect(self.increment_count)
        self.update_view()

    def increment_count(self):
        self.model.increment_count()
        self.update_view()

    def update_view(self):
        count = self.model.count
        self.view.update_label(count)

if __name__ == "__main__":
    app = QApplication([])

    model = Model()
    view = View()
    controller = Controller(model, view)

    view.show()
    app.exec()