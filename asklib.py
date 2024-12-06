import sqlite3
import pytest

class Ask:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS "Income" ("ID" INTEGER NOT NULL,"UID" INTEGER NOT NULL,"passid" INTEGER,"amount" INTEGER NOT NULL,"date" TEXT NOT NULL,PRIMARY KEY("ID" AUTOINCREMENT));')
        self.con.commit()
        self.cur.execute('CREATE TABLE IF NOT EXISTS "Outcome" ("ID" INTEGER NOT NULL,"UID" INTEGER NOT NULL,"amount" INTEGER NOT NULL,"date" TEXT NOT NULL,PRIMARY KEY("ID" AUTOINCREMENT));')
        self.con.commit()
        self.cur.execute('CREATE TABLE IF NOT EXISTS "PassIncome" ("ID" INTEGER NOT NULL,"UID" INTEGER NOT NULL,"date" TEXT NOT NULL,"buyprice" INTEGER NOT NULL,"percent" INTEGER NOT NULL,PRIMARY KEY("ID" AUTOINCREMENT),FOREIGN KEY("UID") REFERENCES "User"("ID"));')
        self.con.commit()
        self.cur.execute('CREATE TABLE IF NOT EXISTS "User" ("ID" INTEGER NOT NULL,"Login" TEXT NOT NULL UNIQUE,"Password" TEXT NOT NULL,PRIMARY KEY("ID" AUTOINCREMENT));')
        self.con.commit()
    def do(self, a):
        self.cur.execute(a)
        self.con.commit()
    def result(self, a):
        self.cur.execute(a)
        rows = self.cur.fetchall()
        return rows

ask = Ask('Save.db')
def test_resulttest():
    a = ask.result('SELECT * FROM User')
    assert len(a) > 0
def test_dotest():
    ask.do('INSERT INTO User VALUES (8, "test", "test")')
    a = ask.result('SELECT * FROM User WHERE ID = 8')
    ask.do('DELETE FROM User WHERE ID = 8')
    assert len(a) > 0
