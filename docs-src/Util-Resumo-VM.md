# Linguagem VM

## Notação

- **Pilha**: Local onde a operação é executada
- **Primeiro endereço**: Dado no topo da pilha
- **Segundo endereço**: Segundo dado no topo da pilha
- **Stack Pointer**: Ponteiro para o endereço do dado no topo da pilha

```
     ...
     ...
      X     <- Segundo Valor
      Y     <- Primeiro Valor
SP ->
```

| Operação                                  | Argumentos | retorno | Descrição                            |
|-------------------------------------------|------------|---------|--------------------------------------|
| [add : Adição](#add-adicao)               | X, Y       | X       | X = X **+** Y                        |
| [sub : Subtração](#sub-subtracao)         | X, Y       | X       | X = X **-** Y                        |
| [neg : Negação](#neg-negacao)             | Y          | Y       | Y = **-** Y                          |
| [not : Not bit a bit](#not-not-bit-a-bit) | Y          | Y       | Y = **!** Y                          |
| [and : And bit a bit](#and-and-bit-a-bit) | X, Y       | X       | X = X **and** Y                      |
| [or  : Or bit a bit](#or-or-bit-a-bit)    | X, Y       | X       | X = X **or** Y                       |
| [eq  : Equal](#eq-equal)                  | X, Y       | X       | X = **True** if X = Y else **False** |
| [gt  : Greater Than](#gt-greater-than)    | X, Y       | X       | X = **True** if X > Y else **False** |
| [lt  : Less Than](#lt-less-than)          | X, Y       | X       | X = **True** if X < Y else **False** |

## Operações

### add - Adição

!!! note ""
    **add**

-  `X = X + Y`

A operação *add* adiciona dois valores da pilha, e retorna o resultado
no local do segundo valor.

??? tip "Pilha"
     ```
            ----------------------------------------
            |     Antes        |     Depois        |
            -------------------|--------------------
               ....            |             ....
                 X             |              X+Y
                 Y             |       SP ->
           SP ->               |        
     ```

---------------------------------------

### sub - Subtração

!!! note ""
    **sub**

-  `X = X-Y`

A operação *sub* subtrai dois valores da pilha, e retorna o resultado
no local do segundo valor.

---------------------------------------

### neg - Negação

!!! note ""
    **neg**

-  `Y = -Y`

A operação *neg* nega (complemento de dois) o valor no topo da pilha, e retorna o resultado
no mesmo local.

??? tip "Pilha"
     ```
            ----------------------------------------
            |     Antes        |     Depois        |
            -------------------|--------------------
               ....            |            ....
                 X             |              X
                 Y             |             -Y
           SP ->               |        SP ->
     ```

---------------------------------------

### not - not bit a bit 

!!! note ""
    **and**

-  `Y = !Y`

A operação *not* inverte (bit a bit) o valor no topo da pilha, e retorna o resultado
no mesmo local.

---------------------------------------

### or - Or bit a bit

!!! note ""
    **or**

-  `Y = X or Y`

A operação *or* aplica um or (bit a bit) com os valores no topo da pilha, e retorna o resultado
no segundo endereço.

---------------------------------------

### and - and bit a bit

!!! note ""
    **and**

-  `Y = X and Y`

A operação *and* aplica um or (bit a bit) com os valores no topo da pilha, e retorna o resultado
no segundo endereço.

---------------------------------------

### eq - Equal

!!! note ""
    **eq**

```
 X = True se X==Y ou
     False
```

A operação *eq* verifica se os dois valores no topo da pilha são iguais, re
retorna o resultado (True ou False) no segundo valor da pilha.

!!! tip "True/false"
    - 'True' é representando por todos os bits em '1': '0xFFFF'
    - 'False' é representando por todos os bits em '0': 0x0000'

!!! warning "Pilha"
    Essa operação consume os dois valores da pilha, veja exemplo.

??? tip "Pilha"
     ```
            ----------------------------------------
            |     Antes        |     Depois        |
            -------------------|--------------------
               ....            |            ....
                 X             |          True/False
                 Y             |        SP ->     
           SP ->               |        
     ```

----------------------------------

### gt - Greater Than

!!! note ""
    **gt**

```
 X = True se X>Y ou
     False
```

A operação *qt* verifica se o valor no topo da pilha é maior que o anterior,
retorna o resultado (True ou False) no segundo valor da pilha.

----------------------------------

### lt - Less Than

!!! note ""
    **lt**

```
 X = True se X<Y ou
     False
```

A operação *qt* verifica se o valor no topo da pilha é menor que o anterior,
retorna o resultado (True ou False) no segundo valor da pilha.
          
## Label

Labels são definidos pelo keyword **label** seguido de seu **nome** :

!!! note ""
    `label` **nome**

São utilizados para endereçar o código em uma condição de goto.

## Goto

Existem dois tipos de GOTO, condicional (**if-goto**) e incondicional (**goto**). No condicional o salto é realizado caso a condição não for Falsa (verifica sempre o último valor da pilha).

!!! note ""
    `goto` **nome**

    `if-goto` **nome**

## Função

A seguir definições de funções:

### Declaração de função 

Uma função é definida pelo keyword **function** seguido do seu **nome** e quantidade de variáveis locais **n** na estrutura a seguir :

!!! note ""
    function **nome** **n**

Toda função em VM deve possuir um retorno, definido pelo keyword **return**

??? example "Exemplo declaração de função"
    ```llvm
    funcion add 2
        push argument 0
        push argument 1
        add
    ```


### Chamada de função

Uma função em VM é chamada pelo keyword: **call** seguido do **nome** da função e da quantidade **m** de parâmetros passados para essa função.

!!! note ""
    call **nome** **m**


??? example "Exemplo chamada de função"
    ```llvm
      push constant 3
      push constant 2
      call mult 2
    ```

### Parâmetros

Os parâmetros de uma função são passados na própria pilha.


