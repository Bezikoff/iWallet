# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)
from PySide6 import QtCharts

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(140, 0, 501, 481))
        self.IncomePage = QWidget()
        self.IncomePage.setObjectName(u"IncomePage")
        self.IP_IncomeTable = QTableWidget(self.IncomePage)
        self.IP_IncomeTable.setObjectName(u"IP_IncomeTable")
        self.IP_IncomeTable.setGeometry(QRect(0, 40, 501, 441))
        self.IP_CommandBox = QComboBox(self.IncomePage)
        self.IP_CommandBox.setObjectName(u"IP_CommandBox")
        self.IP_CommandBox.setGeometry(QRect(340, 10, 69, 22))
        self.IP_DoButton = QPushButton(self.IncomePage)
        self.IP_DoButton.setObjectName(u"IP_DoButton")
        self.IP_DoButton.setGeometry(QRect(420, 10, 75, 24))
        self.IP_DateInput = QTextEdit(self.IncomePage)
        self.IP_DateInput.setObjectName(u"IP_DateInput")
        self.IP_DateInput.setGeometry(QRect(253, 10, 81, 21))
        self.IP_DateInput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.IP_DateInput.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.IP_DateTxt = QLabel(self.IncomePage)
        self.IP_DateTxt.setObjectName(u"IP_DateTxt")
        self.IP_DateTxt.setGeometry(QRect(220, 10, 31, 16))
        self.IP_AmountInput = QTextEdit(self.IncomePage)
        self.IP_AmountInput.setObjectName(u"IP_AmountInput")
        self.IP_AmountInput.setGeometry(QRect(130, 10, 81, 21))
        self.IP_AmountInput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.IP_AmountInput.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.IP_AmountTxt = QLabel(self.IncomePage)
        self.IP_AmountTxt.setObjectName(u"IP_AmountTxt")
        self.IP_AmountTxt.setGeometry(QRect(80, 10, 41, 16))
        self.IP_IDInput = QTextEdit(self.IncomePage)
        self.IP_IDInput.setObjectName(u"IP_IDInput")
        self.IP_IDInput.setGeometry(QRect(30, 10, 41, 21))
        self.IP_IDInput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.IP_IDInput.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.IP_IDTxt = QLabel(self.IncomePage)
        self.IP_IDTxt.setObjectName(u"IP_IDTxt")
        self.IP_IDTxt.setGeometry(QRect(10, 10, 16, 16))
        self.stackedWidget.addWidget(self.IncomePage)
        self.OutcomePage = QWidget()
        self.OutcomePage.setObjectName(u"OutcomePage")
        self.OP_IDTxt = QLabel(self.OutcomePage)
        self.OP_IDTxt.setObjectName(u"OP_IDTxt")
        self.OP_IDTxt.setGeometry(QRect(10, 10, 16, 16))
        self.OP_AmountInput = QTextEdit(self.OutcomePage)
        self.OP_AmountInput.setObjectName(u"OP_AmountInput")
        self.OP_AmountInput.setGeometry(QRect(130, 10, 81, 21))
        self.OP_AmountInput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.OP_AmountInput.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.OP_DateTxt = QLabel(self.OutcomePage)
        self.OP_DateTxt.setObjectName(u"OP_DateTxt")
        self.OP_DateTxt.setGeometry(QRect(220, 10, 31, 16))
        self.OP_IDInput = QTextEdit(self.OutcomePage)
        self.OP_IDInput.setObjectName(u"OP_IDInput")
        self.OP_IDInput.setGeometry(QRect(30, 10, 41, 21))
        self.OP_IDInput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.OP_IDInput.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.OP_DoButton = QPushButton(self.OutcomePage)
        self.OP_DoButton.setObjectName(u"OP_DoButton")
        self.OP_DoButton.setGeometry(QRect(420, 10, 75, 24))
        self.OP_CommandBox = QComboBox(self.OutcomePage)
        self.OP_CommandBox.setObjectName(u"OP_CommandBox")
        self.OP_CommandBox.setGeometry(QRect(340, 10, 69, 22))
        self.OP_OutComeTable = QTableWidget(self.OutcomePage)
        self.OP_OutComeTable.setObjectName(u"OP_OutComeTable")
        self.OP_OutComeTable.setGeometry(QRect(0, 40, 501, 441))
        self.OP_DateInput = QTextEdit(self.OutcomePage)
        self.OP_DateInput.setObjectName(u"OP_DateInput")
        self.OP_DateInput.setGeometry(QRect(253, 10, 81, 21))
        self.OP_DateInput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.OP_DateInput.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.OP_AmountTxt = QLabel(self.OutcomePage)
        self.OP_AmountTxt.setObjectName(u"OP_AmountTxt")
        self.OP_AmountTxt.setGeometry(QRect(80, 10, 41, 16))
        self.stackedWidget.addWidget(self.OutcomePage)
        self.MainPage = QWidget()
        self.MainPage.setObjectName(u"MainPage")
        self.graphicsView = QtCharts.QChartView(self.MainPage)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 0, 501, 451))
        self.stackedWidget.addWidget(self.MainPage)
        self.PassivePage = QWidget()
        self.PassivePage.setObjectName(u"PassivePage")
        self.PP_AmountTxt = QLabel(self.PassivePage)
        self.PP_AmountTxt.setObjectName(u"PP_AmountTxt")
        self.PP_AmountTxt.setGeometry(QRect(240, 0, 51, 41))
        self.PP_AmountTxt.setWordWrap(True)
        self.PP_IDInput = QTextEdit(self.PassivePage)
        self.PP_IDInput.setObjectName(u"PP_IDInput")
        self.PP_IDInput.setGeometry(QRect(190, 10, 41, 21))
        self.PP_IDInput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.PP_IDInput.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.PP_PassiveIncomeTable = QTableWidget(self.PassivePage)
        self.PP_PassiveIncomeTable.setObjectName(u"PP_PassiveIncomeTable")
        self.PP_PassiveIncomeTable.setGeometry(QRect(0, 70, 501, 411))
        self.PP_CommandBox = QComboBox(self.PassivePage)
        self.PP_CommandBox.setObjectName(u"PP_CommandBox")
        self.PP_CommandBox.setGeometry(QRect(340, 40, 69, 22))
        self.PP_DoButton = QPushButton(self.PassivePage)
        self.PP_DoButton.setObjectName(u"PP_DoButton")
        self.PP_DoButton.setGeometry(QRect(420, 40, 75, 24))
        self.PP_IDTxt = QLabel(self.PassivePage)
        self.PP_IDTxt.setObjectName(u"PP_IDTxt")
        self.PP_IDTxt.setGeometry(QRect(170, 10, 16, 16))
        self.PP_DateTxt = QLabel(self.PassivePage)
        self.PP_DateTxt.setObjectName(u"PP_DateTxt")
        self.PP_DateTxt.setGeometry(QRect(380, 10, 31, 16))
        self.PP_DateInput = QTextEdit(self.PassivePage)
        self.PP_DateInput.setObjectName(u"PP_DateInput")
        self.PP_DateInput.setGeometry(QRect(413, 10, 81, 21))
        self.PP_DateInput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.PP_DateInput.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.PP_AmountInput = QTextEdit(self.PassivePage)
        self.PP_AmountInput.setObjectName(u"PP_AmountInput")
        self.PP_AmountInput.setGeometry(QRect(290, 10, 81, 21))
        self.PP_AmountInput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.PP_AmountInput.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.PP_DateInput_2 = QTextEdit(self.PassivePage)
        self.PP_DateInput_2.setObjectName(u"PP_DateInput_2")
        self.PP_DateInput_2.setGeometry(QRect(240, 40, 81, 21))
        self.PP_DateInput_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.PP_DateInput_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.PP_DateTxt_2 = QLabel(self.PassivePage)
        self.PP_DateTxt_2.setObjectName(u"PP_DateTxt_2")
        self.PP_DateTxt_2.setGeometry(QRect(180, 40, 61, 16))
        self.stackedWidget.addWidget(self.PassivePage)
        self.IP_OpenButton = QPushButton(self.centralwidget)
        self.IP_OpenButton.setObjectName(u"IP_OpenButton")
        self.IP_OpenButton.setGeometry(QRect(10, 10, 111, 24))
        self.OP_OpenButton = QPushButton(self.centralwidget)
        self.OP_OpenButton.setObjectName(u"OP_OpenButton")
        self.OP_OpenButton.setGeometry(QRect(10, 40, 111, 24))
        self.PP_OpenButton = QPushButton(self.centralwidget)
        self.PP_OpenButton.setObjectName(u"PP_OpenButton")
        self.PP_OpenButton.setGeometry(QRect(10, 70, 111, 24))
        self.MP_OpenButton = QPushButton(self.centralwidget)
        self.MP_OpenButton.setObjectName(u"MP_OpenButton")
        self.MP_OpenButton.setGeometry(QRect(10, 100, 111, 24))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 130, 49, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.IP_DoButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.IP_DateTxt.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        self.IP_AmountTxt.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.IP_IDTxt.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.OP_IDTxt.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.OP_DateTxt.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        self.OP_DoButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.OP_AmountTxt.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.PP_AmountTxt.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 \u043f\u043e\u043a\u0443\u043f\u043a\u0438", None))
        self.PP_DoButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.PP_IDTxt.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.PP_DateTxt.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        self.PP_DateTxt_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0432\u043a\u0430, %", None))
        self.IP_OpenButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434\u044b", None))
        self.OP_OpenButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u044b", None))
        self.PP_OpenButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0441\u0441\u0438\u0432\u043d\u044b\u0439 \u0434\u043e\u0445\u043e\u0434", None))
        self.MP_OpenButton.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

