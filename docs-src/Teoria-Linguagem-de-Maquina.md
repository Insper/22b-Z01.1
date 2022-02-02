# Linguagem de máquina

> Um programa em código de máquina consiste em uma sequência de bytes que correspondem a instruções que serão executadas pelo processador. As instruções do processador, chamadas de opcodes, são representadas por valores em hexadecimal.
>
> Fonte: https://pt.wikipedia.org/wiki/C%C3%B3digo_de_m%C3%A1quina

É o que efetivamente será convertido em binário e gravado na memória de programa para ser lido e interpretado pela CPU. Essa conversão é realizada normalmente um por software chamado de Assembler ou Montador. Ele é responsável por converter os OPCODES (`leaw`) no código de máquina (`000000101010`).

Uma linguagem de máquina é específica para um [Conjunto de instruções](https://pt.wikipedia.org/wiki/Conjunto_de_instru%C3%A7%C3%B5es) (`instruction set`), que define os recursos de hardware que uma determinada CPU oferece (uso de registradores, operações aritméticas, operações lógicas, ...). 

Fabricantes de chips tendem a modificar o instruction set melhorando o HW entre gerações, essas mudanças tem que ser feito de modo que permita que códigos antigos executem em hardwares mais modernos (retrocompatibilidade).

!!! info "Defeito de ponto flutuante"
    Em 1994, a Intel cometeu um erro no projeto do primeiro processador Pentium que causou um prejuízo devido a um recall de US$ 450.000.000, esse bug de hardware fazia com que raramente uma conta de ponto flutuante tivesse resultado errado.
    
    - Para saber mais a respeito: https://pt.wikipedia.org/wiki/Defeito_de_ponto_flutuante
    
!!! info "Pentium F00F bug"
    É um bug descoberto em 1997 que quando uma instrução específica: `F0 0F C7 C8` fosse executada no hardawre, o mesmo travava e só voltava ao normal com um reset.

    - Para saber mais a respeito: https://en.wikipedia.org/wiki/Pentium_F00F_bug

## Z01

A linguagem de máquina utilizada no curso é adaptada do livro Texto com umas pequenas mudanças, ela possui 18 bits de largura e cada bit possui uma ação direta sobre a CPU, esse tipo de linguagem de máquina é chamado de [**microcode**](https://en.wikipedia.org/wiki/Microcode).

!!! note
    CPUs mais complexas não possuem essa relação de que cada bit da instrução controla algum funcionamento direto (sinal) da CPU.

A seguir a definição da linguagem de máquina da nossa CPU:

![](figs/Hardware/IS-Z011.svg)

### Instruções do tipo A

Instruções do tipo A são aquelas que possibilitam o carregamento efetivo de um dado salvo no programa (ROM) para dentro da CPU. É a maneira que possuímos de carregar uma constante no nosso hardware. Essas instruções são definidas pelo `bit17 = 0`.

No versão atual da CPU só possuímos uma instrução nessa categoria, a `leaw`.

!!! example "exemplo"
    - `leaw $3, %A`
    - `000000000000000011`
    
### Instruções do tipo C

Instruções do tipo C são aquelas que computam alguma coisa (númerico ou lógico), movem dados, ou realizam mudanças no Program Counter (salto / jump condicional ou não-condicional). Essas instruções são definidas pelo `bit17 = 1`.

!!! example 
    - `addw %A, %D, %D`
    - `10000000010010000`
