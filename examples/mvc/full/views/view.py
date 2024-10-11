from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

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