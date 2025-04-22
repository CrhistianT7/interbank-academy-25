import csv

def read_transactions(file_name):
    """
    Reads a CSV file containing transaction data and returns a list of valid transactions.

    Each row in the CSV is expected to have the following columns:
    - 'id': The identifier of the transaction
    - 'tipo': The type of the transaction
    - 'monto': The amount of the transaction (should be convertible to float)

    Any row with an invalid 'monto' value (i.e., not convertible to float) will be skipped.

    Args:
        file_name (str): Path to the CSV file.

    Returns:
        List[dict]: A list of transactions, where each transaction is represented as a dictionary
                    with keys 'id', 'type', and 'amount'.
    """
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