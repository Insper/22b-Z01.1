# Aritmética Binária - HW

- Conteúdo: hald-adder/ full-adder/ somador

!!! tip
    Esse conteúdo está no cap. 2 do livro texto da disciplina [The Elements of Computing Systems](https://b1391bd6-da3d-477d-8c01-38cdf774495a.filesusr.com/ugd/44046b_f0eaab042ba042dcb58f3e08b46bb4d7.pdf).

Precisamos lembrar que nosso objetivo principal é a criação de um hardware capaz de operar com números binários. Nessa teoria iremos analisar algumas técnicas de realizar o hardware necessário para realizar operação de soma binária entre dois vetores. Para isso iremos definir dois componentes: Half-Adder e o Full-Adder.

## half-adder (HAD)

[`Half-Adder` (HAD)](https://en.wikipedia.org/wiki/Adder_(electronics)) é um circuito digital capaz de somar dois bits (`a` e `b`), tem como resultado o valor da `soma` e do `carry`, como ilustrado a seguir: 

```
        ------
  a -->|      |--> Soma
       |  HA  |
  b -->|      |--> Carry
        ------
```

O `HAD` possui a seguinte tabela verdade:

| a   | b   | Carry (out) | Soma (out) |
| --  | --  | -----       | -----      |
| `0` | `0` | `0`         | `0`        |
| `0` | `1` | `0`         | `1`        |
| `1` | `0` | `0`         | `1`        |
| `1` | `1` | `1`         | `0`        |

E é implementado em hardware da seguinte maneira:

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Half_Adder.svg/440px-Half_Adder.svg.png){width=300}

> Fonte: https://en.wikipedia.org/wiki/Adder_(electronics)

## full-adder (FAD)

<iframe width="571" height="286" src="https://www.youtube.com/embed/RK3P9L2ZXk4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Full-adder é um componente digital capaz de somar três vits (`a`, `b` e `c`) e possui como saída o valor da `soma` e do `carry` resultante da operação. A seguir um diagrama de blocos de um `FAD`:

![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/1-bit_full-adder.svg/440px-1-bit_full-adder.svg.png)

> Fonte: https://en.wikipedia.org/wiki/Adder_(electronics)

O FAD possui a seguinte tabela verdade:

| a   | b   | c   | Carry (out) | Soma (out) |
| --  | --  | --  | -----       | -----      |
| `0` | `0` | `0` | `0`         | `0`        |
| `0` | `0` | `1` | `0`         | `1`        |
| `0` | `1` | `0` | `0`         | `1`        |
| `0` | `1` | `1` | `1`         | `0`        |
| `1` | `0` | `0` | `0`         | `1`        |
| `1` | `0` | `1` | `1`         | `0`        |
| `1` | `1` | `0` | `1`         | `0`        |
| `1` | `1` | `1` | `1`         | `1`        |

E é implementado da seguinte maneira em portas lógicas:

![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Full-adder_logic_diagram.svg/440px-Full-adder_logic_diagram.svg.png){width=500}

> Fonte: https://en.wikipedia.org/wiki/Adder_(electronics)

!!! tip
    Você deve ser capaz de encontrar esses circuitos analisando a tabela verdade e simplificando via Mapa de K.
    
    ![](figs/Teoria/Adders-kmap-FAD.png)
    
    Note que existem duas abordagens para representar o Carry_out: `A.B+A.C+B.C`e `A.B+C(A xor B)`
    
    > Fonte: (2011) Fundamentals of Digital and Computer Design with VHDL, pg 199.

## Somador

!!! tip
    <iframe width="571" height="302" src="https://www.youtube.com/embed/NO7Gt8IDSGA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Utilizando o FAD somos capazes de realizar um somador de dois vetores binários. Para isso, teremos que utilizar um full-adder para cada bit desse nosso vetor. 

Por exemplo: se formos criar um Somador capaz de somar dois vetores de `4bits`, necessitamos utilizar 4 FAD para isso com a ligação descrita a seguir:

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/4-bit_ripple_carry_adder.svg/2560px-4-bit_ripple_carry_adder.svg.png)

> Fonte: https://en.wikipedia.org/wiki/Adder_(electronics)

Nesse diagrama, estamos realizando a soma ente os vetores `A(3 downto 0)` e `B(3 downto 0)` que resulta em um outro vetor `S(3 downto 0)` e um carry `C4`.


