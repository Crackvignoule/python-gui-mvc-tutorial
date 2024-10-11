from PySide6.QtWidgets import QApplication
from models.model import Model
from views.view import View
from controllers.controller import Controller

if __name__ == "__main__":
    app = QApplication([])

    model = Model()
    view = View()
    controller = Controller(model, view)

    view.show()
    app.exec()