# SISTEMA DE CONTROLE DE ESTOQUE DASA
# Integrantes: Alexandre Faria, Caio Rossini, Gabriel Danius e Enzo Motta
# RM:558270, 555084, 555747 E 555372

# SISTEMA DE CONTROLE DE ESTOQUE DASA
# Integrantes: Caio Rossini, Gabriel Danius e Enzo Motta
# RM:555084, 555747 E 555372

from datetime import datetime, timedelta
import random

# ======================================================================
# ESTRUTURAS DE DADOS GLOBAIS
# ======================================================================
estoque = {}  # Armazena produtos disponíveis, suas quantidades e preços. É a "prateleira".
historico = []  # Armazena registros de atividades do sistema (ex: "produto X foi cadastrado").
registro_consumo = []  # Armazena o histórico de todos os insumos que já foram consumidos. É o "livro de registros".


# ======================================================================
# IMPLEMENTAÇÃO DE ESTRUTURAS DE DADOS E ALGORITMOS CLÁSSICOS
# ======================================================================

# 1. Fila (Queue) - Para registrar consumo em ordem cronológica (FIFO)
class Fila:
    """Implementação de uma Fila usando uma lista Python."""

    def __init__(self):
        self.items = []

    def enfileirar(self, item):
        """Adiciona um item ao final da fila."""
        self.items.append(item)
        print(f"CONSUMO REGISTRADO NA FILA: {item['insumo']}, Quantidade: {item['quantidade']}")

    def desenfileirar(self):
        """Remove e retorna o item do início da fila."""
        if not self.esta_vazia():
            return self.items.pop(0)
        return None

    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.items) == 0

    def ver_fila(self):
        """Retorna uma representação da fila."""
        return self.items


# 2. Pilha (Stack) - Para consultar consumos em ordem inversa (LIFO)
class Pilha:
    """Implementação de uma Pilha usando uma lista Python."""

    def __init__(self):
        self.items = []

    def empilhar(self, item):
        """Adiciona um item ao topo da pilha."""
        self.items.append(item)

    def desempilhar(self):
        """Remove e retorna o item do topo da pilha."""
        if not self.esta_vazia():
            return self.items.pop()
        return None

    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self.items) == 0


# 3. Estruturas de Busca
def busca_sequencial(lista, chave, valor_buscado):
    """Busca um item em uma lista de dicionários de forma sequencial (Complexidade: O(n))."""
    for item in lista:
        if item[chave].lower() == valor_buscado.lower():
            return item
    return None


def busca_binaria(lista_ordenada, chave, valor_buscado):
    """Busca um item em uma lista de dicionários ORDENADA (Complexidade: O(log n))."""
    inicio, fim = 0, len(lista_ordenada) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        valor_meio = lista_ordenada[meio][chave].lower()

        if valor_meio < valor_buscado.lower():
            inicio = meio + 1
        elif valor_meio > valor_buscado.lower():
            fim = meio - 1
        else:
            return lista_ordenada[meio]
    return None


# 4. Algoritmos de Ordenação
def merge_sort(lista, chave):
    """Implementação do Merge Sort (Complexidade: O(n log n))."""
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave)
    direita = merge_sort(lista[meio:], chave)
    return merge(esquerda, direita, chave)


def merge(esquerda, direita, chave):
    """Função auxiliar para o Merge Sort."""
    resultado = []
    i, j = 0, 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i][chave] < direita[j][chave]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


def quick_sort(lista, chave):
    """Implementação do Quick Sort (Complexidade Média: O(n log n))."""
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2][chave]
    menores = [x for x in lista if x[chave] < pivo]
    iguais = [x for x in lista if x[chave] == pivo]
    maiores = [x for x in lista if x[chave] > pivo]
    return quick_sort(menores, chave) + iguais + quick_sort(maiores, chave)


# ======================================================================
# FUNÇÕES PRINCIPAIS DO SISTEMA DE ESTOQUE
# ======================================================================

def calcular_preco_total(quantidade, preco_unitario):
    """Retorna o preço total de um produto (quantidade * preço unitário)."""
    return quantidade * preco_unitario


def registrar_produto():
    """Solicita ao usuário dados de um novo produto e o adiciona ao estoque."""
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
    estoque[produto] = {
        'quantidade': quantidade,
        'preco_unitario': preco_unitario,
        'preco_total': preco_total,
    }
    print(f"\nProduto '{produto}' registrado com sucesso! Preço total: R${preco_total:.2f}")
    # Mensagem de confirmação da integração
    print(f"--> O produto '{produto}' já está disponível para registrar consumo no Menu 5.")
    historico.append(
        f"{datetime.now()} - Registro: {produto} (quantidade={quantidade}, preço unitário=R${preco_unitario:.2f})")


def atualizar_preco():
    """Permite atualizar o preço unitário de um produto já cadastrado."""
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


def listar_produtos():
    """Lista todos os produtos cadastrados no estoque e suas quantidades atuais."""
    if not estoque:
        print("Nenhum produto cadastrado no estoque.")
        return
    print("\n=== ESTOQUE ATUAL DE PRODUTOS ===")
    for produto in sorted(estoque.keys()):
        dados = estoque[produto]
        print(
            f"{produto.upper():<25} Quantidade: {dados['quantidade']:<5} Preço Unitário: R${dados['preco_unitario']:.2f}  Preço Total: R${dados['preco_total']:.2f}")


def gerar_relatorio():
    """Mostra o histórico das últimas 10 ações realizadas no sistema (cadastros, atualizações)."""
    print("\n=== HISTÓRICO DE ATIVIDADES ===")
    if not historico:
        print("Nenhuma atividade registrada.")
        return
    for registro in historico[-10:]:
        print(registro)


# ======================================================================
# FUNÇÕES DE GERENCIAMENTO DE CONSUMO (MÓDULO INTEGRADO)
# ======================================================================

fila_consumo = Fila()


def simular_dados_iniciais():
    """Pré-popula o estoque e o registro de consumo com dados de exemplo."""
    global registro_consumo, estoque
    insumos_simulados = {
        'reagente alfa': {'quantidade': 500, 'preco_unitario': 25.50},
        'seringa descartável': {'quantidade': 2000, 'preco_unitario': 1.20},
        'tubo de ensaio': {'quantidade': 1500, 'preco_unitario': 0.50},
        'luva cirúrgica': {'quantidade': 3000, 'preco_unitario': 2.00},
        'placa de petri': {'quantidade': 800, 'preco_unitario': 3.75}
    }
    # Adiciona os insumos simulados ao estoque principal
    for nome, dados in insumos_simulados.items():
        estoque[nome] = {
            'quantidade': dados['quantidade'],
            'preco_unitario': dados['preco_unitario'],
            'preco_total': dados['quantidade'] * dados['preco_unitario']
        }

    # Simula alguns eventos de consumo, dando baixa no estoque
    for _ in range(10):
        insumo_nome = random.choice(list(estoque.keys()))
        qtd_consumida = random.randint(10, 50)

        if estoque[insumo_nome]['quantidade'] >= qtd_consumida:
            estoque[insumo_nome]['quantidade'] -= qtd_consumida
            consumo = {
                'insumo': insumo_nome,
                'quantidade': qtd_consumida,
                'data_consumo': datetime.now() - timedelta(days=random.randint(1, 30)),
                'validade': datetime(2026, random.randint(1, 12), random.randint(1, 28))
            }
            registro_consumo.append(consumo)
            fila_consumo.enfileirar(consumo)
    print("Dados de estoque e consumo iniciais simulados com sucesso.")


def registrar_consumo_manual():
    """Permite ao usuário registrar um consumo, interagindo diretamente com o estoque."""
    print("\n--- Insumos Disponíveis no Estoque ---")
    if not estoque:
        print("Nenhum produto no estoque. Cadastre um produto no menu principal primeiro.")
    else:
        for p in sorted(estoque.keys()):
            print(f"- {p.capitalize()} (Qtd: {estoque[p]['quantidade']})")

    try:
        insumo = input("\nDigite o nome do insumo consumido (ou um novo nome): ").strip().lower()
        quantidade = int(input("Quantidade consumida: "))

        # Lógica de integração com o estoque
        if insumo in estoque:
            if estoque[insumo]['quantidade'] >= quantidade:
                estoque[insumo]['quantidade'] -= quantidade
                print(
                    f"BAIXA NO ESTOQUE: {quantidade} unidades de '{insumo}'. Estoque restante: {estoque[insumo]['quantidade']}")
            else:
                print(
                    f"AVISO: Consumo de {quantidade} excede o estoque de {estoque[insumo]['quantidade']}. O estoque ficará negativo.")
                estoque[insumo]['quantidade'] -= quantidade
        else:
            print(f"AVISO: O insumo '{insumo}' não está cadastrado no estoque principal.")
            adicionar = input("Deseja adicioná-lo agora? (s/n): ").lower()
            if adicionar == 's':
                preco_unitario = float(input(f"Qual o preço unitário de '{insumo}'? "))
                estoque[insumo] = {'quantidade': -quantidade, 'preco_unitario': preco_unitario, 'preco_total': 0}
                print(f"'{insumo}' adicionado ao estoque com saldo inicial de -{quantidade} (refletindo este consumo).")
                historico.append(f"{datetime.now()} - Registro via consumo: {insumo}")

        # Registra o evento no histórico de consumo
        ano_validade = int(input("Ano de validade (AAAA): "))
        mes_validade = int(input("Mês de validade (MM): "))
        dia_validade = int(input("Dia de validade (DD): "))

        novo_consumo = {
            'insumo': insumo,
            'quantidade': quantidade,
            'data_consumo': datetime.now(),
            'validade': datetime(ano_validade, mes_validade, dia_validade)
        }
        registro_consumo.append(novo_consumo)
        fila_consumo.enfileirar(novo_consumo)

    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira números para quantidade e datas.")


def ver_ultimos_consumos():
    """Usa uma Pilha para mostrar os últimos consumos registrados (LIFO)."""
    if not registro_consumo:
        print("Nenhum consumo registrado.")
        return
    pilha_consulta = Pilha()
    for consumo in registro_consumo:
        pilha_consulta.empilhar(consumo)
    print("\n--- CONSULTA DE ÚLTIMOS CONSUMOS (DO MAIS RECENTE PARA O MAIS ANTIGO) ---")
    while not pilha_consulta.esta_vazia():
        consumo = pilha_consulta.desempilhar()
        print(
            f"Insumo: {consumo['insumo']}, Qtd: {consumo['quantidade']}, Data: {consumo['data_consumo'].strftime('%d/%m/%Y')}")


def buscar_consumo_insumo():
    """Menu para buscar um insumo no histórico de consumo."""
    if not registro_consumo:
        print("Nenhum consumo para buscar.")
        return
    insumo_buscado = input("Qual insumo deseja buscar no histórico de consumo? ").strip()
    print("Escolha o método de busca:\n1. Busca Sequencial\n2. Busca Binária")
    opcao = input("Opção: ")
    if opcao == '1':
        resultado = busca_sequencial(registro_consumo, 'insumo', insumo_buscado)
    elif opcao == '2':
        print("...Ordenando a lista por nome para a busca binária...")
        lista_ordenada = sorted(registro_consumo, key=lambda x: x['insumo'])
        resultado = busca_binaria(lista_ordenada, 'insumo', insumo_buscado)
    else:
        print("Opção inválida.");
        return
    if resultado:
        print("\n--- Primeiro Registro Encontrado ---")
        print(
            f"Insumo: {resultado['insumo']}, Qtd: {resultado['quantidade']}, Data: {resultado['data_consumo'].strftime('%d/%m/%Y')}, Validade: {resultado['validade'].strftime('%d/%m/%Y')}")
    else:
        print(f"\nNenhum registro de consumo encontrado para o insumo '{insumo_buscado}'.")


def ordenar_registros_consumo():
    """Menu para ordenar o histórico de consumo usando diferentes algoritmos e critérios."""
    if not registro_consumo:
        print("Nenhum consumo para ordenar.")
        return
    print("Ordenar histórico por:\n1. Quantidade Consumida\n2. Data de Validade")
    chave_ord = input("Opção: ")
    chave = 'quantidade' if chave_ord == '1' else 'validade' if chave_ord == '2' else None
    if not chave: print("Opção de chave inválida."); return
    print("\nEscolha o algoritmo de ordenação:\n1. Merge Sort\n2. Quick Sort")
    algo_ord = input("Opção: ")
    lista_para_ordenar = list(registro_consumo)
    if algo_ord == '1':
        ordenada = merge_sort(lista_para_ordenar, chave)
        print(f"\n--- HISTÓRICO ORDENADO POR '{chave.upper()}' (MERGE SORT) ---")
    elif algo_ord == '2':
        ordenada = quick_sort(lista_para_ordenar, chave)
        print(f"\n--- HISTÓRICO ORDENADO POR '{chave.upper()}' (QUICK SORT) ---")
    else:
        print("Opção de algoritmo inválida.");
        return
    for item in ordenada:
        valor = item[chave]
        valor_formatado = valor.strftime('%d/%m/%Y') if isinstance(valor, datetime) else valor
        print(f"Insumo: {item['insumo']:<25} | {chave.replace('_', ' ').capitalize()}: {valor_formatado}")


# ======================================================================
# MENUS E EXECUÇÃO PRINCIPAL
# ======================================================================

def menu_consumo():
    """Exibe o menu de gerenciamento de consumo."""
    while True:
        print("\n=== GERENCIAMENTO DE CONSUMO DE INSUMOS ===")
        print("1. Registrar Consumo Manual (Integrado ao Estoque)")
        print("2. Ver Fila de Consumo (Ordem Cronológica de Registro)")
        print("3. Consultar Últimos Consumos (Ordem Inversa)")
        print("4. Buscar um Consumo por Nome do Insumo")
        print("5. Ordenar Histórico de Consumo")
        print("6. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            registrar_consumo_manual()
        elif opcao == '2':
            print("\n--- FILA ATUAL DE CONSUMO (FIFO) ---")
            for item in fila_consumo.ver_fila():
                print(f"Insumo: {item['insumo']}, Qtd: {item['quantidade']}")
        elif opcao == '3':
            ver_ultimos_consumos()
        elif opcao == '4':
            buscar_consumo_insumo()
        elif opcao == '5':
            ordenar_registros_consumo()
        elif opcao == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_principal():
    """Exibe o menu principal do sistema."""
    print("\n=== SISTEMA DE ESTOQUE DASA ===")
    print("1. Registrar novo produto")
    print("2. Atualizar preço de produto")
    print("3. Listar produtos (Estoque Atual)")
    print("4. Gerar relatório de atividades do sistema")
    print("5. Gerenciar Consumo de Insumos")
    print("6. Sair")
    return input("Escolha uma opção: ")


def main():
    """Função principal que executa o programa."""
    simular_dados_iniciais()
    while True:
        opcao = menu_principal()
        if opcao == '1':
            registrar_produto()
        elif opcao == '2':
            atualizar_preco()
        elif opcao == '3':
            listar_produtos()
        elif opcao == '4':
            gerar_relatorio()
        elif opcao == '5':
            menu_consumo()
        elif opcao == '6':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

