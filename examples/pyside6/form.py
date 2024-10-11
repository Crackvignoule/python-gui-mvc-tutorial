from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

def submit():
    print(f"Name: {name_input.text()}, Age: {age_input.text()}")

app = QApplication([])

window = QWidget()
window.setWindowTitle("Simple Form")

layout = QVBoxLayout()

name_label = QLabel("Name")
age_label = QLabel("Age")

name_input = QLineEdit()
age_input = QLineEdit()

submit_button = QPushButton("Submit")
submit_button.clicked.connect(submit)

layout.addWidget(name_label)
layout.addWidget(name_input)
layout.addWidget(age_label)
layout.addWidget(age_input)
layout.addWidget(submit_button)

window.setLayout(layout)
window.show()

app.exec()