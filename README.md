# Challenge-Dynamic

# Sistema de Controle de Estoque DASA
Objetivo:
Este sistema foi desenvolvido para o desafio DASA e tem como objetivo gerenciar o estoque de insumos em diferentes locais, permitindo o registro, atualização e acompanhamento de produtos, quantidades e preços. O sistema também mantém um histórico das principais atividades realizadas.

# Funcionalidades
Registrar novo produto:
Permite cadastrar um novo produto no estoque, informando nome, quantidade e preço unitário. O sistema calcula automaticamente o preço total do produto.

Atualizar preço de produto:
Permite atualizar o preço unitário de um produto já existente. O preço total é recalculado e a alteração é registrada no histórico.

Listar produtos cadastrados:
Exibe todos os produtos cadastrados, mostrando nome, quantidade, preço unitário e preço total, ordenados alfabeticamente.

Gerar relatório de atividades:
Mostra as últimas 10 ações realizadas no sistema, incluindo registros de novos produtos e atualizações de preços.

Sair:
Encerra o sistema de forma segura.

Bibliotecas Utilizadas
datetime
Usada para registrar a data e hora de cada atividade no histórico do sistema.

Estrutura de Dados
Dicionário (estoque)
Cada produto é uma chave, com um dicionário aninhado contendo quantidade, preço unitário, preço total e preço ideal.

Lista (historico)
Armazena strings descrevendo as atividades realizadas no sistema, com data e hora.

Funções Principais
calcular_preco_total(quantidade, preco_unitario)
Calcula o preço total de um produto.

registrar_produto()
Solicita dados do produto e registra no estoque.

atualizar_preco()
Atualiza o preço unitário de um produto já cadastrado.

listar_produtos()
Lista todos os produtos cadastrados com seus dados.

gerar_relatorio()
Mostra o histórico das últimas 10 atividades.

menu()
Exibe o menu principal e retorna a opção do usuário.

main()
Função principal que executa o sistema de menu interativo.

Execute o arquivo com Python 3:

text
python estoque_dasa.py
Siga as instruções do menu interativo.
