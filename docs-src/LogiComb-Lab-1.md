# Lab 4: FPGA - VHDL

| Material de estudos                                |
|----------------------------------------------------|
| https://insper.github.io/Z01.1/Teoria-Componentes/ |
| https://insper.github.io/Z01.1/VHDL-basico/        |
| https://insper.github.io/Z01.1/VHDL-Combinacional/ |

!!! info "Trabalhando"

    1. ![](https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png){width=30} Usar o Linux fornecido.
   
    1. Esse laboratório é para ser realizado individualmente. Ficar conectado no canal
    do grupo para descutir com os colegas.    

Este laboratório é introdutório para o desenvolvimento do projeto ([`B-Lógica-Combinacional`](/Z01.1/LogiComb-Projeto)), onde iremos criar componentes de hardware que serão os alicerces do nosso computador. Primeiro precisamos praticar um pouco de VHDL e entender a ferramenta e o fluxo de compilação, teste e programação (Quartus).

Após essa etapa, iremos começar o desenvolvimento do projeto, programando os módulos que virão a ser utilizados no computador Z01 (próximo lab).

<button class="button0" id="0:comecando" onClick="progressBut(this.id);">Começando laboratório!</button>

## Antes de começar

Toda vez que um novo projeto começar será necessário realizar algumas configurações no repositório do grupo, vocês devem seguir para o documento: [`Util/Começando novo Projeto`](/Z01.1/Util-Comecando-novo-projeto/) e depois voltar para esse lab.

!!! warning
    Não seguir sem realizar a etapa anterior.

<button class="button0" id="1:comencando-novo-projeto" onClick="progressBut(this.id);">Cheguei Aqui!</button>

## Entendendo a estrutura de pastas dos projetos

A pasta do projeto `B-LogicaCombinacional` no repositório Z01 possui a seguinte estrutura (assim como todos os demais projetos): 

```
/B-LogicaCombinacional
  testeLogicaCombinacional.py
  /Quartus
  /src
    *.vhd
  config_testes.txt
  /testes
    *.vhd
```

1. `Quartus`: Projeto Quartus que faz uso dos arquivos VHDL localizados em `src/rtl/*.vhd` 
     - Serve para programar a **FPGA**
1. `*.py`: Scripts em python automatiza a execução dos testes
1. `src/*.vhd`: Arquivos VHDL que serão implementado pelo grupo
1. `config_testes.txt`: Configuração dos testes
1. `testes/*.vhd`: Arquivos VHDL que realizam teste lógico nos arquivos do rtl

## Abrindo o Quartus


Abra o software do `Quartus` ![](figs/LogiComb/quartusIcon.png){width=30px} e clique em `File` :arrow_right: `Open Project` :arrow_right: escolha o projeto localizado na pasta `B-LogicaCombinacional/Quartus`. O arquivo que o Quartus irá reconhecer é o: `DE0_CV_Default.qpf` como no gif a seguir:

!!! tip
    Se não encontrar o software na barra de tarefas abra o terminal e escreva `quartus` :arrow_right: `enter`.

![Abrindo o Quartus](figs/LogiComb/Quartus1.gif)

Abra o arquivo `TopLevel.vhd` como demonstrado no gif anterior, este arquivo é o que chamamos de [top level](https://www.xilinx.com/support/documentation/sw_manuals/xilinx10/isehelp/pfp_p_toplevelhdl.htm) (pode-se fazer uma analogia com o `main` de um código), ele será o primeiro a ser executado na compilação e utilizará os demais módulos do sistema.

<button class="button0" id="2:abrindo-o-quartus" onClick="progressBut(this.id);">Cheguei Aqui!</button>

### Compilando o código

!!! note
    O código original disponível não realiza nenhuma lógica, repare que sua arquitetura está vazia!

Para compilarmos esse código VHDL basta irmos em: `Processing` :arrow_right: `Start Compilation`. A ferramenta irá "realizar" o código, ou seja, interpretar e torna-lo um hardware.

![Compilando](figs/LogiComb/Quartus2.gif)

<button class="button0" id="3:compilando" onClick="progressBut(this.id);">Cheguei Aqui!</button>

### RTL View

Podemos gerar a visão [RTL](https://en.wikipedia.org/wiki/Register-transfer_level) do código em vhdl, esse diagrama é a interpretação do código em VHDL pelo compilador e como ele seria supostamente implementando em hardware. Para isso: 

- `Tools` :arrow_right: `Netlist Viewers` :arrow_right: `RTL viewer`

Ele irá gerar o diagrama a seguir:

![Compilando](figs/LogiComb/Quartus3.png){width=450}

Onde podemos analisar que não existe nenhuma lógica que relaciona entrada com saída.

!!! note "RTL"
    O RTL aqui tem outro significado de quando foi utilizado com transistores, aqui é **Register-transfer level** e nos transistores é **Resistor–transistor logic**.

!!! info 
    SW = Switchs = Chaves da placa

!!! tip 
    Iremos utilizar bastante o RTL, aprenda a gerar e a interpretar! 

<button class="button0" id="4:rtl-view" onClick="progressBut(this.id);">Cheguei Aqui!</button>

### Modificando o projeto

Vamos modificar o arquivo `toplevel.vhd` do projeto para que o `bit 0` do vetor `LEDR` seja igual ao `bit 0` da chave `SW`, a arquitetura deve ficar como a seguir:

```vhdl
---------------
-- implementacao
---------------
begin
 
  LEDR(0) <= SW(0);

end rtl;
```

!!! example "Tarefa"
    1. Edite o toplevel
    1. Compile
    2. Gere o RTL Viewer novamente

O resultado deve ser o seguinte:

![Compilando](figs/LogiComb/Quartus-rtl2.png){width=450}

Onde o valor do `LEDR0` será o próprio valor de entrada chave `SW0`.

??? info "Programando a FPGA: Para quem estiver no insper"
    Essa etapa deve ser realizada somente para quem está 
    presente no insper.

    ![](figs/LogiComb/de0-cv.jpeg){wdith=10px}

    Para programar a FPGA você deve:
    
    - Conectar a placa via USB (não precisa da fonte)
    - Ligar a placa (botão vermelho)
    - Verificar se a chave SW10 está em 'run'

    No quartus vá em `Tools` :arrow_right: `Programmer`. Ele deve abrir uma nova interface:

    ![Programando](figs/LogiComb/quartus-pgr.gif)

    Mexa na chave SW0 e note que o LED irá acender conforme a chave é colocada na posição on.

<button class="button0" id="5:modificando" onClick="progressBut(this.id);">Cheguei Aqui!</button>

## Exercícios

Para cada desafio proposto a seguir, verifique se o RTL corresponde a lógica que deseja implementar. ~~Se estive no Insper teste o programa na FPGA:~~

1. Compile
1. Verifique o RTL
1. ~~Programe a FPGA (se estiver no insper)~~
    
!!! tip
    valide analisando o RTL ou programando a placa.

<button class="button0" id="6:exe1" onClick="progressBut(this.id);">Cheguei Aqui!</button>

!!! example "Tarefa"
    Faça a saída `LEDR(0)` ser o inverso da entrada `SW(0)`

<button class="button0" id="7:exe2" onClick="progressBut(this.id);">Cheguei Aqui!</button>

!!! example "Tarefa" 
    Faça a saída `LEDR(0)` ser a entrada `SW(0) ou SW(1)`

<button class="button0" id="8:exe3" onClick="progressBut(this.id);">Cheguei Aqui!</button>

!!! example "Tarefa"
    Faça:
    
    - `LEDR(0)` ser a entrada `SW(0) ou SW(1)` 
    - `LEDR(1)` ser a chave `SW(1)`

<button class="button0" id="9:exe4" onClick="progressBut(this.id);">Cheguei Aqui!</button>

!!! example "Tarefa"
    Faça TODOs os LEDs acenderem quando a seguinte combinação de entrada for:
  
    ```
    SW9               SW0
      1 0 0 1 1 0 1 0 1 0
    ```

<button class="button0" id="10:exe5" onClick="progressBut(this.id);">Cheguei Aqui!</button>

!!! example "Tarefa"
    Escreva um código VHDL para implementar o circuito a seguir:

    ![Circuito](figs/LogiComb/circuito.png){width=450}

    Sendo:

    - X: chave 0 (SW(0))
    - y: chave 1 (SW(1))
    - z: chave 2 (SW(2))

    **Dica:** encontre a equação, implemente em VHDL.

<button class="button0" id="11:exe6" onClick="progressBut(this.id);">Cheguei Aqui!</button>

--------------------------

## Sete segmentos

Note que na nossa FPGA possuímos seis [displays de sete segmentos](https://en.wikipedia.org/wiki/Seven-segment_display). 

![](figs/LogiComb/7seg.png)

Para termos acesso a esses displays, basta modificar a entidade do projeto para:

```vhdl
entity TopLevel is
    port(
        SW      : in  std_logic_vector(9 downto 0);
        HEX0    : out std_logic_vector(6 downto 0); -- 7seg0
        LEDR    : out std_logic_vector(9 downto 0)
    );
end entity;
```

Agora com um display de 7segementos mapeado como saída (`out`) na nossa `entity` podemos acionar cada led do display como descrito no manual da placa (isso só é possível pois o projeto já foi configurado corretamente antes pelo seu professor).

![](figs/LogiComb/7seg-manual.png){width=450}

!!! tip
    Para acender um segmento é necessário colocar `0` e para apagar `1`.

!!! example "Tarefa"
    1. Modifique a `entity` para possuir a nova saída
    1. Faça aparecer o número `5` no `HEX0`.

<button class="button0" id="12:7seg" onClick="progressBut(this.id);">Cheguei Aqui!</button>

<!--
## Adicionando um novo componente ao projeto

O desenvolvimento de projetos de hardware assim como os de softwares devem ser feitos de forma modular, onde especifica-se e implementa-se pequenos módulos (entidades) que são combinadas em sistemas cada vez mais complexos até chegar ao `TopLevel`. 

Para usarmos um novo componente no projeto é necessário:

1. Adicionar o arquivo ao projeto
1. Usar na arquitetura

### binário para BCD

Vamos inserir no `toplevel` um componente que faz a conversão de números binários para `BCD`, esse componente já está implementando e se encontra na pasta `B-LogicaCombinacional/src/` junto com outros módulos: 

- And16.vhd
- Mux8Way.vhd
- :arrow_right: binarioToBcd.vhd
- ...
- Nor8Way.vhd
- TopLevel.vhd

O módulo [`binarioToBcd.vhd`](https://github.com/Insper/Z01.1/blob/master/Projetos/B-LogicaCombinacional/src/rtl/binarioToBcd.vhd) possui a seguinte entidade (entradas e saídas):

```vhdl
entity binary_bcd is
    port(
        clk, reset: in std_logic;
        binary_in: in std_logic_vector(N-1 downto 0);
        bcd0, bcd1, bcd2, bcd3, bcd4: out std_logic_vector(3 downto 0)
    );
end binary_bcd ;
```

Esse módulo possui as seguintes interfaces: um vetor de entrada `binary_in` e cinco saídas (`bcd0` .. `bcd5`) e implementa um conversor de binário para BCD. 

!!! note "clock e rst"
    Além das portas descritas anteriormente, esse componente possui outras duas entradas: `clk` e `reset`, isso é necessário pois ele é um componente sequencial (ainda não vimos isso).

### Inserindo `binarioToBcd` no projeto

Para inserirmos o componente no projeto devemos:

- no `quartus` :arrow_right: `Project` :arrow_right: `Add/Remove files in Project`. 
Uma nova janela deve aparecer, nela clicar em `File name ...` e procurar pelo arquivo `binarioToBcd.vhd` que está na pasta `src/` um nível a cima. Ao final, clicar em `apply`.

![](figs/LogiComb/quartus-add-file.gif)

### Usando no `toplevel` 

Podemos inserir o conversor `binarioToBcd` no `toplevel` da seguinte maneira:

``` vhdl
begin
   u1 : work.binarioToBcd port map(clk   => CLOCK_50,
                                   reset => '0',
                                   binary_in => SW,
                                   bcd0  => LEDR(3 downto 0),
                                   bcd1  => LEDR(7 downto 4),
                                   bcd2  => open,
                                   bcd3  => open,
                                   bcd4  => open);
end rtl;
```

Essa linha de código pode ser lida como:

> Cria um componente chamada de **u1**, esse componente é uma implementação do `binarioToBcd`, nesse componente mapeasse a entrada `clk` para o pino `CLOCK_50`, a entrada `reset` para `0` e a entrada `binary_in` para as chaves da FPGA. Os dígitos 0 e 1 são exibidos nos LEDs e os demais deixamos desconectados.

Compilando o projeto podemos analisar o RTL gerado:

![](figs/LogiComb/rtl-binaryToBcd.png)

### Testando

!!! example "Tarefa"
    1. Compile
    1. Gere o RTL e análise 
    1. Programe a FPGA e teste (se estiver no insper)
    
        - você deve mudar as chaves SW e observar se os LEDs (3..0) e (7..4) estão acendendo corretamente.
        - Coloque a palavra 13 em binário nas chaves (1101) você deve obter: LED(3..0) = "0011" e os LED(7..4) = "0001".

-->


