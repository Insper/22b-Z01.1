# Números binários

- Conteúdo: Complemento de um/ Complemento de dois/ Ponto fixo/ Soma binária/ 

Podemos utilizar números binários para codificar qualquer tipo de dado, como vimos na teoria de dados digitais. Mas ainda não sabemos como utilizar números binários para representar: números inteiros que possam ser negativos e números reais (exe: `1,032`). Essa teoria irá tratar desses temas e também da parte referente a operações com números binários (soma e subtração).

## Soma binária

<iframe width="831" height="468" src="https://www.youtube.com/embed/NFTG-VGkik8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

A soma binária é realizada de maneira similar a soma de decimais, só que precisamos notar que `1` + `1` em binário (**esse um é de soma não de OR**), resulta em `10`, esse `1` do estouro e que passa para a próxima casa é chamado de `carry`. Esse `carry` é similar ao `vai um` em uma soma decimal, no caso quando somamos `9` + `3` o resultado é `12`. 

!!! note "Exemplos consideram"
    - Somador de 8 bits
    - Números inteiros não sinalizados

- 0xAA + 0x55 = 0xFF

```
                          : Carry
     1 0 1 0 1 0 1 0      : A 
     0 1 0 1 0 1 0 1 +    : B
     ---------------  
     1 1 1 1 1 1 1 1      : Resultado (A+B)
```

Precisamos perceber que cada bit é armazenado 'real', um sistema com `8` bits não consegue armazenar `9` bits, e se houver um estouro no último bit essa informação será perdida.

- 0x80 + 0x80 = 0x100, mas resulta em **0x00** por conta do somador ser 8 bits:

```
carry é perdido
   1
    \
     1 0 0 0 0 0 0 0 
     1 0 0 0 0 0 0 0 +
     ---------------
     0 0 0 0 0 0 0 0
```

- 0x03 + 0x81 = 0x84

```
               1 1        : carry (vai um)
                  \       
     0 0 0 0 0 0 1 1 
     1 0 0 0 0 0 0 1 +
     ---------------
     1 0 0 0 0 1 0 0    
```


## complemento de 1

!!! warning
    Forma 'errada' de armazenar números sinalizados (+, -)
    
No complemento de 1, utilizamos a casa mais significativa de um vetor de bits para representar se o número é positivo (`0`) ou negativo (`1`). Exemplo (utilizando 4 bits):

- Valor **+1** em binário, com complemento de 1

```
    0001
    ^
    | indica que o valor é positivo
```

- Valor **-1** em binário, com complemento de 1

```
    1001
    ^
    | indica que o valor é negativo
```

O problema do complemento de 1 é que:

- Possuímos duas representações para o valor 0: `0000` e `1000`
- Operações de soma não funcionam corretamente entre os dois números codificados em complemento de 1.

## Complemento de 2

<iframe width="613" height="460" src="https://www.youtube.com/embed/NED9IIpteXA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

O complemento de dois é uma outra maneira de representar números sinalizados com bits, para obter um número positivo <-> negativo nessa notação é necessário seguir os seguintes passos:

1. Inverter todos os bits (not bit a bit) da palavra original 
1. Somar um a palavra invertida


