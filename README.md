# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

1. **Introduction**  
    Desarrolla una aplicación de línea de comandos (CLI) que procese un archivo CSV con transacciones bancarias y genere un reporte que incluya:

   **Balance Final:**  
   Suma de los montos de las transacciones de tipo "Crédito" menos la suma de los montos de las transacciones de tipo "Débito".

   **Transacción de Mayor Monto:**  
   Identificar el ID y el monto de la transacción con el valor más alto.

   **Conteo de Transacciones:**  
   Número total de transacciones para cada tipo ("Crédito" y "Débito").

---

2. **Instruction of execution**
   - Install Python 10 or higher
   - Run the following command in the console
   ```bash
    python3 main.py
   ```
   - Select options in the menu and enjoy the project

---

3. **Approach and Solution**  
   For the solution, I first analized the problem and search for a library to read csv files, since the data comes from a file of this type.

   Then I started coding the main methods, separeted into 3 files, the project structure is in the next step. The methods are:

   ```
   read_transactions(file_name)
   get_final_balance(transactions)
   get_highest_transaction(transactions)
   count_transactions(transactions)
   add_transaction(file_name)
   remove_transaction(transactions, file_name)
   ```

   These methods are then structured in the main file where I created a menu so the user can interact with the application.

---

4. **Project Structure**

```
Interbank-academy-25/
├── helpers.py       # Helper functions
│   └── read_transactions()  # Reads and parses transaction data
├── main.py          # Main execution script
└── methods.py       # Additional logic and methods
```
