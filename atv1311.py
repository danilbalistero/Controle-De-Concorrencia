import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="ATV1311",
    user="postgres",
    password="251406"
)

conn.autocommit = False
cursor = conn.cursor()

def update_quantidade():
    try:
        cursor.execute("SET lock_timeout = '3s'")
        cursor.execute("BEGIN")

        cursor.execute("SELECT quantidade FROM estoque WHERE id = 1")
        quantidade_atual = cursor.fetchone()[0]
        print(f"Quantidade atual do Produto X: {quantidade_atual}")

        nova_quantidade = input("Insira a nova quantidade para o Produto X: ")
        cursor.execute(f"UPDATE estoque SET quantidade = %s WHERE id = 1", [nova_quantidade])
        confirmacao = input("Tem certeza que deseja fazer essa alteração? (sim/não): ")

        if confirmacao.lower() == 'sim':
            conn.commit()
            print("Alteração confirmada.")
        else:
            raise Exception("Alteração não confirmada.")

    except Exception as e:
        print("Erro:", e)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

update_quantidade()
