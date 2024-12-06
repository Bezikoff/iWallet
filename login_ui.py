# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(400, 140)
        LoginWindow.setMinimumSize(QSize(400, 140))
        LoginWindow.setMaximumSize(QSize(400, 140))
        icon = QIcon(QIcon.fromTheme(u"accessories-calculator"))
        LoginWindow.setWindowIcon(icon)
        self.pushButton = QPushButton(LoginWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 100, 75, 24))
        self.LoginSpace = QTextEdit(LoginWindow)
        self.LoginSpace.setObjectName(u"LoginSpace")
        self.LoginSpace.setGeometry(QRect(120, 30, 231, 21))
        self.LoginSpace.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.LoginSpace.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label = QLabel(LoginWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 30, 49, 16))
        self.label_2 = QLabel(LoginWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 60, 49, 16))
        self.readyButton = QPushButton(LoginWindow)
        self.readyButton.setObjectName(u"readyButton")
        self.readyButton.setGeometry(QRect(120, 100, 75, 24))
        self.createButton = QPushButton(LoginWindow)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setEnabled(True)
        self.createButton.setGeometry(QRect(220, 100, 75, 24))
        self.returnButton = QPushButton(LoginWindow)
        self.returnButton.setObjectName(u"returnButton")
        self.returnButton.setGeometry(QRect(220, 100, 75, 24))
        self.label_3 = QLabel(LoginWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 10, 281, 16))
        self.PasswordSpace = QLineEdit(LoginWindow)
        self.PasswordSpace.setObjectName(u"PasswordSpace")
        self.PasswordSpace.setGeometry(QRect(120, 60, 231, 22))
        self.PasswordSpace.setEchoMode(QLineEdit.Password)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"iWallet - \u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("LoginWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.readyButton.setText(QCoreApplication.translate("LoginWindow", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
        self.createButton.setText(QCoreApplication.translate("LoginWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.returnButton.setText(QCoreApplication.translate("LoginWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.label_3.setText(QCoreApplication.translate("LoginWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u0441 \u0434\u0430\u043d\u043d\u044b\u043c \u043b\u043e\u0433\u0438\u043d\u043e\u043c \u0443\u0436\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442!", None))
    # retranslateUi

