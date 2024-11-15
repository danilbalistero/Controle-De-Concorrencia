import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="ATV1311",
    user="postgres",
    password="251406"
)

conn.autocommit = False
cursor = conn.cursor()

def listar_clientes():
    cursor.execute("SELECT idcliente, nome, limite FROM cliente")
    clientes = cursor.fetchall()
    print("Lista de Clientes:")
    for cliente in clientes:
        print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Limite: {cliente[2]}")
    return clientes

def alterar_cliente():

    try:
        listar_clientes()

        cliente_id = input("Digite o ID do cliente que deseja alterar: ")

        cursor.execute("SELECT idcliente, nome, limite FROM cliente WHERE idcliente = %s", [cliente_id])
        cliente = cursor.fetchone()

        if not cliente:
            print("Cliente não encontrado!")
            return

        print(f"Dados Atuais - ID: {cliente[0]}, Nome: {cliente[1]}, Limite: {cliente[2]}")
        dados_atuais = {"nome": cliente[1], "limite": cliente[2]}

        cursor.execute("SET lock_timeout = '3s'")
        cursor.execute("BEGIN")

        cursor.execute("SELECT idcliente, nome, limite FROM cliente WHERE idcliente = %s", [cliente_id])
        cliente_verificacao = cursor.fetchone()

        if cliente_verificacao[1] != dados_atuais["nome"] or cliente_verificacao[2] != dados_atuais["limite"]:
            print("Os dados foram alterados por outro usuário. Operação cancelada.")
            conn.rollback()
            return

        novo_nome = input("Digite o novo nome: ")
        novo_limite = input("Digite o novo limite (formato 99999.99): ")

        cursor.execute(
            "UPDATE cliente SET nome = %s, limite = %s WHERE idcliente = %s",
            [novo_nome, novo_limite, cliente_id]
        )

        confirmacao = input("Confirma a alteração? (sim/não): ")
        if confirmacao.lower() == 'sim':
            conn.commit()
            print("Alteração confirmada.")
        else:
            raise Exception("Alteração cancelada pelo usuário.")

    except psycopg2.DatabaseError as e:
        if e.pgcode == "55P03":  # Código SQLSTATE para lock timeout
            print("Erro: Outro processo está utilizando o mesmo registro. Por favor, tente novamente mais tarde.")
        else:
            print(f"Erro inesperado: {e}")
        conn.rollback()

    except Exception as e:
        print("Erro:", e)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

# Executar a função
alterar_cliente()
