#  SISTEMA DE CONTROLE DE ESTOQUE E CONSUMO DASA
Integrantes: Caio Rossini (RM:555084), Gabriel Danius (RM:555747) e Enzo Motta (RM:555372)

1. Descrição do Problema
Em unidades de diagnóstico, o controle preciso do consumo diário de insumos (reagentes, descartáveis) é um desafio. A falta de registros detalhados dificulta a gestão de estoque e a previsão de reposição, podendo levar à falta de materiais críticos ou a compras desnecessárias.

Este projeto propõe uma solução baseada em estruturas de dados e algoritmos clássicos para simular e organizar os dados de consumo, permitindo um controle mais eficiente e a geração de relatórios estratégicos.

2. Como Executar o Código
Salve o código acima em um arquivo chamado ChallengeDynamic.py.

Abra um terminal ou prompt de comando.

Navegue até o diretório onde você salvou o arquivo.

Execute o comando: python sistema_estoque_dasa.py

O programa iniciará, simulará dados de consumo iniciais e exibirá o menu principal.

3. Explicação das Estruturas e Algoritmos Utilizados
3.1. Fila e Pilha
Fila (Queue)
Conceito: Uma estrutura de dados do tipo FIFO (First-In, First-Out), onde o primeiro elemento a ser inserido é o primeiro a ser removido. Funciona como uma fila de pessoas em um banco.

Aplicação no Problema: Foi implementada a classe Fila para registrar o consumo diário de insumos. Cada vez que um insumo é consumido, ele é adicionado (enfileirar) ao final da fila. Isso garante que os registros sejam mantidos em ordem cronológica estrita. O registro mais antigo é sempre o que está no início da fila, refletindo a ordem natural dos acontecimentos.

Pilha (Stack)
Conceito: Uma estrutura de dados do tipo LIFO (Last-In, First-Out), onde o último elemento inserido é o primeiro a ser removido. É como uma pilha de pratos.

Aplicação no Problema: Foi implementada a classe Pilha para simular consultas que priorizam os dados mais recentes. Na função ver_ultimos_consumos, todos os registros de consumo são inseridos (empilhar) em uma pilha. Em seguida, os itens são removidos (desempilhar) um a um para exibição. O resultado é uma lista de consumos em ordem cronológica inversa, mostrando os eventos mais recentes primeiro, o que é útil para análises gerenciais rápidas.

3.2. Estruturas de Busca
Para localizar um insumo específico no grande volume de registros de consumo, foram implementados dois algoritmos de busca.

Busca Sequencial
Conceito: Um algoritmo simples que percorre a lista de dados do início ao fim, um item de cada vez, até encontrar o valor desejado ou chegar ao final da lista. Sua complexidade é O(n).

Aplicação no Problema: A função busca_sequencial é ideal quando não temos garantia de que os dados estão ordenados. Ela permite que o usuário procure por um insumo em qualquer situação, embora seja menos eficiente para grandes volumes de dados.

Busca Binária
Conceito: Um algoritmo muito mais eficiente, com complexidade O(logn), que funciona dividindo repetidamente a lista de busca pela metade. Pré-requisito crucial: a lista deve estar ordenada.

Aplicação no Problema: A função busca_binaria oferece uma performance superior. No nosso sistema, antes de realizar a busca binária, o programa primeiro ordena a lista de consumo pelo nome do insumo. Isso demonstra a importância da organização dos dados para a eficiência dos algoritmos.

3.3. Algoritmos de Ordenação
Para organizar os dados de consumo e extrair informações valiosas (ex: qual insumo é mais consumido? quais estão com a validade mais próxima?), implementamos dois algoritmos de ordenação eficientes do tipo "dividir para conquistar".

Merge Sort
Conceito: Um algoritmo que divide a lista em metades, ordena cada metade recursivamente e, em seguida, mescla (merge) as duas metades ordenadas para formar a lista final. Sua complexidade é garantida em O(nlogn) em todos os casos, mas requer memória auxiliar para a mesclagem.

Aplicação no Problema: O merge_sort foi implementado para organizar os registros de consumo por quantidade ou data de validade. Sua estabilidade e performance previsível o tornam uma escolha robusta para a geração de relatórios confiáveis.

Quick Sort
Conceito: Também um algoritmo de "dividir para conquistar", ele escolhe um elemento como pivô e particiona a lista, colocando elementos menores que o pivô à sua esquerda e maiores à sua direita. O processo é então aplicado recursivamente a cada sub-lista. Sua complexidade média é O(nlogn) e geralmente é mais rápido na prática que o Merge Sort por não exigir memória extra (opera in-place).

Aplicação no Problema: O quick_sort é oferecido como uma alternativa ao Merge Sort para as mesmas tarefas de ordenação. A inclusão de ambos os algoritmos permite comparar na prática duas soluções clássicas e eficientes para o mesmo problema.

4. Conclusão
Este projeto demonstra como a aplicação de estruturas de dados (Fila, Pilha) e algoritmos fundamentais (Busca Sequencial/Binária, Merge Sort/Quick Sort) pode transformar dados brutos de consumo em um sistema de controle de estoque organizado e funcional. As soluções implementadas não apenas resolvem o problema proposto, mas também fornecem as bases para um sistema escalável e eficiente de gestão de insumos em unidades de diagnóstico.
