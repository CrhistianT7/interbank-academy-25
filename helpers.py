import csv

def read_transactions(file_name):
    transactions = []
    with open(file_name, newline='', encoding='utf-8') as file:
        dataDic = csv.DictReader(file)
        for row in dataDic:
            id = row['id']
            _type = row['tipo']
            
            try:
                amount = float(row['monto'])
                transactions.append({
                    "id": id,
                    "type": _type,
                    "amount": amount
                })
            except:
                continue
    return transactions