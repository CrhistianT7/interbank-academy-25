import csv

def get_final_balance(transactions):
    """
    Calculates the final balance based on a list of transactions.

    Each transaction is expected to be a dictionary with:
    - 'type': Either "Crédito" (credit) or "Débito" (debit)
    - 'amount': A float representing the transaction amount

    Credits add to the balance, debits subtract from it.

    Args:
        transactions (List[dict]): A list of transaction dictionaries.

    Returns:
        float: The resulting balance after applying all transactions.
    """
    return sum(t["amount"] if t["type"] == "Crédito" else -t["amount"] for t in transactions)

def get_highest_transaction(transactions):
    """
    Returns the transaction with the highest amount from a list of transactions.

    Each transaction in the list should be a dictionary containing:
    - 'amount': A float representing the transaction amount

    Args:
        transactions (List[dict]): A list of transaction dictionaries.

    Returns:
        dict: The transaction with the highest 'amount' value.
    """
    return max(transactions, key= lambda t: t["amount"])

def count_transactions(transactions):
    """
    Counts the number of "Crédito" (credit) and "Débito" (debit) transactions in the given list.

    Each transaction should be a dictionary with a 'type' key indicating
    whether it's a credit ("Crédito") or debit ("Débito").

    Args:
        transactions (List[dict]): A list of transaction dictionaries.

    Returns:
        dict: A dictionary with the count of each transaction type:
              {
                  "Crédito": <number_of_credit_transactions>,
                  "Débito": <number_of_debit_transactions>
              }
    """
    types = [t["type"] for t in transactions]
    return {
        "Crédito": types.count("Crédito"),
        "Débito": types.count("Débito")
    }

def add_transaction(file_name):
    """
    Prompts the user to input a new transaction and appends it to the specified CSV file.

    The function requests the following information from the user:
    - 'id': The identifier for the transaction.
    - 'type': The type of transaction (either "Crédito" or "Débito").
    - 'amount': The amount of the transaction, which is expected to be a float.

    The transaction is then appended to the CSV file with the given file name.

    Args:
        file_name (str): The path to the CSV file where the transaction will be appended.

    Returns:
        None: This function modifies the file and prints a success or error message.
    
    Raises:
        ValueError: If the amount is not a valid float.
        IOError: If there is an error opening or writing to the file.
    """
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
    """
    Prompts the user to input the ID of a transaction to remove and updates the CSV file.

    This function looks for a transaction in the provided list of transactions by its ID.
    If the transaction is found, it is removed from both the in-memory list and the file.
    If the transaction is not found, a message is printed indicating the transaction was not found.

    Args:
        transactions (List[dict]): A list of transaction dictionaries, where each dictionary
                                   contains 'id', 'type', and 'amount'.
        file_name (str): The path to the CSV file where transactions are stored.

    Returns:
        None: The function modifies the file and prints a success or error message.

    Raises:
        IOError: If there is an error opening or writing to the file.
    """
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