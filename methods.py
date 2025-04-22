import csv

def get_final_balance(transactions):
    return sum(t["amount"] if t["type"] == "Crédito" else -t["amount"] for t in transactions)

def get_highest_transaction(transactions):
    return max(transactions, key= lambda t: t["amount"])

def count_transactions(transactions):
    types = [t["type"] for t in transactions]
    return {
        "Crédito": types.count("Crédito"),
        "Débito": types.count("Débito")
    }

def add_transaction(file_name):
    try:
        id = input("Id: ")
        _type = input("Type (Crédito/Débito): ")
        amount = float(input("Amount: "))
        
        with open(file_name, "a", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([id, _type, amount])
        print("Transaction added successfully") 
    except:
        print("Error adding transaction")

def remove_transaction(transactions, file_name):
    try:
        id = input("Enter the ID of the transaction to remove: ")
        filtered_transactions = [t for t in transactions if t["id"] != id]
        
        if len(transactions) == len(filtered_transactions):
            print("Transaction with ", id, " Not found!")
            return 
        
        with open(file_name, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["id", "tipo", "monto"])
            for t in filtered_transactions:
                writer.writerow([t["id"], t["type"], t["amount"]])
        print("Transaction removed succesfully")
    except:
        print("Error removing transaction")