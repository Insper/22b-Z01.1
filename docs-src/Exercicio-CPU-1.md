# Exercicio CPU - 1

!!! info
    Os problemas aqui descritos são os mesmo do final do [LAB-15](/Z01.1/cpu-lab-1).

## CPU

Proponha uma modificação na `CPU` do nosso Z01.1 que:

 1. Adiciona mais um registrador (`%S`) (onde é melhor?)
 1. Você teria que modificar a linguagem de máquina do nosso HW. Proponha uma solução.
 1. Possibilita %D endereçar a memória 
     - `movw %A, (%D)`
 1. Possibilite fazer carregamento efetivo em %D
     - `leaw $5, %D`

Para cada modificação faça o desenho da nova CPU.

## Extras

### `nop`

Como o controlUnit controla a CPU para realizar a operação de NOP?

### `movw %D, %A e jg %D` ao mesmo tempo

Nossa CPU suportaria executar simultaneamente a instrução `movw %D, %A` e ao mesmo tempo a instrução `jg %D`? 

### `loadPC`

Quais sinais o influenciam?

