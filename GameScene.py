from PyQt5.QtWidgets import QVBoxLayout, QPlainTextEdit, QHBoxLayout

from CustomButton import CustomButton


class GameScene:
    def __init__(self, id):
        self.layout = QVBoxLayout()
        self.sceneText = QPlainTextEdit()
        self.optionsLayout = QHBoxLayout()
        self.optionButtons = None

        self.initSceneTextOptions()
        self.initOptionsButtons()
        self.combineLayouts()

    def initOptionsButtons(self):
        # TODO: acutally retrieve the options and configure them.
        self.optionButtons = CustomButton('option1', self.chooseOption, tooltip="this is where an explanation goes")
        self.optionsLayout.addWidget(self.optionButtons)

    def initSceneTextOptions(self):
        self.sceneText.setReadOnly(True)
        self.sceneText.insertPlainText("This is where the current scene info goes \n we can have multiple \n lines too")

    def combineLayouts(self):
        self.layout.addWidget(self.sceneText)
        self.layout.addLayout(self.optionsLayout)

    def chooseOption(self):
        # TODO: actually make this select the correct option.
        print("option 1 was clicked")