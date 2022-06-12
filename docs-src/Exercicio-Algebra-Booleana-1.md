# Álgebra Booleana - 1

[![](figs/pdf.png){width=25} Versão para impressão.](https://github.com/Insper/Z01.1/raw/main/Exercicios/Exercicio-Algebra-Booleana-1.pdf)

!!! tip ""
    [:pencil: Resolução](https://github.com/Insper/Z01.1/blob/master/Exercicios/Exercicio-Algebra-Booleana-1-resolucao.pdf)


!!! exercise text short
    Indique o nome dos elementos lógicos a seguir:

    ![](figs/Exercicios/AlgebraBooleana-componentes.png)
    
    !!! answer
        and, nand, or, nor, xor, not

----------------

### Tabela verdade

!!! exercise text short
    A tabela verdade a seguir representa qual porta lógica?

    | A | B | OUT |
    |---|---|-----|
    | 0 | 0 |   0 |
    | 0 | 1 |   1 |
    | 1 | 0 |   1 |
    | 1 | 1 |   0 |
    
    !!! answer
        xor

!!! exercise text short
    A tabela verdade a seguir representa qual porta lógica?

    | A | B | OUT |
    |---|---|-----|
    | 0 | 0 |   1 |
    | 0 | 1 |   1 |
    | 1 | 0 |   1 |
    | 1 | 1 |   0 |
    
    !!! answer
        nand

----------------

!!! exercise choice "Pergunta"
    Aplicando a lei da Distributividade na expressão $A(B+\bar{C}+D)$ se tem:

    - [ ] $A . B + A . C + A . D$
    - [ ] $A . B . C . D$
    - [ ] $A + B + C + D$
    - [X] $A B + A\bar{C} + A . D$


    !!! answer
        $A B + A\bar{C} + A . D$
        
----------------

!!! exercise choice "Pergunta"
    Aplicando o teorema de DeMorgan na expressão $\overline{ABC}$, obtém:

    - [x] $\bar{A}+\bar{B}+\bar{C}$
    - [ ] $\overline{A+B+C}$
    - [ ] $A + \bar{B} + C \bar{C}$
    - [ ] $A . (B+C)$

    !!! answer
        $\bar{A}+\bar{B}+\bar{C}$
        
----------------

!!! exercise choice "Pergunta"
    Qual simplificação está incorreta:

    - [x] $\overline{(\bar{x}+\bar{y})} = \bar{\bar{x}}*\bar{y} = x * \bar{y}$ 
    - [ ] $x ( \bar{x} + y ) = x . \bar{x} + x . y = 0 + x . y = x . y$
    - [x] $x . y + x ( y + z ) = x . y + x . y + z = x . y + z$
    - [ ] $\bar{x} . \bar{y} . z + \bar{x} . y . z + x . \bar{y} = \bar{x} . z (\bar{y} + y) + x . \bar{y} = \bar{x} . z + x . \bar{y}$

    !!! answer
        $\overline{(\bar{x}+\bar{y})} = \bar{\bar{x}}*\bar{y} = x * \bar{y}$ e $x . y + x ( y + z ) = x . y + x . y + z = x . y + z$

----------------

!!! exercise choice "Pergunta"
    Qual forma canônica está correta?

     | **A** | **B** | **Q** |
     |-------|-------|-------|
     |     0 |     0 |     1 |
     |     0 |     1 |     0 |
     |     1 |     0 |     0 |
     |     1 |     1 |     1 |

    - [ ] $Q = A \bar{B} + A \bar{B}$
    - [ ] $Q = A+B * \bar{A} \bar{B}$
    - [ ] $Q = A . B$
    - [x] $Q = \bar{A} . \bar{B} + A . B$
       
    !!! answer
        $Q = \bar{A} . \bar{B} + A . B$

----------------

!!! exercise
    Dado a seguinte tabela verdade (entradas A, B e C, e a saída Q):

     | **A** | **B** | **C** | **Q** |
     |-------|-------|-------|-------|
     |     0 |     0 |     0 |     1 |
     |     0 |     0 |     1 |     0 |
     |     0 |     1 |     0 |     0 |
     |     0 |     1 |     1 |     1 |
     |     1 |     0 |     0 |     1 |
     |     1 |     0 |     1 |     0 |
     |     1 |     1 |     0 |     0 |
     |     1 |     1 |     1 |     1 |
 
    1. Crie uma fórmula em álgebra booleana que represente a tabela via SoP e PoS.
    > SoP: Soma dos Produtos / PoS: Produto das Somas
    1. Simplifique SoP (interprete o resultado!)
    1. Desenhe um circuito usando os símbolos da álgebra booleana. 

----------------

!!! exercise text short
    Quantas saídas com 1 existem na tabela verdade que resulta na seguinte fórmula de soma de produtos:

    $A \bar{B} \bar{C} + \bar{A} B C + \bar{A} B \bar{C} + A \bar{B} \bar{C} + A B C$
    
    !!! answer
        4

----------------

!!! exercise text short
    Qual é a expressão em álgebra booleana do seguinte circuito:

    ![](figs/Exercicios/Algebra-Booleana-1.png)
    
    !!! answer
        $G = (A+B) C D E$

----------------

!!! exercise
    Gere a Tabela Verdade das equações a seguir:

    1. $A . B + \overline{B + A}$
    1. $A \oplus B$
    1. $(A \, and \, B) \, or \, C$

----------------

!!! exercise
    Converta a seguinte expressão em Soma de Produtos para Produto de Somas:

    $A . B . C + A \bar{B} \bar{C} + A . \bar{B} C + A . B . \bar{C} + \bar{A} . \bar{B} . C$

    1. Faça a tabela verdade
    1. Encontre o PoS

----------------

!!! exercise text short
    Determine os valores de A, B, C e D que fazem a fórmula a seguir ser igual a zero (Z = 0).

    $Z = \bar{A} + B + \bar{C} + D$

    !!! answer
        "1010"
        
----------------

!!! exercise choice "Pergunta"
    Qual das seguintes propriedades da álgebra booleana é falsa:

    - [ ] $A . (\bar{A} + B)= A . B$
    - [x] $A + (\bar{A} . B) = A$
    - [ ] $A + \bar{A} = 1$
    - [ ] $A . A = A$
       
    !!! answer
        $A + (\bar{A} . B) = A$

----------------

!!! exercise text short
    Simplifique a seguinte expressão:

    $\bar{A} \bar{B} \bar{C} + \bar{A} B C + \bar{A} B \bar{C} + A \bar{B} \bar{C} + A B \bar{C}$

    !!! answer
        $\bar{C} + \bar{A} B C$
        
----------------

!!! exercise
    Encontre as equações para os mapas de Karnaugh a seguir:

    ![](figs/Exercicios/AlgebraBooleana-MK-1.png)

----------------

!!! exercise
    Crie o mapa de Karnaugh e encontre a equação da tabela verdade a seguir.

     | **A** | **B** | **C** | **OUT** |
     |-------|-------|-------|---------|
     |     0 |     0 |     0 |       1 |
     |     0 |     0 |     1 |       1 |
     |     0 |     1 |     0 |       0 |
     |     0 |     1 |     1 |       1 |
     |     1 |     0 |     0 |       0 |
     |     1 |     0 |     1 |       1 |
     |     1 |     1 |     0 |       0 |
     |     1 |     1 |     1 |       0 |


----------------

!!! exercise
    Crie o mapa de Karnaugh da tabela verdade de quatro entradas.

     | **A** | **B** | **C** | **D** | **OUT** |
     |-------|-------|-------|-------|---------|
     |     0 |     0 |     0 |     0 |       0 |
     |     0 |     0 |     0 |     1 |       1 |
     |     0 |     0 |     1 |     0 |       0 |
     |     0 |     0 |     1 |     1 |       0 |
     |     0 |     1 |     0 |     0 |       0 |
     |     0 |     1 |     0 |     1 |       1 |
     |     0 |     1 |     1 |     0 |       0 |
     |     0 |     1 |     1 |     1 |       0 |
     |     1 |     0 |     0 |     0 |       0 |
     |     1 |     0 |     0 |     1 |       1 |
     |     1 |     0 |     1 |     0 |       1 |
     |     1 |     0 |     1 |     1 |       1 |
     |     1 |     1 |     0 |     0 |       0 |
     |     1 |     1 |     0 |     1 |       1 |
     |     1 |     1 |     1 |     0 |       0 |
     |     1 |     1 |     1 |     1 |       1 |

----------------

!!! exercise
    Crie o mapa de Karnaugh para a expressão a seguir e simplifique:

    $ABC\bar{D} + \bar{A}\bar{B}CD + A \bar{B}\bar{C}D + \bar{A} + \bar{B} + \bar{C} + \bar{D}$       

----------------

!!! exercise
    A seguinte expressão foi resultado da forma canônica do produto de somas de uma tabela verdade para a produção de um circuito lógico. O objetivo é simplificar a álgebra booleana dessa lógica para o menor número possível de portas, porém visivelmente quem fez essa fórmula não percebeu que se tivesse feito a soma de produtos já partiria com um número menor de termos. Converta essa fórmula para a soma de produtos e minimize-a.

    $(A+B+C)(A+B+\bar{C})(A+\bar{B}+C)(\bar{A}+B+C)(\bar{A}+\bar{B}+C)$

    > dica: Equação -> tabela verdade -> soma dos produtos

----------------

Acabou? Os exercícios não param por aqui, tem a [parte 2!](/Z01.1/Exercicio-Algebra-Booleana-2)
