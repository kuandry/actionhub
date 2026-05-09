import sqlite3

DB_PATH = "instance/database.db"

def show_tables(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("\nTabelas no banco:")
    for t in tables:
        print("-", t[0])

def query_table(cursor, table):
    try:
        cursor.execute(f"SELECT * FROM {table} LIMIT 10;")
        rows = cursor.fetchall()
        print(f"\nPrimeiros registros da tabela {table}:")
        for row in rows:
            print(row)
    except Exception as e:
        print("Erro ao consultar:", e)

def run_custom_query(cursor, query):
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        print("\nResultado da query:")
        for row in rows:
            print(row)
    except Exception as e:
        print("Erro ao executar query:", e)

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    while True:
        print("\n=== Menu ===")
        print("1 - Listar tabelas")
        print("2 - Consultar registros de uma tabela")
        print("3 - Rodar query livre")
        print("4 - Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            show_tables(cursor)
        elif choice == "2":
            table = input("Digite o nome da tabela: ")
            query_table(cursor, table)
        elif choice == "3":
            query = input("Digite sua query SQL: ")
            run_custom_query(cursor, query)
        elif choice == "4":
            break
        else:
            print("Opção inválida.")

    conn.close()

if __name__ == "__main__":
    main()
