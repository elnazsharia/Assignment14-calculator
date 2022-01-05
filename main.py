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
        self.ui.btn_persent.clicked.connect(self.Persent_Num)
        self.ui.btn_sum.clicked.connect(self.Sum_num)
        self.ui.btn_sub.clicked.connect(self.Sub_num)
        self.ui.btn_mul.clicked.connect(self.persent)
        self.ui.btn_pow.clicked.connect(self.persent)
        self.ui.btn_equal.clicked.connect(self.persent)
        self.ui.btn_jazr.clicked.connect(self.persent)
        self.ui.btn_delete.clicked.connect(self.persent)

    def Persent_Num(self):
        self.ui.textEdit.setText("")

    def Sum_num(self):
        pass

    def Sub_num(self):
        pass

    def Mul_num(self):
        pass

    def Power_num(self):
        pass

    def Jazr_num(self):
        pass

    def Delete_num(self):
        pass

    def Celere_num(self):
        pass


if __name__ == "__main__":
    app = QApplication()
    main_window = Calculator()
    app. exec()
