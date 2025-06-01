# SISTEMA DE CONTROLE DE ESTOQUE DASA
# Integrantes: Alexandre Faria, Caio Rossini, Gabriel Danius e Enzo Motta
# RM:558270, 555084, 555747 E 555372

from datetime import datetime  # Biblioteca para registrar data e hora das ações

# Estrutura principal de dados: dicionário para o estoque e lista para o histórico
estoque = {}      # Armazena produtos, quantidades, preços e preço ideal
historico = []    # Armazena registros de atividades do sistema

# Função para calcular o preço total de um produto
def calcular_preco_total(quantidade, preco_unitario):
    """
    Retorna o preço total de um produto (quantidade * preço unitário).
    """
    return quantidade * preco_unitario

# Função para registrar um novo produto no estoque
def registrar_produto():
    """
    Solicita ao usuário nome, quantidade e preço unitário do produto.
    Registra o produto no estoque e adiciona ao histórico.
    """
    produto = input("Nome do produto: ").strip().lower()
    if produto in estoque:
        print("Produto já cadastrado. Use a opção de atualização de preço.")
        return
    try:
        quantidade = int(input("Quantidade: "))
        preco_unitario = float(input("Preço unitário: "))
    except ValueError:
        print("Valores inválidos. Tente novamente.")
        return
    preco_total = calcular_preco_total(quantidade, preco_unitario)
    # Estrutura aninhada para cada produto
    estoque[produto] = {
        'quantidade': quantidade,
        'preco_unitario': preco_unitario,
        'preco_total': preco_total,
        'preco_ideal': preco_total  # Inicialmente igual ao total
    }
    print(f"Produto '{produto}' registrado com sucesso! Preço total: R${preco_total:.2f}")
    historico.append(f"{datetime.now()} - Registro: {produto} (quantidade={quantidade}, preço unitário=R${preco_unitario:.2f})")

# Função para atualizar o preço de um produto já existente
def atualizar_preco():
    """
    Permite atualizar o preço unitário de um produto já cadastrado.
    Recalcula o preço total e registra a alteração no histórico.
    """
    produto = input("Produto para atualizar: ").strip().lower()
    if produto not in estoque:
        print("Produto não encontrado.")
        return
    try:
        novo_preco = float(input("Novo preço unitário: "))
    except ValueError:
        print("Valor inválido.")
        return
    estoque[produto]['preco_unitario'] = novo_preco
    estoque[produto]['preco_total'] = calcular_preco_total(
        estoque[produto]['quantidade'], novo_preco)
    print(f"Preço de '{produto}' atualizado com sucesso! Novo preço total: R${estoque[produto]['preco_total']:.2f}")
    historico.append(f"{datetime.now()} - Atualização: {produto} (novo preço unitário=R${novo_preco:.2f})")

# Função para listar todos os produtos cadastrados
def listar_produtos():
    """
    Lista todos os produtos cadastrados, mostrando quantidade, preço unitário e preço total.
    """
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
    print("\n=== PRODUTOS CADASTRADOS ===")
    for produto in sorted(estoque.keys()):
        dados = estoque[produto]
        print(f"{produto.upper():<15} Quantidade: {dados['quantidade']:<5} Preço Unitário: R${dados['preco_unitario']:.2f}  Preço Total: R${dados['preco_total']:.2f}")

# Função para gerar o relatório de atividades
def gerar_relatorio():
    """
    Mostra o histórico das últimas 10 ações realizadas no sistema.
    """
    print("\n=== HISTÓRICO DE ATIVIDADES ===")
    if not historico:
        print("Nenhuma atividade registrada.")
        return
    for registro in historico[-10:]:
        print(registro)

# Função para exibir o menu e solicitar opção válida do usuário
def menu():
    """
    Exibe o menu principal e solicita uma opção válida do usuário.
    """
    print("\n=== SISTEMA DE ESTOQUE ===")
    print("1. Registrar novo produto")
    print("2. Atualizar preço de produto")
    print("3. Listar produtos cadastrados")
    print("4. Gerar relatório de atividades")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

# Função principal para rodar o sistema
def main():
    """
    Executa o sistema de menu interativo até o usuário escolher sair.
    """
    while True:
        opcao = menu()
        if opcao == '1':
            registrar_produto()
        elif opcao == '2':
            atualizar_preco()
        elif opcao == '3':
            listar_produtos()
        elif opcao == '4':
            gerar_relatorio()
        elif opcao == '5':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa
if __name__ == "__main__":
    main()
