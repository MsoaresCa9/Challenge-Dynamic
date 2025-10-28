Compreendido\! Você quer um `README.md` mais dinâmico e amigável para exibição, evitando tabelas markdown que podem não renderizar bem em todas as plataformas ou que você prefere evitar. Vou reestruturar o `README.md` para ser mais fluído e descritivo, usando listas e texto corrido.

Aqui está a nova versão do `README.md`:

---

# 📚 SISTEMA DE CONTROLE DE ESTOQUE DASA

**Integrantes:** Caio Rossini, Gabriel Danius e Enzo Motta
**RM:** 555084, 555747 e 555372



## 1. Descrição do Problema

Este projeto aborda o desafio do controle preciso de estoque e da previsão de reposição de insumos em unidades de diagnóstico. A ausência de registros detalhados e uma gestão otimizada pode levar a faltas de materiais críticos ou a compras excessivas e desnecessárias.

Nossa solução utiliza **Estruturas de Dados** e **Algoritmos Clássicos** para organizar e processar os dados de consumo. Além disso, introduz um módulo de **Programação Dinâmica** focado na **otimização da alocação orçamentária** para a compra de insumos, garantindo que os recursos sejam utilizados da forma mais eficiente possível para manter o estoque adequado.

## 2. Como Executar o Código

Para iniciar o sistema, siga estes passos simples:

1.  Salve o código completo em um arquivo Python, por exemplo, `sistema_estoque_dasa.py`.
2.  Abra seu terminal ou prompt de comando.
3.  Navegue até o diretório onde você salvou o arquivo.
4.  Execute o comando: `python sistema_estoque_dasa.py`
5.  O programa carregará dados simulados iniciais de estoque e consumo e apresentará o menu principal.

---

## 3. Explicação das Estruturas e Algoritmos Utilizados

O sistema integra diversas estruturas de dados e algoritmos fundamentais para gerenciar o estoque e o consumo de insumos de forma eficiente.

### 3.1. Estruturas Clássicas

* **Fila (Queue - FIFO: First-In, First-Out):**
    * **Conceito:** Como uma fila de banco, o primeiro a entrar é o primeiro a sair.
    * **Aplicação:** Utilizada para registrar e visualizar o histórico de consumo de insumos em **ordem estritamente cronológica**. Isso é essencial para entender a sequência de uso. (Acessível via Menu 5, Opção 2).

* **Pilha (Stack - LIFO: Last-In, First-Out):**
    * **Conceito:** Pense em uma pilha de pratos, o último prato colocado é o primeiro a ser retirado.
    * **Aplicação:** Usada para consultar os consumos de forma a priorizar os eventos mais recentes, mostrando-os em **ordem inversa** (do mais novo para o mais antigo). Ideal para análises rápidas sobre o uso recente. (Acessível via Menu 5, Opção 3).

### 3.2. Algoritmos de Busca

* **Busca Sequencial ($O(n)$):**
    * **Conceito:** Percorre a lista item por item até encontrar o que busca.
    * **Aplicação:** Útil para encontrar um insumo específico no histórico de consumo quando a ordem dos dados não é garantida ou para listas pequenas.

* **Busca Binária ($O(\log n)$):**
    * **Conceito:** Um método muito mais rápido que divide a lista pela metade repetidamente, mas exige que a lista esteja **ordenada**.
    * **Aplicação:** Demonstra a eficiência de busca em listas maiores. No sistema, a lista de consumo é primeiro ordenada pelo nome do insumo antes da busca binária ser executada.

### 3.3. Algoritmos de Ordenação

* **Merge Sort ($O(n \log n)$):**
    * **Conceito:** Divide a lista em partes menores, ordena essas partes e depois as combina. É conhecido por sua performance consistente em todos os cenários.
    * **Aplicação:** Usado para organizar o histórico de consumo por critérios como **Quantidade Consumida** ou **Data de Validade**, fornecendo relatórios confiáveis e bem estruturados.

* **Quick Sort ($O(n \log n)$ em média):**
    * **Conceito:** Escolhe um "pivô" e reorganiza a lista em torno dele, recursivamente ordenando as sub-listas. Geralmente mais rápido na prática que o Merge Sort.
    * **Aplicação:** Oferecido como uma alternativa eficiente ao Merge Sort para as mesmas tarefas de ordenação do histórico de consumo.



## 4. Programação Dinâmica: Otimização de Alocação de Insumos

Este é um módulo chave que utiliza Programação Dinâmica (PD) para resolver um problema complexo de decisão: **como alocar um orçamento limitado para a compra de insumos de forma a maximizar seu valor estratégico.**

### 4.1. Formulação do Problema 

O problema modelado é uma variação do **Problema da Mochila (Knapsack 0/1)**, adaptado para o controle de estoque do DASA.

* **Objetivo:** Maximizar o "valor estratégico total" dos insumos a serem adquiridos.
* **Restrição:** Respeitar um **orçamento máximo** pré-definido.
* **Estados:** Representado por $DP[i][b]$, que é o **valor máximo** que podemos obter ao considerar os **primeiros $i$ insumos** com um **orçamento disponível de $b$**.
* **Decisões:** Para cada insumo $i$, o sistema decide entre:
    * **Não Incluir o Insumo:** Mantém o orçamento e o valor dos insumos anteriores.
    * **Incluir o Insumo:** Se o custo do insumo couber no orçamento, adiciona seu valor e reduz o orçamento.
* **Função de Transição:** A relação que define o cálculo do valor máximo para um estado atual com base em estados anteriores é:
    $$DP[i][b] = \max(DP[i-1][b], \text{valor}_i + DP[i-1][b - \text{custo}_i])$$
    (Onde $\text{custo}_i$ é o preço para garantir a quantidade mínima de segurança do insumo $i$, e $\text{valor}_i$ é uma pontuação de importância estratégica desse insumo).
* **Função Objetivo:** O resultado final é o valor máximo encontrado em $DP[N][B]$, onde $N$ é o número total de insumos e $B$ é o orçamento máximo.

### 4.2. Implementações e Prova de Equivalência
O código oferece e compara **três implementações** da solução de Programação Dinâmica, demonstrando as diferentes abordagens para resolver o mesmo problema e provando que todas chegam ao mesmo resultado:

1.  **Versão Recursiva Pura:** Esta é a implementação mais direta da função de transição. Embora conceitualmente clara, sua complexidade de tempo é exponencial ($O(2^N)$), tornando-a impraticável para um grande número de insumos.
2.  **Versão com Memorização (Top-Down):** Otimiza a versão recursiva armazenando os resultados de subproblemas já resolvidos em um dicionário (tabela de memorização). Isso evita recálculos desnecessários, reduzindo a complexidade para $O(N \cdot B)$.
3.  **Versão Iterativa (Bottom-Up):** Constrói a solução de forma incremental, preenchendo uma tabela $DP[i][b]$ do menor subproblema para o maior. Esta é a abordagem mais eficiente na prática para PD, mantendo a complexidade de tempo em $O(N \cdot B)$.

**Prova de Equivalência:** No menu de "Otimizar Alocação" (Opção 7), o sistema executa as três versões do algoritmo com os mesmos dados de entrada. Ele então **verifica e reporta se todas as implementações produziram o mesmo resultado**, confirmando a correção e a validade das otimizações aplicadas.

