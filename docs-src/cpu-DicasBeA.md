# Dicas B/A

##  B

Não vamos ter o teste do `memoryIO` nem do `controlUnit` adequados para as mudanças, será necessário testar direto no Hardware:

1. Abrir Quartus e compilar projeto
1. Executar `programMyFPGA.py`

Como vocês alteraram o InstructionSet, será necessário escrever um programa em linguagem de máquina, para isso:

1. Altere o arquivo: `testeComputador.mif` com suas operações
1. Execute  `./programSoftware.py -m testeComputador.mif` para programar a ROM do Z01.1 com seu programa.

**Note que o arquivo `testeComputador.mif` possui um campo que é `DEPTH=30;` Você deve alterar esse valor para a quantidade de linhas que seu programa possui!**



## A

Para inserir o display sete segmentos (7s) será necessário:

1. Modificar o memoryIO
    - Adicionar novas saídas na `entity`
    - Adicionar periférico que recebe `vetor de bits` e converte para sinais do 7s
          - **Decoder**
1. Modificar Computador.vhd
    - Deve-se agora rotear os novos sinais do memoryIO para os pinos da FPGA, para isso modifique a entity do `Computador.vhd` para

```diff
entity Computador is
   generic(
        IS_SIMULATION : std_logic := '0'
   );
   port(
        -- Sistema
        CLOCK_50     : in    std_logic;
        RESET_N      : in    std_logic;
        LEDR         : out   std_logic_vector(9 downto 0);
        SW           : in    std_logic_vector(9 downto 0);

        -- LCD EXTERNAL I/OS
        LCD_CS_N     : out   std_logic;
        LCD_D        : inout std_logic_vector(15 downto 0);
        LCD_RD_N     : out   std_logic;
        LCD_RESET_N  : out   std_logic;
        LCD_RS       : out   std_logic;	      
        LCD_WR_N     : out   std_logic;
        LCD_ON       : out   std_logic;	

+       --- Seven Seg
+       HEX0    : out std_logic_vector(6 downto 0); -- 7seg0
+       HEX1    : out std_logic_vector(6 downto 0); -- 7seg1
+       HEX2    : out std_logic_vector(6 downto 0); -- 7seg2
+       HEX3    : out std_logic_vector(6 downto 0)  -- 7seg3
       );
end entity;
```

## Programando ROM com linguagem de máquina 

Uma vez implementando as modificações no HW não temos mais como realizar os testes lógicos na CPU (`testeHW` e `testeAssemblyMyCPU`), já que o nosso Assembler não está adequado para essas modificações. 

Uma alternativa para verificarmos se a alteração está certa é:
1. Compilar no Quartus o novo computador
1. Programar a FPGA com o novo HW `./programMyFPGA.py`
1. Escreva um programa em linguagem de máquina (adequado ao novo Instruction Set) que teste as novas funcionalidades.
    - Programa já em binário, extensão: `.mif`
    - Exemplo na pasta: `Projeto/G-CPU/testeComputador.mif`
1. Programar a memória da ROM com arquivo `.mif`: `./programSoftware -m Arquivo.mif`
1. Verificar a funcionalidade das modificações.

### Arquivo `.mif`

O  `.mif` é um formato de arquivo que possibilita carregarmos uma memória na FPGA, ele possui a seguinte estrutura:

```
WIDTH=18;
DEPTH=5;

ADDRESS_RADIX=UNS;
DATA_RADIX=BIN;

CONTENT BEGIN
  0 : 000000000000000101;
  1 : 100101100000010000;
  2 : 000000000000000001;
  3 : 100000000000100000;
  4 : 000000000000001011;
END;
```

- **Você deve editar a linha `DEPTH=5;` para a quantidade de linhas que seu programa possui!**

Esse arquivo é geralmente gerado pelo `Assembler`:

```
       assembler        
.nasm --------->  .mif 
                    v
                    |---------> FPGA
                    |---------> SIMULADOR
```

## Teclado como periférico

Adicionar os seguintes sinais na entidade do `Computador.vhd` e do `memoryIO.vhd`

```
 PS2_CLK : in std_logic;
 PS2_DAT : in std_logic;
```

E implementar a leitura das teclas no `memoryIO`. Dica:

- https://www.digikey.com/eewiki/pages/viewpage.action?pageId=28278929

