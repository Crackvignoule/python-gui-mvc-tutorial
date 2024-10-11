from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

def submit():
    name = name_input.text()
    age = age_input.text()
    email = email_input.text()
    
    if not name or not age or not email:
        QMessageBox.critical(window, "Validation Error", "Name, Age, and Email fields cannot be empty")
    else:
        print(f"Name: {name}, Age: {age}, Email: {email}")

app = QApplication([])

window = QWidget()
window.setWindowTitle("Simple Form")

layout = QVBoxLayout()

name_label = QLabel("Name")
age_label = QLabel("Age")
email_label = QLabel("Email")

name_input = QLineEdit()
age_input = QLineEdit()
email_input = QLineEdit()

submit_button = QPushButton("Submit")
submit_button.clicked.connect(submit)

layout.addWidget(name_label)
layout.addWidget(name_input)
layout.addWidget(age_label)
layout.addWidget(age_input)
layout.addWidget(email_label)
layout.addWidget(email_input)
layout.addWidget(submit_button)

window.setLayout(layout)
window.show()

app.exec()