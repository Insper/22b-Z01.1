# Tabela de Símbolos 

O Z01 possui alguns símbolos definidos para facilitar o desenvolvimento de um programa em assembly, por exemplo, não é preciso saber de cor que o LCD começa no endereço 16384, basta usarmos o símbolo SCREEN no código que o mesmo será substituído pelo valor 16384. Além de facilitar o desenvolvimento, possibilita uma maior portabilidade já que o compilador que é encarregado de substituir o valor, se o endereço  uma maior portabilidade do código. 

## Símbolos padrões

Esse são os símbolos que são definidos estaticamente, sempre devem existir. Eles indicam um endereço da memória RAM. Exemplo :

``` asm
leaw $LED, %A
movd %D, (%A)
```


| Simb   | Endereço |
|--------|----------|
| R0-R15 |     0-15 |
| SP     |        0 |
| LCL    |        1 |
| ARG    |        2 |
| THIS   |        3 |
| THAT   |        4 |
| SCREEN |    16384 |
| LED    |    21184 |
| SW     |    21185 |

## Labels

São os símbolos que indicam um endereço da memória ROM, são utilizados pelas operações de salto para indicar o seu destino :

``` asm
LOOP:
leaw $LOOP, %A
jmp
```
## Endereços de memória

São endereços de memória criados automaticamente pelo assembler, será utilizado pela VM e futuramente pelo compilador para alocar variáveis no START_RAM_ADDRESS computador. Funciona da seguinte maneira :

``` asm
leaw $var, %A    
movw %D, (%A)
```

O Assembler deve alocar um endereço automaticamente ainda não utilizado para **var0**, o valor a ser alocado é a partir do endereço 16 da RAM.

| Simb | valor |
|------|-------|
| var0 |    16 |

**O nome da variável pode ser qualquer uma, desde que não repita um nome de label.**

# Exemplo

Vamos supor o código (que não faz nada coerente) a seguir:

```
 0:    leaw $x, %A
 1:    movw $1, (%A)
 2:  LOOP:
 3:    leaw $UPDATE, %A
 4:    je %D
 5:    nop
 6:    leaw $temp, %A
 7:    movw (%A), %A
 8:    addw %A, %S, %S
 9:    decw %D
10:    leaw $LOOP, %A
11:    jmp
12:    nop
13:  UPDATE:
14:    leaw $3, %A
15:    movw %S, (%A)
16:  END:
17:    leaw $END, %A
18:    jmp
19:    nop
```

A tabela de símbolos gerada deveria ser:

| Símbolos   |  Valor |
|------------|--------|
| R0         |      0 |
| R1         |      1 |
| ...        |    ... |
| R15        |     15 |
| SP         |      0 |
| LCL        |      1 |
| ARG        |      2 |
| THIS       |      3 |
| THAT       |      4 |
| SCREEN     |  16384 |
| LED        |  21184 |
| SW         |  21185 |
|------------|--------|
| **x**      | **16** |
| **y**      | **17** |
| **LOOP**   |  **2** |
| **UPDATE** | **12** |
| **END**    | **14** |
