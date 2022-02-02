# H - Assembler - Dica Macro

Suponha o seguinte arquivo .nasm :

```asm
%macro name nPar 
... ..
%endmacro
```

- name : Nome do macro
- nPar : Quantidade de parâmetros (0, 1, 2), acessível via : par0, par1

O macro serve para facilitar o reaproveitamento de códigos, diferente de uma função que altera o fluxo de execução do código para o endereço que a função está salva, o macro funciona copiando o macro para a onde ele foi chamado, como no exemplo a seguir:


Código sem macro :
``` asm
; carrega 5 em D
leaw $5, %A
movw %A, %D
 
; salva valor em RAM8
leaw $8, %A
movw %D, (%A)
```

Código com 2 macros definidos : 

- movCntToReg : Move uma constante (par0) para uma registrador (par1)
- movRegtoRAM : Move um registrador (par0) para o endereço de memória (par1).

``` asm
 %macro movCntToReg 2
 leaw par0, %A
 movw %A, par1
 %endmacro
 
 %macro movRegtoRAM 2
   leaw par0, %A
   movw par1, (%A)
 %endmacro
 
; carrega 5 em D
movCntToReg $D, %5
; chama macro para salvar em RAM 8
movRegtoRAM %D, $8
```