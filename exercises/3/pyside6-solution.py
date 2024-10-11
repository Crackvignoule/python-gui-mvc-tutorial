# from PySide6.QtCore import Qt
# from PySide6.QtGui import QFont
# from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QTextEdit, QPushButton

# class Calculator(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Calculator")
        
#         self.layout = QVBoxLayout()
#         self.grid = QGridLayout()
        
#         self.entry = QTextEdit()
#         self.entry.setAlignment(Qt.AlignRight)
#         self.entry.setFont(QFont("Arial", 20))
#         self.entry.setFixedHeight(50)
        
#         self.layout.addWidget(self.entry)
#         self.layout.addLayout(self.grid)
        
#         self.setLayout(self.layout)
        
#         buttons = [
#             '7', '8', '9', '/',
#             '4', '5', '6', '*',
#             '1', '2', '3', '-',
#             'C', '0', '=', '+'
#         ]
        
#         row_val = 1
#         col_val = 0
        
#         for button in buttons:
#             btn = QPushButton(button)
#             btn.setFont(QFont("Arial", 20))
#             btn.clicked.connect(self.on_click)
#             self.grid.addWidget(btn, row_val, col_val)
#             col_val += 1
#             if col_val > 3:
#                 col_val = 0
#                 row_val += 1
    
#     def on_click(self):
#         button = self.sender()
#         text = button.text()
#         if text == "=":
#             try:
#                 result = eval(self.entry.toPlainText())
#                 self.entry.setText(str(result))
#             except:
#                 self.entry.setText("Error")
#         elif text == "C":
#             self.entry.setText("")
#         else:
#             self.entry.setText(self.entry.toPlainText() + text)
    
#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
#             self.on_click_equals()
#         elif event.key() == Qt.Key_Escape:
#             self.entry.setText("")
#         else:
#             super().keyPressEvent(event)
    
#     def on_click_equals(self):
#         try:
#             result = eval(self.entry.toPlainText())
#             self.entry.setText(str(result))
#         except:
#             self.entry.setText("Error")

# app = QApplication([])

# window = Calculator()
# window.show()

# app.exec()