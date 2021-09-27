from flask import Flask, request, jsonify
from sortedcontainers import SortedList
from datetime import datetime
from transaction import Transaction

app = Flask(__name__)
transactions = SortedList(key=lambda x: x.timestamp)
payers = dict()

@app.route('/transaction', methods=['GET', 'POST'])
def record_transaction():
    json = request.json
    if 'payer' not in json or 'points' not in json or 'timestamp' not in json:
        return jsonify({'error': f'request must contain \'payer\', \'points\', and \'timestamp\': {json}'}), 400
    
    payer = json['payer']
    points = int(json['points'])
    try:
        timestamp = datetime.strptime(json['timestamp'], '%Y-%m-%dT%H:%M:%SZ')
    except:
        return jsonify({'error': 'invalid timestamp format; must be %Y-%m-%dT%H:%M:%SZ'}), 400

    transactions.add(Transaction(payer, points, timestamp))

    if payer not in payers:
        payers[payer] = 0
    payers[payer] += points

    return jsonify({'payer': payer, 'points': points, 'timestamp': timestamp})


@app.route('/spend', methods=['GET', 'POST'])
def spend_points():
    json = request.json
    if 'points' not in json:
        return jsonify({'error': f'request must contain \'points\': {json}'}), 400
    
    remaining_points = int(json['points'])
    spent_points = dict()
    while remaining_points > 0 and len(transactions) > 0:
        transaction = transactions.pop(0)
        if transaction.payer not in spent_points:
            spent_points[transaction.payer] = 0

        if remaining_points - transaction.points < 0:
            spent_points[transaction.payer] += remaining_points
            transaction.points -= remaining_points
            transactions.add(transaction)
            payers[transaction.payer] -= remaining_points
            remaining_points = 0
        else:
            spent_points[transaction.payer] += transaction.points
            payers[transaction.payer] -= transaction.points
            remaining_points -= transaction.points


    return jsonify(spent_points)


@app.route('/balances', methods=['GET', 'POST'])
def view_balances():
    return jsonify(payers)


@app.route('/')
def hello_world():
    return 'Welcome to fetch points!'