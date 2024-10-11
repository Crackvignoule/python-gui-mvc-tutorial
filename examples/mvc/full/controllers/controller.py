from PySide6.QtCore import QObject, Signal

class Controller(QObject):
    count_updated = Signal(int)  # Custom signal to update the view

    def __init__(self, model, view):
        super().__init__()
        self.model = model
        self.view = view
        self.view.button.clicked.connect(self.increment_count)
        self.count_updated.connect(self.view.update_label)  # Connect the custom signal to the view's update_label method
        # self.update_view()

    def increment_count(self):
        self.model.increment_count()
        self.count_updated.emit(self.model.count)  # Emit the custom signal with the updated count
        # self.update_view()

    # def update_view(self):
    #     count = self.model.count
    #     self.view.update_label(count)