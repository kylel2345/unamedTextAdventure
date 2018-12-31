import sys

from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QHBoxLayout, QPushButton

from GameScene import GameScene

from MenuButtonsLayout import MenuButtonsLayout

import xml.etree.ElementTree as ET


class GameScreen(QWidget):
    def __init__(self, window):
        super().__init__()

        self.settings = self.initSettings()

        self.window = window
        self.layout = QHBoxLayout()

        self.currentScene = GameScene("mainMenu")
        self.sceneStack = []
        self.menuButtons = None

        self.initMenuButtons()

        self.initGameScene()

        # finalize GameScreen Layout and show it
        self.setLayout(self.layout)
        self.show()

    def initMenuButtons(self):
        self.menuButtons = MenuButtonsLayout()
        self.layout.addLayout(self.menuButtons.getLayout(), int(self.getSettingValue("fileMenuButtPercent")))

    def initGameScene(self):
        self.layout.addLayout(self.currentScene.layout, int(self.getSettingValue("gameScenePercent")))

    def getLayout(self):
        return self.layout

    def initSettings(self):
        try:
            return ET.parse("GameScreenSettings").getroot()
        except:
            print("Error reading and parsing GameScreenSettings", file=sys.stderr)
            exit(1)

    def getSettingValue(self, settingName):
        return self.settings.findall("./*/"+settingName)[0].text

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Display everything
        gameScreen = GameScreen(self)

        self.setCentralWidget(gameScreen)
        self.setGeometry(150, 150, 800, 600)
        self.setWindowTitle('Unknown Adventure')
        self.show()


if __name__ == '__main__':
    print("Starting App")
    try:
        app = QApplication(sys.argv)
        ex = Window()
        sys.exit(app.exec_())
    finally:
        print("Exiting App")
