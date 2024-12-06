import sys, sqlite3
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from main_ui import Ui_MainWindow as umw
from login_ui import Ui_LoginWindow as ulw
from PySide6 import QtCharts
import pytest

def showinfo(title, message):
    app = QApplication.instance()

    if not app:
        app = QApplication([])

    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.setIcon(QMessageBox.Icon.Information)
    msg_box.exec()
def passincomecheck():
    for i in ask.zapout(f'SELECT date, buyprice, percent, ID FROM PassIncome WHERE UID = {uid}'):
        if i[0][:5] == datetime.now().strftime('%d/%m'):
            if len(ask.zapout(f'SELECT * FROM Income WHERE date = "{datetime.now().strftime("%d/%m/%Y")}" and passid = {i[3]}')) == 0:
                mani = i[1] * i[2] // 100
                truth = True
                aidi = 0
                while truth:
                    aidi += 1
                    if len(ask.zapout(f"SELECT * FROM PassIncome WHERE ID = {aidi}")) == 0:
                        id = aidi
                        truth = False
                ask.zap(f'INSERT INTO Income VALUES ({id}, {uid}, {i[3]}, {mani}, "{datetime.now().strftime("%d/%m/%Y")}")')
def SomeInfo(now):
    global uid
    month = ['', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    tm = [int(i) for i in now[3::].split('/')]
    if tm[0] == 1:
        pm = [12, tm[1]-1]
    else:
        pm = [tm[0]-1, tm[1]]
    if pm[0]==1:
        xpm=[12, pm[1]-1]
    else:
        xpm=[pm[0]-1, pm[1]]
    tincome = 0
    for i in ask.zapout(f'SELECT amount FROM Income WHERE UID = {uid} AND date LIKE "__/{tm[0]}/{tm[1]}"'):
        tincome+=int(i[0])
    pincome = 0
    for i in ask.zapout(f'SELECT amount FROM Income WHERE UID = {uid} AND date LIKE "__/{pm[0]}/{pm[1]}"'):
        pincome+=int(i[0])
    xpincome = 0
    for i in ask.zapout(f'SELECT amount FROM Income WHERE UID = {uid} AND date LIKE "__/{xpm[0]}/{xpm[1]}"'):
        xpincome+=int(i[0])
    toutcome = 0
    for i in ask.zapout(f'SELECT amount FROM Outcome WHERE UID = {uid} AND date LIKE "__/{tm[0]}/{tm[1]}"'):
        toutcome+=int(i[0])
    for i in ask.zapout(f'SELECT buyprice FROM PassIncome WHERE UID = {uid} AND date LIKE "__/{tm[0]}/{tm[1]}"'):
        toutcome+=int(i[0])
    poutcome = 0
    for i in ask.zapout(f'SELECT amount FROM Outcome WHERE UID = {uid} AND date LIKE "__/{pm[0]}/{pm[1]}"'):
        poutcome+=int(i[0])
    for i in ask.zapout(f'SELECT buyprice FROM PassIncome WHERE UID = {uid} AND date LIKE "__/{pm[0]}/{pm[1]}"'):
        poutcome+=int(i[0])
    xpoutcome = 0
    for i in ask.zapout(f'SELECT amount FROM Outcome WHERE UID = {uid} AND date LIKE "__/{xpm[0]}/{xpm[1]}"'):
        xpoutcome+=int(i[0])
    for i in ask.zapout(f'SELECT buyprice FROM PassIncome WHERE UID = {uid} AND date LIKE "__/{xpm[0]}/{xpm[1]}"'):
        xpoutcome+=int(i[0])
    incomeall = 0
    for i in ask.zapout(f'SELECT amount FROM Income WHERE UID = {uid}'):
        incomeall += int(i[0])
    outcomeall = 0
    for i in ask.zapout(f'SELECT amount FROM Outcome WHERE UID = {uid}'):
        outcomeall+=int(i[0])
    result = [[f'{month[tm[0]]} {tm[1]}', f'{month[pm[0]]} {pm[1]}', f'{month[xpm[0]]} {xpm[1]}'],
              [tincome, pincome, xpincome], [toutcome, poutcome, xpoutcome], [incomeall, outcomeall]]
    return result
def checkdate(inp):
    try:
        a = inp.split('/')
        b = int(''.join(a))
    except:
        return False
    month = {'01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
    try:
        if int(a[0]) <= month[a[1]] and int(a[0]) > 0:
            if int(a[2]) > 1900 and int(a[2]) < 2200:
                return True
            else:
                return False
        else:
            return False
    except:
        return False
def checkint(inp):
    try:
        a = int(inp)
    except:
        return False
    return True
class Ask:
    def __init__(self):
        self.con = sqlite3.connect("Save.db")
        self.cur = self.con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS "Income" ("ID" INTEGER NOT NULL,"UID" INTEGER NOT NULL,"passid" INTEGER,"amount" INTEGER NOT NULL,"date" TEXT NOT NULL,PRIMARY KEY("ID" AUTOINCREMENT));')
        self.con.commit()
        self.cur.execute('CREATE TABLE IF NOT EXISTS "Outcome" ("ID" INTEGER NOT NULL,"UID" INTEGER NOT NULL,"amount" INTEGER NOT NULL,"date" TEXT NOT NULL,PRIMARY KEY("ID" AUTOINCREMENT));')
        self.con.commit()
        self.cur.execute('CREATE TABLE IF NOT EXISTS "PassIncome" ("ID" INTEGER NOT NULL,"UID" INTEGER NOT NULL,"date" TEXT NOT NULL,"buyprice" INTEGER NOT NULL,"percent" INTEGER NOT NULL,PRIMARY KEY("ID" AUTOINCREMENT),FOREIGN KEY("UID") REFERENCES "User"("ID"));')
        self.con.commit()
        self.cur.execute('CREATE TABLE IF NOT EXISTS "User" ("ID" INTEGER NOT NULL,"Login" TEXT NOT NULL UNIQUE,"Password" TEXT NOT NULL,PRIMARY KEY("ID" AUTOINCREMENT));')
        self.con.commit()
    def zap(self, a):
        self.cur.execute(a)
        self.con.commit()
    def zapout(self, a):
        self.cur.execute(a)
        rows = self.cur.fetchall()
        return rows
class iWalletWindow(QMainWindow):
    def __init__(self):
        super(iWalletWindow, self).__init__()
        self.setWindowTitle('iWallet')
        self.ui = umw()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.IncomePage)
        self.ui.IP_OpenButton.clicked.connect(lambda x: self.ui.stackedWidget.setCurrentWidget(self.ui.IncomePage))
        self.ui.IP_DoButton.clicked.connect(lambda x: self.docommand())
        self.ui.OP_DoButton.clicked.connect(lambda x: self.docommand())
        self.ui.PP_DoButton.clicked.connect(lambda x: self.docommand())
        self.ui.OP_OpenButton.clicked.connect(lambda x: self.ui.stackedWidget.setCurrentWidget(self.ui.OutcomePage))
        self.ui.PP_OpenButton.clicked.connect(lambda x: self.ui.stackedWidget.setCurrentWidget(self.ui.PassivePage))
        self.ui.MP_OpenButton.clicked.connect(lambda x: self.ui.stackedWidget.setCurrentWidget(self.ui.MainPage))
        self.ui.LeaveButton.clicked.connect(lambda x:self.logout())
        self.ui.IP_IncomeTable.setColumnCount(3)
        self.ui.OP_OutComeTable.setColumnCount(3)
        self.ui.PP_PassiveIncomeTable.setColumnCount(4)
        self.ui.IP_IncomeTable.setHorizontalHeaderLabels(["ID", "Дата", "Сумма"])
        self.ui.OP_OutComeTable.setHorizontalHeaderLabels(["ID", "Дата", "Сумма"])
        self.ui.PP_PassiveIncomeTable.setHorizontalHeaderLabels(["ID", "Дата", "Сумма", "Ставка"])
        self.ui.IP_CommandBox.addItems(['Добавить/изменить', 'Удалить', 'Поиск'])
        self.ui.OP_CommandBox.addItems(['Добавить/изменить', 'Удалить', 'Поиск'])
        self.ui.PP_CommandBox.addItems(['Добавить/изменить', 'Удалить', 'Поиск'])
        '''self.set0 = QtCharts.QBarSet('Доходы')
        self.set1 = QtCharts.QBarSet('Расходы')
        a = datetime.now()
        a = a.strftime('%d/%m/%Y')
        self.BarSetInfo = QChartsAutoInfo(str(a))
        self.set0.append(self.BarSetInfo[1])
        self.set1.append(self.BarSetInfo[2])
        self.barcharts = QtCharts.QBarSeries()
        self.barcharts.append(self.set0)
        self.barcharts.append(self.set1)
        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.barcharts)
        self.chart.setTitle('Доходы и расходы за последние 3 месяца')
        self.xaxis = QtCharts.QBarCategoryAxis()
        self.xaxis.append(self.BarSetInfo[0])
        self.chart.setAxisX(self.xaxis, self.barcharts)
        self.yaxis = QtCharts.QValueAxis()
        self.chart.setAxisY(self.yaxis, self.barcharts)
        self.yaxis.setRange(0, self.BarSetInfo[3])'''
    def logout(self):
        self.hide()
        logwindow.show()
    def docommand(self):
        global uid
        page = str(self.ui.stackedWidget.currentWidget().objectName())
        if page == 'IncomePage':
            amount = self.ui.IP_AmountInput.toPlainText()
            date = self.ui.IP_DateInput.toPlainText()
            command = self.ui.IP_CommandBox.currentText()
            id = self.ui.IP_IDInput.toPlainText()
            if command == 'Добавить/изменить':
                if id == '' and checkdate(date) and checkint(amount):
                    truth = True
                    aidi = 0
                    while truth:
                        aidi += 1
                        if len(ask.zapout(f"SELECT * FROM Income WHERE ID = {aidi}")) == 0:
                            id = aidi
                            truth = False
                    ask.zap(f'INSERT INTO Income VALUES ({id}, {uid}, NULL, {amount}, "{date}")')
                elif checkint(id):
                    zapros = 'UPDATE Income SET'
                    if date != '' or amount != '':
                        if date != '' and checkdate(date):
                            zapros += f' date = "{date}",'
                        if amount != '' and checkint(amount):
                            zapros += f' amount = "{amount}",'
                        zapros = zapros[:-1]
                        zapros += f'WHERE ID = "{id}"'
                        ask.zap(zapros)
                else:
                    showinfo('Ошибка', 'Неправильный формат данных')
                self.ui.IP_IncomeTable.setRowCount(len(ask.zapout(f"SELECT * FROM Income WHERE uid = {uid}")))
                row = 0
                for i in ask.zapout(f"SELECT * FROM Income WHERE uid = {uid}"):
                    self.ui.IP_IncomeTable.setItem(row, 2, QTableWidgetItem(str(i[3])))
                    self.ui.IP_IncomeTable.setItem(row, 1, QTableWidgetItem(i[4]))
                    self.ui.IP_IncomeTable.setItem(row, 0, QTableWidgetItem(str(i[0])))
                    row += 1
            elif command == 'Удалить':
                if checkint(id):
                    ask.zap(f'DELETE FROM Income WHERE ID = {id}')
                    self.ui.IP_IncomeTable.setRowCount(len(ask.zapout(f"SELECT * FROM Income WHERE uid = {uid}")))
                    row = 0
                    for i in ask.zapout(f"SELECT * FROM Income WHERE uid = {uid}"):
                        self.ui.IP_IncomeTable.setItem(row, 1, QTableWidgetItem(str(i[3])))
                        self.ui.IP_IncomeTable.setItem(row, 0, QTableWidgetItem(i[4]))
                        row += 1
                else:
                    showinfo('Ошибка', 'Неправильный формат данных')
            elif command == 'Поиск':
                if id != '' or date != '' or amount != '':
                    zapros = 'SELECT * FROM Income WHERE'
                    if id != '':
                        zapros += f' ID = "{id}",'
                    if amount != '':
                        zapros += f' amount = "{amount}",'
                    if date != '':
                        zapros += f' date = "{date}",'
                    zapros+=f' uid = {uid}'
                    self.clearpage()
                    row = 0
                    self.ui.IP_IncomeTable.setRowCount(len(ask.zapout(zapros)))
                    for i in ask.zapout(zapros):
                        self.ui.IP_IncomeTable.setItem(row, 2, QTableWidgetItem(str(i[3])))
                        self.ui.IP_IncomeTable.setItem(row, 1, QTableWidgetItem(i[4]))
                        self.ui.IP_IncomeTable.setItem(row, 0, QTableWidgetItem(str(i[0])))
                        row += 1
                else:
                    self.ui.IP_IncomeTable.setRowCount(len(ask.zapout(f"SELECT * FROM Income WHERE uid = {uid}")))
                    row = 0
                    for i in ask.zapout(f"SELECT * FROM Income WHERE uid = {uid}"):
                        self.ui.IP_IncomeTable.setItem(row, 2, QTableWidgetItem(str(i[3])))
                        self.ui.IP_IncomeTable.setItem(row, 1, QTableWidgetItem(i[4]))
                        self.ui.IP_IncomeTable.setItem(row, 0, QTableWidgetItem(str(i[0])))
                        row += 1
                        showinfo(title='test', message='test')
        elif page == 'OutcomePage':
            amount = self.ui.OP_AmountInput.toPlainText()
            date = self.ui.OP_DateInput.toPlainText()
            command = self.ui.OP_CommandBox.currentText()
            id = self.ui.OP_IDInput.toPlainText()
            if command == 'Добавить/изменить':
                if id == '' and checkdate(date) and checkint(amount):
                    truth = True
                    aidi = 0
                    while truth:
                        aidi += 1
                        if len(ask.zapout(f"SELECT * FROM Outcome WHERE ID = {aidi}")) == 0:
                            id = aidi
                            truth = False
                    ask.zap(f'INSERT INTO Outcome VALUES ({id}, {uid}, {amount}, "{date}")')
                elif checkint(id):
                    zapros = 'UPDATE Outcome SET'
                    if date != '' or amount != '':
                        if date != '' and checkdate(date):
                            zapros += f' date = "{date}",'
                        if amount != '' and checkint(amount):
                            zapros += f' amount = "{amount}",'
                        zapros = zapros[:-1]
                        zapros += f'WHERE ID = "{id}"'
                        ask.zap(zapros)
                else:
                    showinfo('Ошибка', 'Неправильный формат даты')
                self.ui.OP_OutComeTable.setRowCount(len(ask.zapout(f"SELECT * FROM Outcome WHERE uid = {uid}")))
                row = 0
                for i in ask.zapout(f"SELECT * FROM Outcome WHERE uid = {uid}"):
                    self.ui.OP_OutComeTable.setItem(row, 2, QTableWidgetItem(str(i[2])))
                    self.ui.OP_OutComeTable.setItem(row, 1, QTableWidgetItem(i[3]))
                    self.ui.OP_OutComeTable.setItem(row, 0, QTableWidgetItem(str(i[0])))
                    row += 1
            elif command == 'Удалить':
                if not checkint(id):
                    showinfo('Ошибка', 'Неправильный формат данных')
                else:
                    ask.zap(f'DELETE FROM Outcome WHERE ID = {id}')
                    self.ui.OP_OutComeTable.setRowCount(len(ask.zapout(f"SELECT * FROM Outcome WHERE uid = {uid}")))
                    row = 0
                    for i in ask.zapout(f"SELECT * FROM Outcome WHERE uid = {uid}"):
                        self.ui.OP_OutComeTable.setItem(row, 0, QTableWidgetItem(str(i[0])))
                        self.ui.OP_OutComeTable.setItem(row, 2, QTableWidgetItem(str(i[2])))
                        self.ui.OP_OutComeTable.setItem(row, 1, QTableWidgetItem(i[3]))
                        row += 1
            elif command == 'Поиск':
                if id != '' or date != '' or amount != '':
                    zapros = 'SELECT * FROM Outcome WHERE'
                    if id != '':
                        zapros += f' ID = "{id}",'
                    if amount != '':
                        zapros += f' amount = "{amount}",'
                    if date != '':
                        zapros += f' date = "{date}",'
                    zapros+=f' uid = {uid}'
                    self.clearpage()
                    row = 0
                    self.ui.OP_OutComeTable.setRowCount(len(ask.zapout(zapros)))
                    for i in ask.zapout(zapros):
                        self.ui.OP_OutComeTable.setItem(row, 2, QTableWidgetItem(str(i[2])))
                        self.ui.OP_OutComeTable.setItem(row, 1, QTableWidgetItem(i[3]))
                        self.ui.OP_OutComeTable.setItem(row, 0, QTableWidgetItem(str(i[0])))
                        row += 1
                else:
                    self.ui.OP_OutComeTable.setRowCount(len(ask.zapout(f"SELECT * FROM Outcome WHERE uid = {uid}")))
                    row = 0
                    for i in ask.zapout(f"SELECT * FROM Outcome WHERE uid = {uid}"):
                        self.ui.OP_OutComeTable.setItem(row, 2, QTableWidgetItem(str(i[2])))
                        self.ui.OP_OutComeTable.setItem(row, 1, QTableWidgetItem(i[3]))
                        self.ui.OP_OutComeTable.setItem(row, 0, QTableWidgetItem(str(i[0])))
                        row += 1
        elif page == 'PassivePage':
            amount = self.ui.PP_AmountInput.toPlainText()
            date = self.ui.PP_DateInput.toPlainText()
            command = self.ui.PP_CommandBox.currentText()
            percent = self.ui.PP_DateInput_2.toPlainText()
            id = self.ui.PP_IDInput.toPlainText()
            if command == 'Добавить/изменить':
                if id == '' and checkdate(date) and checkint(amount) and checkint(percent):
                    truth = True
                    aidi = 0
                    while truth:
                        aidi += 1
                        if len(ask.zapout(f"SELECT * FROM PassIncome WHERE ID = {aidi}")) == 0:
                            id = aidi
                            truth = False
                    ask.zap(f'INSERT INTO PassIncome VALUES ({id}, {uid}, "{date}", {amount}, {percent})')
                elif checkint(id):
                    zapros = 'UPDATE PassIncome SET'
                    if date != '' or amount != '' or percent != '':
                        if date != '' and checkdate(date):
                            zapros += f' date = "{date}",'
                        if amount != '' and checkint(amount):
                            zapros += f' buyprice = "{amount}",'
                        if percent != '' and checkint(percent):
                            zapros += f' percent = "{percent}",'
                        zapros = zapros[:-1]
                        zapros += f'WHERE ID = "{id}"'
                        ask.zap(zapros)
                else:
                    showinfo('Ошибка', 'Неправильный формат данных')
                self.ui.PP_PassiveIncomeTable.setRowCount(len(ask.zapout(f"SELECT * FROM PassIncome WHERE uid = {uid}")))
                row = 0
                for i in ask.zapout(f"SELECT * FROM PassIncome WHERE uid = {uid}"):
                    self.ui.PP_PassiveIncomeTable.setItem(row, 2, QTableWidgetItem(str(i[3])))
                    self.ui.PP_PassiveIncomeTable.setItem(row, 1, QTableWidgetItem(i[2]))
                    self.ui.PP_PassiveIncomeTable.setItem(row, 0, QTableWidgetItem(str(i[0])))
                    self.ui.PP_PassiveIncomeTable.setItem(row, 3, QTableWidgetItem(str(f'{i[4]} %')))
                    row += 1
            elif command == 'Удалить':
                if not checkint(id):
                    showinfo('Ошибка', 'Неправильный формат данных')
                else:
                    ask.zap(f'DELETE FROM PassIncome WHERE ID = {id}')
                    self.ui.PP_PassiveIncomeTable.setRowCount(len(ask.zapout(f"SELECT * FROM PassIncome WHERE uid = {uid}")))
                    row = 0
                    for i in ask.zapout(f"SELECT * FROM PassIncome WHERE uid = {uid}"):
                        self.ui.PP_PassiveIncomeTable.setItem(row, 2, QTableWidgetItem(str(i[3])))
                        self.ui.PP_PassiveIncomeTable.setItem(row, 1, QTableWidgetItem(i[2]))
                        self.ui.PP_PassiveIncomeTable.setItem(row, 0, QTableWidgetItem(str(i[0])))
                        self.ui.PP_PassiveIncomeTable.setItem(row, 3, QTableWidgetItem(str(f'{i[4]} %')))
                        row += 1
            elif command == 'Поиск':
                if id != '' or date != '' or amount != '' or percent != '':
                    zapros = 'SELECT * FROM PassIncome WHERE'
                    if id != '':
                        zapros += f' ID = "{id}",'
                    if amount != '':
                        zapros += f' buyprice = "{amount}",'
                    if date != '':
                        zapros += f' date = "{date}",'
                    if percent != '':
                        zapros += f' percent = "{percent}",'
                    zapros+=f' uid = {uid}'
                    self.clearpage()
                    row = 0
                    self.ui.PP_PassiveIncomeTable.setRowCount(len(ask.zapout(zapros)))
                    for i in ask.zapout(zapros):
                        self.ui.PP_PassiveIncomeTable.setItem(row, 2, QTableWidgetItem(str(i[3])))
                        self.ui.PP_PassiveIncomeTable.setItem(row, 1, QTableWidgetItem(i[2]))
                        self.ui.PP_PassiveIncomeTable.setItem(row, 0, QTableWidgetItem(str(i[0])))
                        self.ui.PP_PassiveIncomeTable.setItem(row, 3, QTableWidgetItem(str(f'{i[4]} %')))
                        row += 1
                else:
                    self.ui.PP_PassiveIncomeTable.setRowCount(len(ask.zapout(f"SELECT * FROM PassIncome WHERE uid = {uid}")))
                    row = 0
                    for i in ask.zapout(f"SELECT * FROM PassIncome WHERE uid = {uid}"):
                        self.ui.PP_PassiveIncomeTable.setItem(row, 2, QTableWidgetItem(str(i[3])))
                        self.ui.PP_PassiveIncomeTable.setItem(row, 1, QTableWidgetItem(i[2]))
                        self.ui.PP_PassiveIncomeTable.setItem(row, 0, QTableWidgetItem(str(i[0])))
                        self.ui.PP_PassiveIncomeTable.setItem(row, 3, QTableWidgetItem(str(f'{i[4]} %')))
                        row += 1
        self.startup()



    def clearpage(self):
        a = 0
    def startup(self):
        passincomecheck()
        global uid
        self.ui.IP_IncomeTable.setRowCount(len(ask.zapout(f"SELECT * FROM Income WHERE uid = {uid}")))
        self.ui.OP_OutComeTable.setRowCount(len(ask.zapout(f"SELECT * FROM Outcome WHERE uid = {uid}")))
        self.ui.PP_PassiveIncomeTable.setRowCount(len(ask.zapout(f"SELECT * FROM PassIncome WHERE uid = {uid}")))
        row = 0
        for i in ask.zapout(f"SELECT * FROM Income WHERE uid = {uid}"):
            self.ui.IP_IncomeTable.setItem(row, 2, QTableWidgetItem(str(i[3])))
            self.ui.IP_IncomeTable.setItem(row, 1, QTableWidgetItem(i[4]))
            self.ui.IP_IncomeTable.setItem(row, 0, QTableWidgetItem(str(i[0])))
            row += 1
        row = 0
        for i in ask.zapout(f"SELECT * FROM Outcome WHERE uid = {uid}"):
            self.ui.OP_OutComeTable.setItem(row, 2, QTableWidgetItem(str(i[2])))
            self.ui.OP_OutComeTable.setItem(row, 1, QTableWidgetItem(i[3]))
            self.ui.OP_OutComeTable.setItem(row, 0, QTableWidgetItem(str(i[0])))
            row += 1
        row = 0
        for i in ask.zapout(f"SELECT * FROM PassIncome WHERE uid = {uid}"):
            self.ui.PP_PassiveIncomeTable.setItem(row, 2, QTableWidgetItem(str(i[3])))
            self.ui.PP_PassiveIncomeTable.setItem(row, 1, QTableWidgetItem(i[2]))
            self.ui.PP_PassiveIncomeTable.setItem(row, 0, QTableWidgetItem(str(i[0])))
            self.ui.PP_PassiveIncomeTable.setItem(row, 3, QTableWidgetItem(str(f'{i[4]} %')))
            row += 1
        a = datetime.now()
        a = a.strftime('%d/%m/%Y')
        self.wastedInfo = SomeInfo(str(a))
        self.ui.Date1Label.setText(f'{self.wastedInfo[0][0]} Года')
        self.ui.Date1Label.setStyleSheet('font-size: 18pt')
        self.ui.Date1Income.setText(str(self.wastedInfo[1][0]))
        self.ui.Date1Income.setStyleSheet('font-size: 18pt')
        self.ui.Date1Outcome.setText(str(self.wastedInfo[2][0]))
        self.ui.Date1Outcome.setStyleSheet('font-size: 18pt')
        self.ui.Date1Label_2.setText(f'{self.wastedInfo[0][1]} Года')
        self.ui.Date1Label_2.setStyleSheet('font-size: 18pt')
        self.ui.Date1Income_2.setText(str(self.wastedInfo[1][1]))
        self.ui.Date1Income_2.setStyleSheet('font-size: 18pt')
        self.ui.Date1Outcome_2.setText(str(self.wastedInfo[2][1]))
        self.ui.Date1Outcome_2.setStyleSheet('font-size: 18pt')
        self.ui.Date1Label_3.setText(f'{self.wastedInfo[0][2]} Года')
        self.ui.Date1Label_3.setStyleSheet('font-size: 18pt')
        self.ui.Date1Income_3.setText(str(self.wastedInfo[1][2]))
        self.ui.Date1Income_3.setStyleSheet('font-size: 18pt')
        self.ui.Date1Outcome_3.setText(str(self.wastedInfo[2][2]))
        self.ui.Date1Outcome_3.setStyleSheet('font-size: 18pt')
        self.ui.IP_IncomeRes.setText(str(self.wastedInfo[3][0]))
        self.ui.IP_IncomeRes.setStyleSheet('font-size: 18pt')
        self.ui.OP_ResText.setText(str(self.wastedInfo[3][1]))
        self.ui.OP_ResText.setStyleSheet('font-size: 18pt')
        res1 = self.wastedInfo[1][0] - self.wastedInfo[2][0]
        res2 = self.wastedInfo[1][1] - self.wastedInfo[2][1]
        res3 = self.wastedInfo[1][2] - self.wastedInfo[2][2]
        self.ui.Res1.setText(str(res1))
        if res1 >= 0:
            self.ui.Res1.setStyleSheet('font-size: 24pt; color: #126f0b')
        else:
            self.ui.Res1.setStyleSheet('font-size: 24pt; color:#6f0002')
        self.ui.Res2.setText(str(res2))
        if res2 >= 0:
            self.ui.Res2.setStyleSheet('font-size: 24pt; color: #126f0b')
        else:
            self.ui.Res2.setStyleSheet('font-size: 24pt; color:#6f0002')
        self.ui.Res3.setText(str(res3))
        if res3 >= 0:
            self.ui.Res3.setStyleSheet('font-size: 24pt; color: #126f0b')
        else:
            self.ui.Res3.setStyleSheet('font-size: 24pt; color:#6f0002')



class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setWindowTitle('iWallet - Авторизация')
        self.ui = ulw()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda x: self.checkpass())
        self.ui.createButton.clicked.connect(lambda x: self.newperson())
        self.ui.readyButton.clicked.connect(lambda x: self.createnewperson())
        self.ui.returnButton.clicked.connect(lambda x: self.returnb())
        self.ui.readyButton.setVisible(False)
        self.ui.returnButton.setVisible(False)
        self.ui.label_3.setVisible(False)

    def checkpass(self):
        login = self.ui.LoginSpace.toPlainText()
        password = self.ui.PasswordSpace.text()
        if len(ask.zapout(f'SELECT * FROM User WHERE Login = "{login}"')) == 0:
            showinfo(title='Ошибка', message='Неправильный логин!')
        elif len(ask.zapout(f'SELECT * FROM User WHERE Login = "{login}" AND Password = "{password}"')) == 0:
            showinfo(title='Ошибка', message='Неправильный пароль!')
        else:
            self.hide()
            window.show()
            global uid
            uid = ask.zapout(f'SELECT Id from User WHERE Login = "{login}" AND Password = "{password}"')[0][0]
            window.ui.label.setText(ask.zapout(f'SELECT Login FROM User WHERE Id={uid}')[0][0])
            window.startup()
    def newperson(self):
        self.ui.pushButton.setVisible(False)
        self.ui.createButton.setVisible(False)
        self.ui.readyButton.setVisible(True)
        self.ui.returnButton.setVisible(True)
    def returnb(self):
        self.ui.pushButton.setVisible(True)
        self.ui.createButton.setVisible(True)
        self.ui.readyButton.setVisible(False)
        self.ui.returnButton.setVisible(False)
        self.ui.label_3.setVisible(False)
    def createnewperson(self):
        login = self.ui.LoginSpace.toPlainText()
        password = self.ui.PasswordSpace.text()
        if len(ask.zapout(f'SELECT * FROM User where login = "{login}"')) == 0:
            truth = True
            aidi = 0
            while truth:
                aidi += 1
                if len(ask.zapout(f"SELECT * FROM User WHERE ID = {aidi}")) == 0:
                    id = aidi
                    truth = False
            ask.zap(f'INSERT INTO User VALUES ({id}, "{login}", "{password}")')
            window.show()
            global uid
            uid = ask.zapout(f'SELECT Id from User WHERE Login = "{login}" AND Password = "{password}"')[0][0]
            self.close()
            window.ui.label.setText(ask.zapout(f'SELECT Login FROM User WHERE Id={uid}')[0][0])
            window.startup()
        else:
            self.ui.label_3.setVisible(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ask = Ask()
    logwindow = LoginWindow()
    if len(ask.zapout('SELECT * FROM User')) == 0:
        logwindow.newperson()
        logwindow.ui.returnButton.setVisible(False)
    uid = 0
    window = iWalletWindow()
    logwindow.show()

    def test_timechecker1():
        assert checkdate('03/12/3001') == False
    def test_timechecker2():
        assert checkdate('69/12/2012') == False
    def test_timechecker3():
        assert checkdate('13/24/2012') == False
    def test_timechecker4():
        assert checkdate('12/12/Пиво') == False
    def test_timechecker5():
        assert checkdate('12/12/2016') == True

    sys.exit(app.exec())