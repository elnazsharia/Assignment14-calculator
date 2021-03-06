from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from math import *
from sympy import *


class Calculator (QMainWindow):
    def __init__(self):

        super().__init__()
        self.res = 0
        loader = QUiLoader()
        self.ui = loader.load("designer.ui")
        self.ui. show()
        self.ui.btn_persent.clicked.connect(self.Persent_Num)
        self.ui.btn_sum.clicked.connect(self.Sum_num)
        self.ui.btn_equal.clicked.connect(self.Equal_num)
        self.ui.btn_div.clicked.connect(self.Div_num)
        self.ui.btn_sub.clicked.connect(self.Sub_num)
        self.ui.btn_mul.clicked.connect(self.Mul_num)
        self.ui.btn_pow.clicked.connect(self.Power_num)
        self.ui.btn_jzr.clicked.connect(self.Jazr_num)
        self.ui.btn_delete.clicked.connect(self.Delete_num)
        self.ui.btn_cel.clicked.connect(self.Clear_num)
        """ self.ui.btn_negPos.clicked.connect(self.Negpos_num) """
        self.ui.btn_sin.clicked.connect(self.Sin_num)
        self.ui.btn_cos.clicked.connect(self.Cos_num)
        self.ui.btn_cot.clicked.connect(self.Cot_num)
        self.ui.btn_tan.clicked.connect(self.Tan_num)
        self.ui.btn_log.clicked.connect(self.Log_num)

    def Persent_Num(self):
        self.cal = 8
        self.first = float(self.ui.text_box.text())
        self.ui.text_box.setText("")

    def Sum_num(self):
        try:
            self.cal = 1
            self.first = float(self.ui.text_box.text())
            self.ui.text_box.setText("")
        except:
            self.ui.text_box.setText("Not valid")

    def Sub_num(self):
        try:
            self.cal = 2
            self.first = float(self.ui.text_box.text())
            self.ui.text_box.setText("")
        except:
            self.ui.text_box.setText("Not valid")

    def Mul_num(self):
        try:
            self.cal = 3
            self.first = float(self.ui.text_box.text())
            self.ui.text_box.setText("")
        except:
            self.ui.text_box.setText("Not valid")

    def Div_num(self):
        try:
            self.cal = 4
            self.first = float(self.ui.text_box.text())
            self.ui.text_box.setText("")
        except:
            self.ui.text_box.setText("Not valid")

    def Power_num(self):
        try:
            self.cal = 5
            self.first = float(self.ui.text_box.text())
            self.ui.text_box.setText("")
        except:
            self.ui.text_box.setText("Not valid")

    def Jazr_num(self):
        try:
            self.cal = 6
            self.first = int(self.ui.text_box.text())
            self.ui.text_box.setText("The root of " + str(self.first))
        except:
            self.ui.text_box.setText("")

    def Delete_num(self):
        self.ui.text_box.setText("")

    def Clear_num(self):
        try:
            self.first = self.ui.text_box.setText("")
        except:
            self.ui.text_box.setText("Not valid")

    def Negpos_num(self):
        try:
            self.first = self.ui.text_box.setText("")
        except:
            self.ui.text_box.setText("Not valid")

    def Sin_num(self):
        try:
            self.cal = 9
            self.first = float(self.ui.text_box.text())
        except:
            self.ui.text_box.setText("Not valid")

    def Cos_num(self):
        try:
            self.cal = 10
            self.first = float(self.ui.text_box.text())
        except:
            self.ui.text_box.setText("Not valid")

    def Log_num(self):
        try:
            self.cal = 11
            self.first = float(self.ui.text_box.text())
        except:
            self.ui.text_box.setText("Not valid")

    def Tan_num(self):
        try:
            self.cal = 12
            self.first = float(self.ui.text_box.text())
        except:
            self.ui.text_box.setText("Not valid")

    def Cot_num(self):
        try:
            self.cal = 13
            self.first = float(self.ui.text_box.text())
        except:
            self.ui.text_box.setText("Not valid")

    def Equal_num(self):
        if self.cal == 1:
            self.second = float(self.ui.text_box.text())
            self.ui.text_box.setText("")
            self.first = self.ui.text_box.setText(
                str(self.first + self.second))
        if self.cal == 2:
            self.second = float(self.ui.text_box.text())
            self.ui.text_box.setText("")
            self.first = self.ui.text_box.setText(
                str(self.first - self.second))
        if self.cal == 3:
            self.second = float(self.ui.text_box.text())
            self.ui.text_box.setText("")
            self.first = self.ui.text_box.setText(
                str(self.first * self.second))
        if self.cal == 4:
            self.second = float(self.ui.text_box.text())
            self.ui.text_box.setText("")
            self.first = self.ui.text_box.setText(
                str(self.first / self.second))
        if self.cal == 5:
            self.second = float(self.ui.text_box.text())
            self.ui.text_box.setText("")
            self.first = self.ui.text_box.setText(
                str(self.first ** self.second))
        if self.cal == 6:
            self.first = self.ui.text_box.setText(
                str(sqrt(self.first)))
        if self.cal == 8:
            self.second = float(self.ui.text_box.text())
            self.ui.text_box.setText("")
            self.first = self.ui.text_box.setText(
                str((self.first / self.second)*100))
        if self.cal == 9:
            self.first = self.ui.text_box.setText(
                str(sin(self.first)))
        if self.cal == 10:
            self.first = self.ui.text_box.setText(
                str(cos(self.first)))
        if self.cal == 11:
            self.first = self.ui.text_box.setText(
                str(log(self.first)))
        if self.cal == 12:
            self.first = self.ui.text_box.setText(
                str(tan(self.first)))
        if self.cal == 13:
            self.first = self.ui.text_box.setText(
                str(cot(self.first)))


if __name__ == "__main__":
    app = QApplication()
    main_window = Calculator()
    app. exec()
