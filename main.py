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
        self.ui.btn_mul.clicked.connect(self.Mul_num)
        self.ui.btn_pow.clicked.connect(self.Power_num)
        self.ui.btn_equal.clicked.connect(self.persent)
        self.ui.btn_jazr.clicked.connect(self.Jazr_num)
        self.ui.btn_delete.clicked.connect(self.Delete_num)
        self.ui.btn_ce.clicked.connect(self.Clear_num)
        self.ui.btn_ce.clicked.connect(self.Clear_num)
        self.ui.btn_dot.clicked.connect(self.Dot_num)
        self.ui.btn_negPos.clicked.connect(self.Negpos_num)

    def Persent_Num(self):
        try:
            pass
        except:
            self.ui.textEdit.setText("Not valid")

    def Sum_num(self):
        try:
            pass
        except:
            self.ui.textEdit.setText("Not valid")

    def Sub_num(self):
        try:
            pass
        except:
            self.ui.textEdit.setText("Not valid")

    def Mul_num(self):
        try:
            pass
        except:
            self.ui.textEdit.setText("Not valid")

    def Power_num(self):
        try:
            pass
        except:
            self.ui.textEdit.setText("Not valid")

    def Jazr_num(self):
        try:
            pass
        except:
            self.ui.textEdit.setText("Not valid")

    def Delete_num(self):
        try:
            pass
        except:
            self.ui.textEdit.setText("Not valid")

    def Clear_num(self):
        try:
            pass
        except:
            self.ui.textEdit.setText("Not valid")

    def Dot_num(self):
        pass

    def Negpos_num(self):
        pass


if __name__ == "__main__":
    app = QApplication()
    main_window = Calculator()
    app. exec()
