from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowOpacity(0.7)
