

from PyQt5 import QtCore, QtGui, QtWidgets
import sumeerlogic


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(612, 561)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.filename = QtWidgets.QLineEdit(Form)
        self.filename.setObjectName("filename")
        self.verticalLayout_3.addWidget(self.filename)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.textset)
        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.origtext = QtWidgets.QPlainTextEdit(Form)
        self.origtext.setReadOnly(True)
        self.origtext.setObjectName("origtext")
        self.verticalLayout.addWidget(self.origtext)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.summtext = QtWidgets.QPlainTextEdit(Form)
        self.summtext.setReadOnly(True)
        self.summtext.setObjectName("summtext")
        self.verticalLayout_2.addWidget(self.summtext)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(self.summtext.clear)
        self.pushButton_2.clicked.connect(self.origtext.clear)
        self.pushButton_2.clicked.connect(self.filename.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Enter the filename(.txt formatl)"))
        self.pushButton.setText(_translate("Form", "Generate"))
        self.label_2.setText(_translate("Form", "Original Text"))
        self.label_3.setText(_translate("Form", "Summary text"))
        self.pushButton_2.setText(_translate("Form", "Clear"))

    def textset(self):
        txt = self.filename.text()
        name = txt+'.txt'
        f = open(name, 'r')
        text = f.read()
        f.close()
        short = sumeerlogic.summerfunc(text)
        self.origtext.setPlainText(text)
        self.summtext.setPlainText(short)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
