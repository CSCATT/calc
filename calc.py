import math
import sys
from PySide2 import QtWidgets
from design.calc_ui import Ui_MainWindow


# link for help: https://habr.com/ru/post/458536/
# ui to py: pyside2-uic "you_file.ui" -o "your_file.py"

class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):
    # Конструктор класса
    def __init__(self):
        super().__init__()

        # Создание формы и Ui (наш дизайн)
        self.setupUi(self)
        # Показать наше окно
        self.show()
        # в поле вывода устанавливаем ноль при запуске
        self.lineEdit.setText('0')

        self.firstMemoryCell = 0.0
        self.secondMemoryCell = 0.0
        self.result = 0.0
        self.example = "None"
        self.equal = "None"

        self.operation_id = "None"
        self.on_operation_click_check = 0

        self.LOG_TAG_CHECKER()

        # pressed
        # on_digit_pressed done
        self.pushButton_1.clicked.connect(self.on_digit_pressed)  # 1
        self.pushButton_2.clicked.connect(self.on_digit_pressed)  # 2
        self.pushButton_3.clicked.connect(self.on_digit_pressed)  # 3
        self.pushButton_4.clicked.connect(self.on_digit_pressed)  # 4
        self.pushButton_5.clicked.connect(self.on_digit_pressed)  # 5
        self.pushButton_6.clicked.connect(self.on_digit_pressed)  # 6
        self.pushButton_7.clicked.connect(self.on_digit_pressed)  # 7
        self.pushButton_8.clicked.connect(self.on_digit_pressed)  # 8
        self.pushButton_9.clicked.connect(self.on_digit_pressed)  # 9
        self.pushButton_zero.clicked.connect(self.on_digit_pressed)  # 0

        # on_operation_pressed
        self.pushButtonSum.clicked.connect(self.on_operation_pressed)  # +
        self.pushButtonMinus.clicked.connect(self.on_operation_pressed)  # -
        self.pushButtonDiv.clicked.connect(self.on_operation_pressed)  # /
        self.pushButtonRise.clicked.connect(self.on_operation_pressed)  # *
        self.pushButton_upper.clicked.connect(self.on_operation_pressed)  # ** ^
        self.pushButton_log.clicked.connect(self.on_operation_pressed)  # log
        self.pushButton_percent.clicked.connect(self.on_operation_pressed)  # %

        self.pushButton_result.clicked.connect(self.function_result)  # =
        self.pushButtonC.clicked.connect(self.function_clear)  # C
        self.pushButton_dot.clicked.connect(self.make_point_fractional)  # .
        self.pushButtonXZ.clicked.connect(self.function_delete)  # <
        # self.pushButton_open_skob.clicked.connect(self.create_big_example) #(

    # lineEdit - белое поле, в котором будут транслироваться все цифры и операции
    # text() - возвращает текст, который написан на нашей кнопке
    # setText() - кладет текст в объект от которого мы вызываем его
    # sender() - функция, которая возвращает отправителя сигнала (какая кнопка была нажата, от какой идет сигнал)
    # button.text() - помещает текст кнопки
    def on_digit_pressed(self):
        button = self.sender()
        if self.lineEdit.text() == '0':
            # Если у нас в нашем поле результата "0", то заменяем его на текст, который написан на кнопке
            self.lineEdit.setText(button.text())
        else:
            if self.result == self.lineEdit.text():
                self.lineEdit.setText(button.text())
            else:
                self.lineEdit.setText(self.lineEdit.text() + button.text())
        self.result = 0

    # clear() - отчищает строку, которую от которой мы его вызываем
    # str(object) - делает из int > str
    # float(object) - делает float num.num
    # int(object) - делает integer
    def on_operation_pressed(self):
        button = self.sender()
        self.operation_id = button.text()
        self.LOG_TAG_CHECKER()

        if self.on_operation_click_check > 0:
            self.secondMemoryCell = float(self.lineEdit.text())
            self.LOG_TAG_CHECKER()
            do_operation = self.operation(self.firstMemoryCell, self.secondMemoryCell)
            self.lineEdit.setText('0')
            print("PRINT_TAG: do_operation = ", do_operation)
        else:
            self.firstMemoryCell = float(self.lineEdit.text())
            self.lineEdit.setText('0')
            self.on_operation_click_check += 1

        print(self.operation_id, type(self.firstMemoryCell), self.firstMemoryCell,
              type(self.secondMemoryCell), self.secondMemoryCell)

    def operation(self, digit_in_memory, new_digit):
        operation_result = None

        if self.operation_id == '+':
            operation_result = self.function_addition(digit_in_memory, new_digit)
        elif self.operation_id == '-':
            operation_result = self.function_subtraction(digit_in_memory, new_digit)
        elif self.operation_id == "/":
            operation_result = self.function_divison(digit_in_memory, new_digit)
        elif self.operation_id == '*':
            operation_result = self.function_multiply(digit_in_memory, new_digit)
        elif self.operation_id == "^":
            operation_result = self.exponentiation(digit_in_memory, new_digit)
        elif self.operation_id == "%":
            operation_result = self.function_percent(digit_in_memory, new_digit)
        elif self.operation_id == "log":
            operation_result = self.function_log(digit_in_memory, new_digit)

        self.result = operation_result
        return operation_result

    def function_result(self):
        if self.equal == '+':
            self.function_addition()
        elif self.equal == '-':
            self.function_subtraction()
        elif self.equal == "/":
            self.function_divison()
        elif self.equal == '*':
            self.function_multiply()
        elif self.equal == "^":
            self.exponentiation()
        elif self.equal == "%":
            self.function_percent()
        elif self.equal == "log":
            self.function_log()

    def function_addition(self, a, b):
        result = float(a + b)
        return result

    def function_subtraction(self, a, b):
        result = float(a - b)
        return result

    def function_divison(self, a, b):
        result = float(a / b)
        return result

    def function_multiply(self, a, b):
        result = float(a * b)
        return result

    def function_exponentiation(self, a, b):
        result = float(a ** b)
        return result

    def function_percent(self, a, b):
        result = float((a * 100) / b)
        return result

    def function_log(self, a, b):
        result = float(math.log(a, b))
        return result

    def form_result(self, a, b):
        self.result = str(self.result)
        if self.result[-2:] == '.0':
            self.result = self.result[:-2]
        self.lineEdit.setText(str(self.result))
        self.label.clear()

    def make_point_fractional(self):
        value = self.lineEdit.text()
        if '.' not in value:
            self.lineEdit.setText(value + '.')

    def function_delete(self):
        value = self.lineEdit.text()
        self.lineEdit.setText(value[:-1])

    def function_clear(self):
        self.lineEdit.setText('0')
        self.GLOBAL_VARIABLES_restart()

    def LOG_TAG_CHECKER(self):
        print("LOG_TAG: ", self.firstMemoryCell, self.secondMemoryCell,
              self.result, self.example, self.equal, self.operation_id,
              self.on_operation_click_check)

    def GLOBAL_VARIABLES_restart(self):
        self.firstMemoryCell = None
        self.secondMemoryCell = None
        self.result = None
        self.example = "None"
        self.equal = "None"

        self.operation_id = "None"
        self.on_operation_click_check = 0


if __name__ == '__main__':
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)
    # Сздание инстанса класса Калькулятор, который мы создадим далее
    calc = Calculator()
    # Запуск
    sys.exit(app.exec_())
