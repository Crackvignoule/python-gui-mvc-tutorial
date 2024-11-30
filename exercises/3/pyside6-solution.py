from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QMenuBar, QStatusBar

def submit():
    name = name_input.text()
    age = age_input.text()
    email = email_input.text()
    
    if not name or not age or not email:
        QMessageBox.critical(window, "Validation Error", "Name, Age, and Email fields cannot be empty")
    else:
        print(f"Name: {name}, Age: {age}, Email: {email}")
        status_bar.showMessage("Form submitted successfully")

def quit_app():
    app.quit()

def show_about():
    QMessageBox.information(window, "About", "This is a simple form application")

app = QApplication([])

window = QMainWindow()
window.setWindowTitle("Simple Form")

central_widget = QWidget()
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

central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

# Create menu
menu_bar = QMenuBar()
window.setMenuBar(menu_bar)

file_menu = menu_bar.addMenu("File")
quit_action = QAction("Quit", window)
quit_action.triggered.connect(quit_app)
file_menu.addAction(quit_action)

help_menu = menu_bar.addMenu("Help")
about_action = QAction("About", window)
about_action.triggered.connect(show_about)
help_menu.addAction(about_action)

# Create status bar
status_bar = QStatusBar()
window.setStatusBar(status_bar)
status_bar.showMessage("Ready")

window.show()
app.exec()