from helpers import read_transactions
from methods import get_final_balance, get_highest_transaction
from methods import count_transactions, add_transaction, remove_transaction

def runApplication():
    file_name = "data.csv"
    while True:
        print("""
-----------------------------------
Select one of the following options
-----------------------------------
1. Get final balance
2. Get highest amount transaction
3. Count transactions
4. Add transaction
5. Remove transaction
6. salir
        """)
        option = int(input("Select an option> "))
        transactions = read_transactions(file_name)
        match option:
            case 1:
                final_balance = get_final_balance(transactions)
                print("\nFinal Balance: ", round(final_balance,2))
            case 2:
                highest_transaction = get_highest_transaction(transactions)
                print("\nHighest transaction: ID ", highest_transaction["id"], " - ", highest_transaction["amount"])
            case 3:
                count = count_transactions(transactions)
                print("\nTransactions count: Crédito: ", count["Crédito"], " Débito: ", count["Débito"])
            case 4:
                add_transaction(file_name)
            case 5:
                remove_transaction(transactions, file_name)
            case 6:
                print("Thank you for using the application\n")
                break
            case _:
                print("\nINVALID OPTION*****")
                

if __name__ == "__main__":
    runApplication()