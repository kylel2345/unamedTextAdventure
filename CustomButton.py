from PyQt5.QtWidgets import QPushButton


class CustomButton(QPushButton):
    def __init__(self, title, onClick, tooltip="", width = 25, height = 15):
        super().__init__()
        self.setText(title)
        self.setToolTip(tooltip)
        self.clicked.connect(onClick)
