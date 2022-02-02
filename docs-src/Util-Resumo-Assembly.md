# Z01 - Resumo Assembly

!!! tip "Notação"
    - **reg** : Registrador (`%A`, `%D`)
    - **mem** : Acesso a memória (%A)
    - **im**: Imediato, pode ser: (`$1`, `$0`, `$-1`)
    - **const**: Constante positiva (`$0`, `$9`, ....)

!!! note "Arquivos: extensões"
    - `.nasm`: Arquivo assembly
    - `.hack`: Linguagem de máquina (arquivo com zeros e uns)
    - `.mif `: Arquivo .hack que pode ser salvo na memória da FPGA
    - `.lst `: saída do simulador com os estados da CPU

!!! warning
    Nosso hardware não suporta operações que realizam escrita e leitura na memória RAM ao mesmo tempo. Operações como:
    
    - `incw (%A)`
    - `decw (%A)`
    - `addw (%A), %D, (%A)`
    - `subw %D, (%A), (%A)`
    - ...
    
    Vão ser aceitas pelo assembler, mas vão executar erradas no HW.

## Instruções

#### LEA - Carregamento Efetivo do Endereço (Valor)

!!! note ""
    **leaw** const, reg

!!! warning "Restrição"
    A operação de **leaw** só aceita o registrador `%A`

A instrução *leaw* armazena o valor passado (`const`) no
registrador especificado 

```nasm
; Exemplo: %A = 15
leaw $15, %A
```

---------------------------------------

#### MOV - Copia Valores

!!! note ""
    **movw** im*/reg/mem, reg/mem {, reg/mem, reg/mem}

!!! tip "Dica"
    A operação de mov faz na verde uma cópia, deixando a origem com o 
    dado original.

 A instrução *mov,* copia o valor da primeira posição para
a segunda posição (terceira e quarta opcional).

```nasm
; Exemplo: D = RAM[A]
movw (%A), %D
```

---------------------------------------

#### ADD - Adição de Inteiros

!!! note ""
    **addw** reg/mem, reg/mem/im*, reg/mem {, reg/mem, reg/mem}

!!! tip "Dica"
    A operação permite salvar o resultado em mais de um destino.

 instrução add, soma o primeiro valor ao segundo
valor e armazena o resultado no terceiro parâmetro (quarto e quinto
opcional).

```nasm
; Exemplo: D = RAM[A]+D 
addw (%A), %D, %D
```

---------------------------------------

#### SUB - Subtração de Inteiros

!!! note ""
     **subw** reg/mem, rem/mem/im*, reg/mem {, reg/mem, reg/mem}

 A instrução sub, subtrai o segundo valor do primeiro
valor e armazena o resultado no terceiro parâmetro (quarto e quinto
opcional).

```nasm
; Exemplo: A = D - RAM[A] 
subw %D, (%A), %A
```

---------------------------------------

#### RSUB - Subtração de Inteiros Reversa

!!! note ""
     **rsubw** reg/mem/im*, rem/mem, reg {, reg, reg}

 A instrução rsub, subtrai o segundo valor do primeiro
valor e armazena o resultado no terceiro parâmetro (quarto e quinto
opcional).


```nasm
; Exemplo: A = RAM[A] - D
rsubw %D, (%A), %A
```

---------------------------------------

#### INC - Incrementa Inteiro

!!! note ""
     **incw** reg

!!! warning "Restrição"
    O destino é o próprio registrador! A operação não permite
    salvar em um registrador diferente.
    
!!! tip "Dica"
    Se quiser fazer a operação de **inc** e salvar em outro 
    registrador, pode utilizar a operação de **addw**:
    
    ```nasm
    ; D = A + 1
    addw $1, %A, %D 
    ```

 A instrução *inc,* adiciona um (1) ao valor do
registrador ou memória.


```nasm
; Exemplo: D = D + 1
incw %D
```

---------------------------------------

#### DEC - Decrementa Inteiro

!!! note ""
     **decw** reg
 
A instrução *dec,* subtrai um (1) do valor do registrador
ou memória.

```nasm
; Exemplo: A = A-1
decw %A
```

---------------------------------------

#### NOT - Negação por Complemento de Um

!!! note ""
    **notw** reg
    
A instrução *not,* inverte o valor de cada bit do reg origem, ou seja,
se um bit tem valor 0 fica com 1 e vice-versa.

```nasm
; Exemplo:  D = !D
notw %D
```

---------------------------------------

#### NEG - Negação por Complemento de dois

!!! note ""
     negw reg

 A instrução *neg,* faz o valor ficar negativo, ou seja,
um valor de x é modificado para -x.


```nasm
; Exemplo: A = -A
 negw %A
```

---------------------------------------

#### AND - Operador E (and)

!!! note ""
     andw reg/mem, rem/mem

 A instrução *and* executa o operador lógico E (and).

```nasm
; Exemplo: D = A&D
andw %A, %D, %D
```

---------------------------------------

#### OR - Operador OU (or)

!!! note ""
    orw reg/mem, rem/mem

 A instrução *or* executa o operador lógico Ou (or).


```nasm
; Exemplo: D = RAM[A] | D
orw (%A), %D, %D
```

---------------------------------------

#### JMP - Jump

!!! note ""
     jmp

 A instrução *jmp* executa um desvio, no fluxo de
execução, para o endereço armazenado em %A.

```nasm
jmp
```

---------------------------------------

#### JE - Desvia Execução se Igual a Zero

!!! note ""
     je reg

 A instrução *je* faz um desvio, no fluxo de execução,
para o endereço armazenado em %A, somente se o valor do reg. for igual a
zero.

```nasm
je %D
```

---------------------------------------

#### JNE - Desvia Execução se Diferente de Zero

!!! note ""
     jne reg

 A instrução *jne* faz um desvio, no fluxo de execução,
para o endereço armazenado em %A, somente se o valor do reg. for
diferente de zero.

```nasm
jne %D
```

---------------------------------------

#### JG - Desvia Execução se Maior que Zero

!!! note ""
     jg reg

A instrução *jg* desvia, o fluxo de execução, para o
endereço armazenado em %A, somente se o valor do reg. for maior que
zero.

```nasm
jg %D
```

---------------------------------------

#### JGE - Desvia Execução se Maior Igual a Zero

!!! note ""
     jge reg

 A instrução *jge* faz um desvio, no fluxo de execução,
para o endereço armazenado em %A, somente se o valor do reg. for maior
ou igual a zero.

```nasm
jge %D
```

---------------------------------------

#### JL - Desvia Execução se Menor que Zero

!!! note ""
     jl reg

 A instrução *jl* faz desvio, no fluxo de execução, para o
endereço armazenado em %A, somente se o valor do reg. for menor que
zero.

```nasm
jl %D
```

---------------------------------------

#### JLE - Desvia Execução se Menor Igual a Zero

!!! note ""
     jle reg

 A instrução *jle* faz um desvio, no fluxo de execução,
para o endereço armazenado em %A, somente se o valor do reg. for menor
ou igual a zero.

```nasm
jle %D
```

---------------------------------------

#### NOP - Não faz nada (No Operation)

!!! note ""
     nop

 A instrução *nop* não faz nada, usado para pular um ciclo
de execução.

```nasm
nop
```

---------------------------------------

## Descrição Detalhada

**Formato das Instruções**

Em Assembly, codificamos uma instrução por linha e ela é construída a
partir do mnemônico da operação e seus argumentos. Além disso, temos
marcadores de posição (endereço usado em desvios), constantes e
possíveis variáveis. O formato das instruções na sintaxe AT&T segue o
seguinte formato:

mnemônico origem, destino

**Registradores**

Todos os registradores devem ter como prefixo o sinal de porcentagem
'%\', por exemplo: %A ou %D.

**Valores Literais**

Todos os valores literais devem ter como prefixo o sinal de cifrão
'\$\', por exemplo: \$55, \$376, sendo o maior valor 2047 (15 bits).

**Endereçamento de Memória**

Na sintaxe AT&T, a memória é referenciada com parêntese em volta do
registrador que armazena o endereço: por exemplo (%A).

**Tamanho dos operadores**

Algumas instruções podem trabalhar com diferentes tamanhos de dados,
assim as instruções podem ter um sufixo, informando o tamanho do dado
que irá manipular, sendo b (8 bits), w (16 bits) e l (32 bits). Por
exemplo:

 movw $2000, (%A)

**Instruções de Transferência de Controle**

As instruções de jump, fazem o fluxo do programa desviar de uma posição
do programa para outra. Para marcar as posições no programa, são usados
marcadores (labels) que sempre terminam com dois pontos (:). Por
exemplo: loop:

**Registradores virtuais**

Os símbolos R0, ..., R15 são automaticamente predefinidos para se
referir aos endereços de RAM 0, ..., 15

**Ponteiros de I/O**

Os símbolos SCREEN e KBD são automaticamente predefinidos para se
referir aos endereços de RAM 16384 e 24576, respectivamente.

**Ponteiros de controle da VM**

Os símbolos SP, LCL, ARG, THIS, e THAT são automaticamente predefinidos
para se referir aos endereços de RAM 0-4, respectivamente.

**Notações:**

im : valor imediato (somente os valores 1, 0 e -1).

reg : registrador.

mem: memória, ou seja (%A).

**Limitações:**

-   A arquitetura não permite somar o valor da memória apontada por (%A)
    com o valor de %A, ou de (%A) com (%A), tampouco %A com %A.

-   Não é possível somar (ou subtrair, se é que isso faz sentido) o
    registrador com o mesmo, por exemplo somar %D com %D.

-   Não é possível ler e gravar a memória ao mesmo tempo. Por exemplo,
    as instruções abaixo não funcionam no nosso computador:

    -   incw (%A);
    -   subw (%A),%D,(%A).

**Observação:**

A linguagem Assembly apresentada é especifica para o processador
produzido no curso. Embora muito similar a outras usadas em produtos de
mercado, as instruções possuem limitações inerentes a cada hardware.

