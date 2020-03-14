from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setWindowTitle("Follow Up Generator")
        Dialog.setObjectName("Dialog")
        Dialog.resize(970, 656)
        Dialog.setSizeGripEnabled(True)


        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(670, 610, 281, 32))
        self.buttonBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(110, 88, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.workText = QtWidgets.QTextEdit(Dialog)
        self.workText.setGeometry(QtCore.QRect(110, 140, 291, 101))
        self.workText.setObjectName("workText")
        self.nameLabel = QtWidgets.QLabel(Dialog)
        self.nameLabel.setGeometry(QtCore.QRect(20, 30, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameLabel.setFont(font)
        self.nameLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.nameLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.nameLabel.setMidLineWidth(0)
        self.nameLabel.setTextFormat(QtCore.Qt.AutoText)
        self.nameLabel.setObjectName("nameLabel")
        self.dateText = QtWidgets.QLabel(Dialog)
        self.dateText.setGeometry(QtCore.QRect(20, 80, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateText.setFont(font)
        self.dateText.setFrameShape(QtWidgets.QFrame.Box)
        self.dateText.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dateText.setMidLineWidth(0)
        self.dateText.setTextFormat(QtCore.Qt.AutoText)
        self.dateText.setObjectName("dateText")
        self.nameText = QtWidgets.QTextEdit(Dialog)
        self.nameText.setGeometry(QtCore.QRect(110, 30, 104, 31))
        self.nameText.setObjectName("nameText")
        self.workLabel = QtWidgets.QLabel(Dialog)
        self.workLabel.setGeometry(QtCore.QRect(20, 140, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.workLabel.setFont(font)
        self.workLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.workLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.workLabel.setMidLineWidth(0)
        self.workLabel.setTextFormat(QtCore.Qt.AutoText)
        self.workLabel.setObjectName("workLabel")
        self.bugLabel = QtWidgets.QLabel(Dialog)
        self.bugLabel.setGeometry(QtCore.QRect(19, 251, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bugLabel.setFont(font)
        self.bugLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.bugLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bugLabel.setMidLineWidth(0)
        self.bugLabel.setTextFormat(QtCore.Qt.AutoText)
        self.bugLabel.setObjectName("bugLabel")
        self.bugCheck = QtWidgets.QCheckBox(Dialog)
        self.bugCheck.setGeometry(QtCore.QRect(330, 84, 81, 31))
        self.bugCheck.setAcceptDrops(False)
        self.bugCheck.setTristate(False)
        self.bugCheck.setObjectName("bugCheck")
        self.bugText = QtWidgets.QTextEdit(Dialog)
        self.bugText.setGeometry(QtCore.QRect(110, 250, 291, 101))
        self.bugText.setObjectName("bugText")
    
        self.finalResult = QtWidgets.QTextEdit(Dialog)
        self.finalResult.setGeometry(QtCore.QRect(110, 480, 751, 111))
        # self.finalResult.setObjectName("finalResult")


        # self.FinalResultLabel = QtWidgets.QLabel(Dialog)
        # self.FinalResultLabel.setGeometry(QtCore.QRect(110, 480, 751, 111))
        # self.FinalResultLabel.setFrameShape(QtWidgets.QFrame.Panel)
        # self.FinalResultLabel.setObjectName("FinalResultLabel")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #self.update()


        #checked actions
        self.bugCheck.clicked.connect(self.getFinalFollowUp)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.nameLabel.setText(_translate("Dialog", "Name"))
        self.dateText.setText(_translate("Dialog", "Date"))
        self.workLabel.setText(_translate("Dialog", "Worked "))
        self.bugLabel.setText(_translate("Dialog", "Bug"))
        self.bugCheck.setText(_translate("Dialog", "Bugs"))
        #self.FinalResultLabel.setText(_translate("Dialog", "Final Followup"))


    def update(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.getFinalFollowUp)

    def getFinalFollowUp(self):

        print(self.bugCheck.isChecked())
        if self.bugCheck.isChecked():
            print("yes")
            self.finalResult.setText(self.nameText.toPlainText() + " worked on this lesson today")
        else:
            self.finalResult.setText("")
        # #self.FinalResultLabel.setText("Testing 132")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.getFinalFollowUp()
    Dialog.show()
    sys.exit(app.exec_())
