# Algoritmo de Multiplicacao de Karatsuba

## Descricao
Este projeto implementa o algoritmo de multiplicacao de Karatsuba em Python. 
O algoritmo de Karatsuba eh um metodo eficiente para multiplicacao de numeros grandes, reduzindo a complexidade em comparacao com a multiplicacao tradicional.

## Como Rodar o Projeto

1. Certifique-se de ter o Python instalado em sua maquina. 
   - Para verificar, execute no terminal:
     ```sh
     python --version
     ```
2. Baixe o arquivo contendo o codigo `karatsuba.py`.
3. Execute o script Python com o seguinte comando:
   ```sh
   python main.py
   ```
4. O programa ira imprimir os resultados das multiplicacoes realizadas pelo algoritmo de Karatsuba e a comparacao com a multiplicacao convencional.

## Logica do Algoritmo

O algoritmo de Karatsuba divide cada numero em duas partes:
- Parte mais significativa (high)
- Parte menos significativa (low)

Dado dois numeros `num1` e `num2`, a multiplicacao eh feita da seguinte forma:
1. Se um dos numeros for menor que 10, a multiplicacao eh feita diretamente.
2. Divide os numeros em duas partes:
   - `high1 = num1 // 10**m` → Obtém a parte mais significativa de `num1`, removendo os `m` últimos dígitos.
   - `low1 = num1 % 10**m` → Obtém a parte menos significativa de `num1`, pegando os `m` últimos dígitos.
   - `high2 = num2 // 10**m` → Obtém a parte mais significativa de `num2`, removendo os `m` últimos dígitos.
   - `low2 = num2 % 10**m` → Obtém a parte menos significativa de `num2`, pegando os `m` últimos dígitos.

3. Calcula tres multiplicacoes recursivas:
   - `low_product = karatsuba(low1, low2)` (multiplicacao das partes menos significativas)
   - `cross_terms_product = karatsuba((low1 + high1), (low2 + high2))` (soma das partes menos e mais significativas)
   - `high_product = karatsuba(high1, high2)` (multiplicacao das partes mais significativas)
4. Combina os resultados usando a formula:
   ```
   resultado = (high_product * 10^(2*m)) + ((cross_terms_product - high_product - low_product) * 10^m) + low_product
   ```

## Exemplo de Saida
```
 11111 x 22222 = 246908642
 11111 x 22222 = 246908642
 5634 x 96374 = 542948316
 5634 x 96374 = 542948316
 50 x 5 = 250
 50 x 5 = 250
```


# Análise de Complexidade do Algoritmo de Karatsuba

## Complexidade Ciclomática
A complexidade ciclomática do algoritmo de Karatsuba pode ser calculada a partir do fluxo de controle da função.

### Grafo de Fluxo de Controle
O grafo de fluxo é estruturado da seguinte forma:
1. Início da função.
2. Verificação do caso base (**if num1 < 10 or num2 < 10**).
3. Cálculo do tamanho dos números.
4. Divisão dos números em partes mais e menos significativas.
5. Três chamadas recursivas (**karatsuba** em partes menores).
6. Combinação dos resultados.
7. Retorno do resultado.

### Cálculo de complexidade
Utilizando a fórmula:
M= E - N + 2P

Onde:
- **E** é o número de arestas no grafo.
- **N** é o número de nós no grafo.
- **P** é o número de componentes conexos

Analisando o fluxo de controle do algoritmo, obtemos:
- **N = 7** (nós principais do fluxo de decisão e operações).
- **E = 8** (conexões entre os blocos do código).
- **P = 1**.

Assim, a complexidade ciclomática é:
M = 8 - 7 + 2(1) = 3


## Complexidade Assintótica

### Complexidade Temporal
O algoritmo de Karatsuba segue a relação de recorrência:

T(n) = 3T(n/2) + O(n)


Aplicando o **Teorema Mestre**, obtemos:

T(n) = O(n^{\log_2{3}}) \approx O(n^{1.5})


Ou seja, a complexidade temporal é **O(n^1.5)**, tornando-o mais eficiente que a multiplicação tradicional (**O(n^2)**) para números grandes.

#### Casos:
- **Melhor caso:** O(n) quando os números são pequenos e caem no caso base rapidamente.
- **Caso médio e pior caso:** O(n^1.5), pois a recursão sempre ocorre três vezes antes de combinar os resultados.

### Complexidade Espacial
A memória utilizada pelo algoritmo é dominada pelas chamadas recursivas.
- A profundidade da recursão é **O(log n)**.
- Cada chamada usa um espaço **O(1)** para armazenar variáveis locais.


---





