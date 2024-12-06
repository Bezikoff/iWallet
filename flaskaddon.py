import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('Save.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/users', methods=['GET'])
def get_all_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM User').fetchall()
    conn.close()
    result = [dict(zip(row.keys(), row)) for row in users]
    return jsonify(result)

@app.route('/users/<int:id>', methods=['GET'])
def get_one_user(id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM User WHERE ID = ?', (id,)).fetchone()
    conn.close()
    if not user:
        return 'Пользователь не найден.', 404
    result = dict(zip(user.keys(), user))
    return jsonify(result)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = (data['Login'], data['Password'])
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO User (Login, Password) VALUES (?, ?)", new_user)
    conn.commit()
    conn.close()
    
    return f'Пользователь {new_user[0]} успешно создан.', 201

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    updated_user = (data['Login'], data['Password'], id)
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE User SET Login=?, Password=? WHERE ID=?", updated_user)
    conn.commit()
    conn.close()
    
    return f'Информация о пользователе {updated_user[0]} обновлена.', 200

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM User WHERE ID=?", (id,))
    conn.commit()
    conn.close()
    
    return f'Пользователь с id={id} удален.', 204

@app.route('/incomes', methods=['GET'])
def get_all_incomes():
    conn = get_db_connection()
    incomes = conn.execute('SELECT * FROM Income').fetchall()
    conn.close()
    result = [dict(zip(row.keys(), row)) for row in incomes]
    return jsonify(result)

@app.route('/incomes/<int:id>', methods=['GET'])
def get_one_income(id):
    conn = get_db_connection()
    income = conn.execute('SELECT * FROM Income WHERE ID = ?', (id,)).fetchone()
    conn.close()
    if not income:
        return 'Доход не найден.', 404
    result = dict(zip(income.keys(), income))
    return jsonify(result)

@app.route('/incomes', methods=['POST'])
def create_income():
    data = request.get_json()
    new_income = (data['UID'], data['passid'], data['amount'], data['date'])
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Income (UID, passid, amount, date) VALUES (?, ?, ?, ?)", new_income)
    conn.commit()
    conn.close()
    
    return f'Новый доход добавлен.', 201

@app.route('/incomes/<int:id>', methods=['PUT'])
def update_income(id):
    data = request.get_json()
    updated_income = (data['UID'], data['passid'], data['amount'], data['date'], id)
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE Income SET UID=?, passid=?, amount=?, date=? WHERE ID=?", updated_income)
    conn.commit()
    conn.close()
    
    return f'Доход с id={id} обновлен.', 200

@app.route('/incomes/<int:id>', methods=['DELETE'])
def delete_income(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Income WHERE ID=?", (id,))
    conn.commit()
    conn.close()
    
    return f'Доход с id={id} удален.', 204

@app.route('/outcomes', methods=['GET'])
def get_all_outcomes():
    conn = get_db_connection()
    outcomes = conn.execute('SELECT * FROM Outcome').fetchall()
    conn.close()
    result = [dict(zip(row.keys(), row)) for row in outcomes]
    return jsonify(result)

@app.route('/outcomes/<int:id>', methods=['GET'])
def get_one_outcome(id):
    conn = get_db_connection()
    outcome = conn.execute('SELECT * FROM Outcome WHERE ID = ?', (id,)).fetchone()
    conn.close()
    if not outcome:
        return 'Расход не найден.', 404
    result = dict(zip(outcome.keys(), outcome))
    return jsonify(result)

@app.route('/outcomes', methods=['POST'])
def create_outcome():
    data = request.get_json()
    new_outcome = (data['UID'], data['amount'], data['date'])
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Outcome (UID, amount, date) VALUES (?, ?, ?)", new_outcome)
    conn.commit()
    conn.close()
    
    return f'Новый расход добавлен.', 201

@app.route('/outcomes/<int:id>', methods=['PUT'])
def update_outcome(id):
    data = request.get_json()
    updated_outcome = (data['UID'], data['amount'], data['date'], id)
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE Outcome SET UID=?, amount=?, date=? WHERE ID=?", updated_outcome)
    conn.commit()
    conn.close()
    
    return f'Расход с id={id} обновлен.', 200

@app.route('/outcomes/<int:id>', methods=['DELETE'])
def delete_outcome(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Outcome WHERE ID=?", (id,))
    conn.commit()
    conn.close()
    
    return f'Расход с id={id} удален.', 204

@app.route('/passincomes', methods=['GET'])
def get_all_passincomes():
    conn = get_db_connection()
    passincomes = conn.execute('SELECT * FROM PassIncome').fetchall()
    conn.close()
    result = [dict(zip(row.keys(), row)) for row in passincomes]
    return jsonify(result)

@app.route('/passincomes/<int:id>', methods=['GET'])
def get_one_passincome(id):
    conn = get_db_connection()
    passincome = conn.execute('SELECT * FROM PassIncome WHERE ID = ?', (id,)).fetchone()
    conn.close()
    if not passincome:
        return 'Пассивный доход не найден.', 404
    result = dict(zip(passincome.keys(), passincome))
    return jsonify(result)

@app.route('/passincomes', methods=['POST'])
def create_passincome():
    data = request.get_json()
    new_passincome = (data['UID'], data['date'], data['buyprice'], data['percent'])
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO PassIncome (UID, date, buyprice, percent) VALUES (?, ?, ?, ?)", new_passincome)
    conn.commit()
    conn.close()
    
    return f'Новый пассивный доход добавлен.', 201

@app.route('/passincomes/<int:id>', methods=['PUT'])
def update_passincome(id):
    data = request.get_json()
    updated_passincome = (data['UID'], data['date'], data['buyprice'], data['percent'], id)
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE PassIncome SET UID=?, date=?, buyprice=?, percent=? WHERE ID=?", updated_passincome)
    conn.commit()
    conn.close()
    
    return f'Пассивный доход с id={id} обновлен.', 200

@app.route('/passincomes/<int:id>', methods=['DELETE'])
def delete_passincome(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM PassIncome WHERE ID=?", (id,))
    conn.commit()
    conn.close()
    
    return f'Пассивный доход с id={id} удален.', 204

if __name__ == '__main__':
    app.run(debug=True)
