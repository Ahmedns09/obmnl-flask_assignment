# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route('/')
def get_transactions():
    return render_template('transactions.html', transactions=transactions)

# Create operation
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if(request.method == 'GET'):
        return render_template("form.html")
    
    elif(request.method == 'POST'):
        new_date = request.form['date']
        new_amount = float(request.form['amount'])
        new_id = len(transactions) + 1
        transactions.append({'id': new_id, 'date': new_date, 'amount': new_amount})
        return redirect(url_for("get_transactions"))

# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    transaction = next((t for t in transactions if t['id'] == transaction_id), None)
    if not transaction:
        return "Transaction not found", 404

    if request.method == 'GET':
        return render_template('edit.html', transaction=transaction)

    elif request.method == 'POST':
        transaction['date'] = request.form['date']
        transaction['amount'] = float(request.form['amount'])
        return redirect(url_for("get_transactions"))

# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break
    return redirect(url_for("get_transactions"))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)