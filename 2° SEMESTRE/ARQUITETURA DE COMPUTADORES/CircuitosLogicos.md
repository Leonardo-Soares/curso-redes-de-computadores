# Tema: Circuitos Lógicos

# Conceito de Circuitos Lógicos
Os circuitos lógicos são componentes que trabalham com operações booleanas ou binárias (0 e 1,  Verdadeiro e Falso ou High e Low), sendo elas : **E (AND)**, **OU (OR)**, **NOT (NÃO)**. Os CI’s (Circuitos Integrados) lógicos são componentes que possuem um agrupamento de portas lógicas em seu componente, capazes de identificar e executar a lógica de Boole (Lógica Booleana), através da tensão nos pinos de entrada, identificando os valores altos ou baixos nos pinos e enviando a resposta correspondente ao pino de saída.

# Tipos 

## 1 - NOR
### A diferença para a porta lógica OR é o fato de  ela possuir uma NOT em sua saída, ou seja, o resultado será o mesmo invertendo o valor.

| A   | B   | Resultado  |
| --- | --- | :---------:|
| 0   | 0   | ``` 1```   |
| 0   | 1   | `0`        |
| 1   | 0   | `0`        |
| 1   | 1   | `0`        |

## 2 - NAND
### A diferença para a porta lógica AND é o fato de ela possuir uma NOT em sua saída, ou seja, o resultado será o mesmo invertendo o valor.

| A   | B   | Resultado  |
| --- | --- | :---------:|
| 0   | 0   | ``` 1```   |
| 0   | 1   | ``` 1```   |
| 1   | 0   | ``` 1```   |
| 1   | 1   | `0`        |

## 3 - XOR
### O resultado será positivo quando houver "variações" na tabela verdade

| A   | B   | Resultado  |
| --- | --- | :---------:|
| 0   | 0   | `0`        |
| 0   | 1   | ``` 1```   |
| 1   | 0   | ``` 1```   |
| 1   | 1   | `0`        |

## 4 - XNOR 
### O resultado será positivo quando ouver "afirmações" na tabela verdade

| A   | B   | Resultado  |
| --- | --- | :---------:|
| 0   | 0   | ``` 1```   |
| 0   | 1   | `0`        |
| 1   | 0   | `0`        |
| 1   | 1   | ``` 1```   |


[Veja detalhes a respeito da tabela verdade](../introducao)
# Referências
[FilipeFlop](https://www.filipeflop.com/blog/circuitos-logicos-logica-booleana-em-cis/)
 
