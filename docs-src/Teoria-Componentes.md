# Componentes Digitais

!!! success "2022-1"
    Material atualizado.

Aqui iremos alguns dos inúmeros componentes combinacionais
(não precisam de clock) que são utilizados no desenvolvimento de circuitos digitais e que serão usados na disciplina.

## portas lógicas

![](figs/Exercicios/AlgebraBooleana-componentes.png)

``` vhd
S <= A and B;  
S <= A nand B; S <= not (A and B)
S <= A or B;
S <= A nor B;  S <= not (A or B);
S <= A xor B; 
S <= (not A);
```

- and
- nand
- or
- nor
- xor
- not

## Multiplexado (mux)

![](https://upload.wikimedia.org/wikipedia/commons/b/b2/Multiplexer2.png)

> [fonte wikipedia](https://en.wikipedia.org/wiki/Multiplexer): Schematic of a 2-to-1 Multiplexer. It can be equated to a controlled switch.

```vhdl
entity mux is port(
     in0 : in  std_logic;
     in1 : in  std_logic;
     sel : in  std_logic;
       o : out std_logic);
end entity;
```

O mux como é chamado o [Multiplexador](https://www.electronics-tutorials.ws/combination/comb_2.html) é um componente que possui `n` entradas e uma saída `q`, um sinal chamado de seletor `sel` seleciona qual entrada irá ser copiada para a saída.

As entradas `n` e a saída `q` podem ser binárias ou vetor de tamanho `m`. 

A seguir uma tabela verdade para um `mux` de 2 entradas:

| in 0                | in 1               |     Sel |   out |
| ------------------- | ------------------ | ------- | ----- |
| 1                   | X                  |       0 |     1 |
| X                   | 0                  |       1 |     0 |
| 0                   | X                  |       0 |     0 |
| X                   | 1                  |       1 |     1 |
    
!!! note
    A tabela verdade do mux de 2 entradas possuir 2^3 linhas (o seletor conta como entrada), totalizando 8 linhas. Porém para simplificar, utilizamos o `X` que significa tanto faz (`0` ou `1`), logo cada linha que possui `X` seria expandida para duas linhas.
    
!!! tip
    O tamanho do seletor deve ser um numero inteiro: $log2(size(n))$. 
    
    | Quantidade de entras | Tamanho do seletor |
    |  ------------------- | ------------------ |
    |                    2 |                  1 |
    |                    3 |                  2 |
    |                    4 |                  2 |
    |                    5 |                  3 |
    |                    8 |                  3 |



## Demutiplexador  (demux)

É similar com o mux só que possui uma entrada `in` e `n` saídas `q`, o demux conecta a entrada a alguma das saídas, sendo controlado pelo seletor.

![](https://upload.wikimedia.org/wikipedia/commons/4/48/Demultiplexer.png)
>  [fonte wikipedia](https://en.wikipedia.org/wiki/Multiplexer): Schematic of a 1-to-2 Demultiplexer. Like a multiplexer, it can be equated to a controlled switch. 

```vhdl
    entity demux is
      port(
            in0   : in  std_logic;
            sel   : in  std_logic;
            out0  : out std_logic;
            out1  : out std_logic
      );
    end entity;
```


A entrada `in` e a saída `q` podem ser binárias ou de vetorer de tamanho `m`. 

A seguir uma tabela verdade para um `demux` de 2 saídas:

|                  in |                Sel |   out 0 | out 1 |
| ------------------- | ------------------ | ------- | ----- |
|                   1 |                  0 |       1 |     0 |
|                   1 |                  1 |       0 |     1 |
|                   0 |                  1 |       0 |     0 |
|                   0 |                  0 |       0 |     0 |


## Enconders 

Enconders são componentes que codificam uma entrada em uma saída de outro formato, algum exemplos são:

- BCD
- Gray code
- SevenSeg
- [Priority Encoder](https://en.wikipedia.org/wiki/Priority_encoder)

### BCD

[`Binary-coded decimal`](https://en.wikipedia.org/wiki/Binary-coded_decimal) (BCD) é uma forma de codificação de números inteiros em binário na qual utiliza-se para cada dígito de um número inteiro, 4 bits em binário.

| Decimal Number | BCD 8421 Code  |
| -------------- | -------------  |
|             0  | 0000 0000      |
|             01 | 0000 0001      |
|             02 | 0000 0010      |
|             03 | 0000 0011      |
|             04 | 0000 0100      |
|             05 | 0000 0101      |
|             06 | 0000 0110      |
|             07 | 0000 0111      |
|             08 | 0000 1000      |
|             09 | 0000 1001      |
|       10 (1+0) | 0001 0000      |
|       11 (1+1) | 0001 0001      |
|       12 (1+2) | 0001 0010      |
|       continua | em blocos de 4 |

```
             |-----------|
             |           |  out1[3..0]
   x[n..0]   |  Binary   |-----/-------->
 ----/------>|    to     |  ....
             |   BCD     |  outm[3..0]
             |           |-----/-------->
             |-----------|
```

```vhdl
    entity binaryToBCD is
      port(
            x    : in  std_logic(4 downto 0);
            out0 : out std_logic_vector(3 downto 0); -- Unidade
            out1 : out std_logic_vector(3 downto 0)  -- Dezena
      );
    end entity;
```


!!! tip
    O maior valor que um bloco de 4 bits do BCD assume é o `1001` que é referente ao número inteiro 9.

O BCD é bastante utilizado para o controle de displays de 7 segmentos, como demonstrado na figura a seguir que usa o chip 

![](https://www.electronics-tutorials.ws/wp-content/uploads/2016/01/bin10.gif?fit=408%2C211)

> [fonte electronics-tutorials](https://www.electronics-tutorials.ws/binary/binary-coded-decimal.html)

### Código Gray

O [código gray](https://pt.wikipedia.org/wiki/C%C3%B3digo_de_Gray) é uma forma de codificar números binários, nessa codificação apenas um bit muda por vez. 

| Código decimal | Código Binário | Código Gray |
|  ------------- |  ------------- |    -------- |
|              0 |           0000 |        0000 |
|              1 |           0001 |        0001 |
|              2 |           0010 |        0011 |
|              3 |           0011 |        0010 |
|              4 |           0100 |        0110 |
|              5 |           0101 |        0111 |
|              6 |           0110 |        0101 |
|              7 |           0111 |        0100 |
|              8 |           1000 |        1100 |
|              9 |           1001 |        1101 |
|             10 |           1010 |        1111 |
|             11 |           1011 |        1110 |
|             12 |           1100 |        1010 |
|             13 |           1101 |        1011 |
|             14 |           1110 |        1001 |
|             15 |           1111 |        1000 |

!!! note
    Esse sistema era muito utilizado antigamente quando relés eram utilizados no lugar de transistor, em um contador binário comum ocorre de muitos bits mudarem de uma única vez (0111 -> 1000) isso gerava um pico de corrente elétrica e muito ruído.

!!! tip
    Utilizamos o código Gray para montar o Mapa de Karnaugh

## Comparador

Comparadores são componentes que podem possuir diversos atributos, tais como comparar:

-  se duas entradas são iguais
-  se a entrada A é maior que entrada B
-  se entrada A é igual a zero
-  ...

A seguir um exemplo de um comparador que possui apenas uma entrada `x[1..0]` e compara se essa entrada é **igual** a zero (`x == 0`), ou **maior que** zero (`x > 0`).

| x (inteiro) | x binário | eq | gt |
|-------------|-----------|----|----|
|           0 |        00 |  1 |  0 |
|           1 |        01 |  0 |  1 |
|          -1 |        11 |  0 |  0 |
|          -2 |        10 |  0 |  0 |


```
             |-----------|
             |           |  eq
  x[1..0]    |           |---------->
 ----/------>| comparador|
             |           |  gt
             |           |---------->
             |-----------|

```

```vhdl
    entity COMPARADOR is
      port(
            x  : in  std_logic_vector(1 downto 0);
            eq : out std_logic;
            gt : out std_logic
      );
    end entity;
```




## Somadores

Os somadores são componentes que realizam a soma de dois números binários, eles podem ser construídos de diversas maneiras. 

```
 in0[1..0]   |-----------|
 ----/------>|           |
             |           |  out[2..0]
             |  ADDER    |-----/----->
 in1[1..0]   |           |
 ----/------>|           |
             |-----------|

```


```vhdl
    entity ADDER is
      port(
            in0   : in  std_logic(1 downto 0);
            in1   : in  std_logic(1 downto 0);
            o     : out std_logic_vector(2 downto 0)
      );
    end entity;
```

Um somador de dois vetores de dois bits cada possui o seguinte comportamento:

| in0 | in1 | out |
| --- | --- | --- |
|  00 |  00 | 000 |
|  00 |  01 | 001 |
|  01 |  01 | 010 |
|  10 |  01 | 011 |
|  10 |  11 | 101 |
|  11 |  11 | 110 |
