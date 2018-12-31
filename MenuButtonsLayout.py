from PyQt5.QtWidgets import QWidget, QLayout, QVBoxLayout, QPushButton

from CustomButton import CustomButton


class MenuButtonsLayout:
    class __MenuButtonsLayout:

        def __init__(self):
            super().__init__()

            self.layout = QVBoxLayout()
            self.buttonList = self.initButtonList()
            self.initShownButtons()

        def getLayout(self):
            return self.layout

        def initButtonList(self):
            return ["Save", "Load", "Inventory", "Char Profile", "Menu"]

        def initShownButtons(self):
            for title in self.buttonList:
                button = CustomButton(title, self.printMe)
                self.layout.addWidget(button)

        def printMe(self):
            print("me")

    instance = None

    def __init__(self):
        if not MenuButtonsLayout.instance:
            MenuButtonsLayout.instance = MenuButtonsLayout.__MenuButtonsLayout()

    def getLayout(self):
        return MenuButtonsLayout.instance.layout
