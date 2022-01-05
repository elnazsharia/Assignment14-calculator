from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader


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
        """self.ui.btn_pow.clicked.connect(self.Power_num)
        self.ui.btn_jazr.clicked.connect(self.Jazr_num)
        self.ui.btn_delete.clicked.connect(self.Delete_num)
        self.ui.btn_ce.clicked.connect(self.Clear_num)
        self.ui.btn_ce.clicked.connect(self.Clear_num)
        self.ui.btn_dot.clicked.connect(self.Dot_num)
        self.ui.btn_negPos.clicked.connect(self.Negpos_num)
        
        self.ui.btn_sin.clicked.connect(self.Equal_num)
        self.ui.btn_cos.clicked.connect(self.Equal_num)
        self.ui.btn_cot.clicked.connect(self.Equal_num)
        self.ui.btn_tan.clicked.connect(self.Equal_num)
        self.ui.btn_sqrt.clicked.connect(self.Equal_num)
        self.ui.btn_log.clicked.connect(self.Equal_num) """

    def Persent_Num(self):
        try:
            pass
        except:
            self.ui.textEdit.setText("Not valid")

    def Sum_num(self):
        try:
            self.cal = 1
            self.first = int(self.ui.text_box.text())
            self.ui.text_box.setText("")
        except:
            self.ui.textEdit.setText("Not valid")

    def Sub_num(self):
        try:
            self.cal = 2
            self.first = int(self.ui.text_box.text())
            self.ui.text_box.setText("")
        except:
            self.ui.textEdit.setText("Not valid")

    def Mul_num(self):
        try:
            self.cal = 3
            self.first = int(self.ui.text_box.text())
            self.ui.text_box.setText("")
        except:
            self.ui.textEdit.setText("Not valid")

    def Div_num(self):
        try:
            self.cal = 4
            self.first = int(self.ui.text_box.text())
            self.ui.text_box.setText("")
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

    def Equal_num(self):
        if self.cal == 1:
            self.second = int(self.ui.text_box.text())
            self.ui.text_box.setText("")
            self.ui.text_box.setText(str(self.first + self.second))
        if self.cal == 2:
            self.second = int(self.ui.text_box.text())
            self.ui.text_box.setText("")
            self.ui.text_box.setText(str(self.first - self.second))
        if self.cal == 3:
            self.second = int(self.ui.text_box.text())
            self.ui.text_box.setText("")
            self.ui.text_box.setText(str(self.first * self.second))
        if self.cal == 4:
            self.second = int(self.ui.text_box.text())
            self.ui.text_box.setText("")
            self.ui.text_box.setText(str(self.first / self.second))


if __name__ == "__main__":
    app = QApplication()
    main_window = Calculator()
    app. exec()
