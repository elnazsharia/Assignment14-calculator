from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader


class Calculator (QMainWindow):
    def __init__(self):

        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load("designer.ui")
        self.ui. show()
        self.ui.btn_persent.clicked.connect(self.persent)

    def persent(self):
        self.ui.textEdit.setText("")


if __name__ == "__main__":
    app = QApplication()
    main_window = Calculator()
    app. exec()
