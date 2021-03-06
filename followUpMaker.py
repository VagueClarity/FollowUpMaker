from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from message import Message

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setWindowTitle("Follow Up Generator")
        Dialog.setObjectName("Dialog")
        Dialog.resize(970, 656)
        Dialog.setSizeGripEnabled(True)
        
        # Okay and Cancel button
        
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.nameText = QtWidgets.QTextEdit(Dialog)
        self.pronounLabel = QtWidgets.QLabel(Dialog)
        self.nameLabel = QtWidgets.QLabel(Dialog)
        self.dateText = QtWidgets.QLabel(Dialog)
        self.workLabel = QtWidgets.QLabel(Dialog)
        self.bugLabel = QtWidgets.QLabel(Dialog)
        self.finalResult = QtWidgets.QTextEdit(Dialog)
        self.codeLangLabel = QtWidgets.QLabel(Dialog)
     
        
        
        
        # Student attributes
        self.focusedLabel = QtWidgets.QLabel(Dialog)
        self.distractedLabel = QtWidgets.QLabel(Dialog)
        self.independentLabel = QtWidgets.QLabel(Dialog)
        self.helpfulLabel = QtWidgets.QLabel(Dialog)
        self.focusedCheck = QtWidgets.QCheckBox(Dialog)
        self.distractedCheck = QtWidgets.QCheckBox(Dialog)
        self.independentCheck = QtWidgets.QCheckBox(Dialog)
        self.helpfulCheck = QtWidgets.QCheckBox(Dialog)
        
        self.okButton.setGeometry(QtCore.QRect(780, 610, 80, 20))
        self.okButton.setObjectName("okButton")
        self.okButton.setText("Ok")
        
      
        
        # Checkbox
        self.focusedCheck.setGeometry(QtCore.QRect(20, 55, 104, 20))
        self.distractedCheck.setGeometry(QtCore.QRect(110, 55, 104, 20))
        self.independentCheck.setGeometry(QtCore.QRect(200, 55, 104, 20))
        self.helpfulCheck.setGeometry(QtCore.QRect(300, 55, 104, 20))
        
        self.focusedLabel.setGeometry(QtCore.QRect(40, 55, 71, 20))
        self.focusedLabel.setObjectName("focusedLabel")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.focusedLabel.setFont(font)
        
       
        self.distractedLabel.setGeometry(QtCore.QRect(130, 55, 71, 20))
        self.distractedLabel.setObjectName("distractedLabel")
        self.distractedLabel.setFont(font)
        
        self.independentLabel.setGeometry(QtCore.QRect(220, 55, 71, 20))
        self.independentLabel.setObjectName("independentLabel")
        self.independentLabel.setFont(font)
        
        self.helpfulLabel.setGeometry(QtCore.QRect(320, 55, 71, 20))
        self.helpfulLabel.setObjectName("independentLabel")
        self.helpfulLabel.setFont(font)
        
        
        
        
        # Time edit
        self.dateTimeEdit.setGeometry(QtCore.QRect(110, 90, 194, 20))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
       
        # Text Fields
        self.nameText.setGeometry(QtCore.QRect(110, 30, 104, 20))
        self.nameText.setObjectName("nameText")
        self.nameText.setTabChangesFocus(True)
        self.workText = QtWidgets.QTextEdit(Dialog)
        self.workText.setGeometry(QtCore.QRect(110, 140, 291, 101))
        self.workText.setObjectName("workText")
        self.workText.setTabChangesFocus(True)
        self.bugText = QtWidgets.QTextEdit(Dialog)
        self.bugText.setGeometry(QtCore.QRect(110, 250, 291, 101))
        self.bugText.setObjectName("bugText")
        self.bugText.setTabChangesFocus(True)
        

        # Gender Choice
        self.pronounLabel.setGeometry(QtCore.QRect(230, 30, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pronounLabel.setFont(font)
        self.pronounLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.pronounLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pronounLabel.setMidLineWidth(0)
        self.pronounLabel.setTextFormat(QtCore.Qt.AutoText)
        self.pronoun = QtWidgets.QComboBox(Dialog)
        self.pronoun.setGeometry(QtCore.QRect(320, 30, 80, 20))
        self.pronoun.clear()
        self.pronoun.addItems(['He', 'She', 'They'])
      
        # Pronoun Choice
        self.codeLangLabel.setGeometry(QtCore.QRect(415, 30, 71, 20))
        self.codeLangLabel.setFont(font)
        self.codeLangLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.codeLangLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.codeLangLabel.setMidLineWidth(0)
        self.codeLangLabel.setTextFormat(QtCore.Qt.AutoText)
        self.codeLang = QtWidgets.QComboBox(Dialog)
        self.codeLang.setGeometry(QtCore.QRect(500, 30, 80, 20))
        self.codeLang.clear()
        self.codeLang.addItems(['Javascript', 'Scratch', 'Unity'])
      
        # Labels
        self.nameLabel.setGeometry(QtCore.QRect(20, 30, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameLabel.setFont(font)
        self.nameLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.nameLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.nameLabel.setMidLineWidth(0)
        self.nameLabel.setTextFormat(QtCore.Qt.AutoText)
        self.nameLabel.setObjectName("nameLabel")
       
        self.dateText.setGeometry(QtCore.QRect(20, 90, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateText.setFont(font)
        self.dateText.setFrameShape(QtWidgets.QFrame.Box)
        self.dateText.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dateText.setMidLineWidth(0)
        self.dateText.setTextFormat(QtCore.Qt.AutoText)
        self.dateText.setObjectName("dateText")
        
        
       
    
        self.workLabel.setGeometry(QtCore.QRect(20, 140, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.workLabel.setFont(font)
        self.workLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.workLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.workLabel.setMidLineWidth(0)
        self.workLabel.setTextFormat(QtCore.Qt.AutoText)
        self.workLabel.setObjectName("workLabel")
        
        self.bugLabel.setGeometry(QtCore.QRect(19, 251, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bugLabel.setFont(font)
        self.bugLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.bugLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bugLabel.setMidLineWidth(0)
        self.bugLabel.setTextFormat(QtCore.Qt.AutoText)
        self.bugLabel.setObjectName("bugLabel")
        # self.bugCheck = QtWidgets.QCheckBox(Dialog)
        # self.bugCheck.setGeometry(QtCore.QRect(330, 84, 81, 20))
        # self.bugCheck.setAcceptDrops(False)
        # self.bugCheck.setTristate(False)
        # self.bugCheck.setObjectName("bugCheck")
        
    
        
        self.finalResult.setGeometry(QtCore.QRect(110, 480, 751, 111))
        # self.finalResult.setObjectName("finalResult")


        # self.FinalResultLabel = QtWidgets.QLabel(Dialog)
        # self.FinalResultLabel.setGeometry(QtCore.QRect(110, 480, 751, 111))
        # self.FinalResultLabel.setFrameShape(QtWidgets.QFrame.Panel)
        # self.FinalResultLabel.setObjectName("FinalResultLabel")

        self.retranslateUi(Dialog)
        # self.buttonBox.accepted.connect(self.getFinalFollowUp)
        # self.buttonBox.rejected.connect(Dialog.reject)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)



        #checked actions
        self.okButton.clicked.connect(self.getFinalFollowUp)
        #self.focusedCheck.clicked.connect(self.getFinalFollowUp)
       

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.nameLabel.setText(_translate("Dialog", "Name"))
        self.dateText.setText(_translate("Dialog", "Date"))
        self.workLabel.setText(_translate("Dialog", "Worked "))
        self.bugLabel.setText(_translate("Dialog", "Bug"))
        #self.bugCheck.setText(_translate("Dialog", "Bugs"))
        self.pronounLabel.setText(_translate("Dialog", "Pronoun"))
        self.focusedLabel.setText(_translate("Dialog", "Focused"))
        self.distractedLabel.setText(_translate("Dialog", "Distracted"))
        self.independentLabel.setText(_translate("Dialog", "Independent"))
        self.helpfulLabel.setText(_translate("Dialog", "Helfpul"))
        self.codeLangLabel.setText(_translate("Dialog","Language"))
        #self.FinalResultLabel.setText(_translate("Dialog", "Final Followup"))


    def update(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.getFinalFollowUp)




    def getFinalFollowUp(self):
    
        name = self.nameText.toPlainText()
        pronoun = self.pronoun.currentText()
        codeLang = self.codeLang.currentText()
        
        stuff = self.workText.toPlainText()
        s = Student(name, pronoun, codeLang)
        m = Message(s, stuff)
        
       
        if self.focusedCheck.isChecked():
            self.finalResult.setText(m.getIntroMessage() + m.isFocusedMessage() +  m.getOutroMessage())
        else:
            self.finalResult.setText(m.getIntroMessage() +  m.getOutroMessage())
    
class Student():
    
    def __init__(self, name, pronoun, codeLang):
        self.name = name
        if pronoun == 'he' or pronoun == 'He':
            self.pronoun =  [pronoun, 'his']
        elif pronoun == 'she' or pronoun == 'She':
            self.pronoun = [pronoun, 'her']
        elif pronoun == 'they' or pronoun == 'They':
            self.pronoun = [pronoun, 'their']
        self.codeLang = codeLang
        self.description()
        
        
    def description(self):
    
        self.distracted = False
        self.helpful = False
        self.independent = False
        self.focused = False
        
    
    def getName(self):
        return self.name
    
    def getPronoun(self):
        return self.pronoun
    
    def isFocused(self):
        return self.focused
    
    def getLanguage(self):
        return self.codeLang
    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    #ui.getFinalFollowUp()
    Dialog.show()
    sys.exit(app.exec_())
