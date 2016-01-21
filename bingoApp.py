from PyQt4 import QtCore, QtGui
import sys
import random

class Form(QtGui.QFrame):

    def clickedButton(self):
        print("clicked")
        while True:
            newNumber = random.randint(1,100)
            if newNumber not in self.bingoNumbers:
                self.bingoNumbers.add(newNumber)
                self.LCD.setDigitCount(QtCore.QString("%1").arg(newNumber).length())
                self.LCD.display(newNumber)

                break
            else:
                print("error")

    def resetButton(self):
        self.bingoNumbers = set()
        self.LCD.setDigitCount(QtCore.QString("%1").arg(0).length())
        self.LCD.display(0)

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.bingoNumbers = set()
        self.bingoNumbers.add(0)
        self.LCD = QtGui.QLCDNumber()
        self.LCD.setDigitCount(QtCore.QString("%1").arg(0).length())
        self.layout = QtGui.QVBoxLayout()

        self.nextBtn = QtGui.QPushButton("Next number")
        self.nextBtn.setMaximumWidth(150)
        self.resetBtn = QtGui.QPushButton("reset")
        self.resetBtn.setMaximumWidth(150)
        self.btnLayout = QtGui.QHBoxLayout()
        self.btnLayout.setSpacing(10)
        self.btnLayout.addWidget(self.nextBtn)
        self.btnLayout.addWidget(self.resetBtn)
        self.btnFrame = QtGui.QFrame()
        self.btnFrame.setMaximumHeight(100)
        self.btnFrame.setLayout(self.btnLayout)

        self.layout.addWidget(self.LCD)
        self.layout.addWidget(self.btnFrame)
        self.setLayout(self.layout)
        self.showFullScreen()

        self.resetBtn.clicked.connect(self.resetButton)
        self.nextBtn.clicked.connect(self.clickedButton)

    def keyPressEvent(self, e):

        if e.key() == QtCore.Qt.Key_Escape:
            self.close()




app = QtGui.QApplication(sys.argv)
form = Form()
form.show()
app.exec_()