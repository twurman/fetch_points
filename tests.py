import requests

#basic test
res = requests.post('http://127.0.0.1:5000/transaction', json={ "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" })
output = res.json()
if res.ok:
    print('basic add transaction test passed')
    print(output)
else:
    print('basic add transaction test failed')


#no payer 
res = requests.post('http://127.0.0.1:5000/transaction', json={ "points": 1000, "timestamp": "2020-11-02T14:00:00Z" })

if not res.ok:
    print('no payer test passed')
else:
    print('no payer test failed')


#no points 
res = requests.post('http://127.0.0.1:5000/transaction', json={ "payer": "DANNON", "timestamp": "2020-11-02T14:00:00Z" })

if not res.ok:
    print('no points test passed')
else:
    print('no points test failed')


#bad timestamp 
res = requests.post('http://127.0.0.1:5000/transaction', json={ "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02" })

if not res.ok:
    print('bad timestamp test passed')
else:
    print('bad timestamp test failed')


#add some others
res = requests.post('http://127.0.0.1:5000/transaction', json={ "payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z" })
res = requests.post('http://127.0.0.1:5000/transaction', json={ "payer": "DANNON", "points": -200, "timestamp": "2020-10-31T15:00:00Z" })
res = requests.post('http://127.0.0.1:5000/transaction', json={ "payer": "MILLER COORS", "points": 10000, "timestamp": "2020-11-01T14:00:00Z" })
res = requests.post('http://127.0.0.1:5000/transaction', json={ "payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z" })

res = requests.post('http://127.0.0.1:5000/balances')
output = res.json()
print(output)

res = requests.post('http://127.0.0.1:5000/spend', json={ "points": 5000 })
output = res.json()
print(output)

res = requests.post('http://127.0.0.1:5000/balances')
output = res.json()
print(output)